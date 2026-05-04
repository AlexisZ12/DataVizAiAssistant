import MatplotlibInterface
import json
from concurrent.futures import ThreadPoolExecutor

def stairs(text_in, client, llmmodel, prompt2, prompt3, prompt4, prompt5):
    # 第2阶段：提取数据与数据标签（必须先执行）
    messages2 = [{"role": "user", "content": prompt2 + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
    print(openai_out)

    # 验证并解析JSON，如果验证失败则让LLM修正
    while True:
        try:
            data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
            # 检查字段名是否存在
            required_fields = ["position", "value", "label"]
            for field in required_fields:
                if field not in data:
                    raise KeyError(f"缺少必需字段 '{field}'")

            # 检查 position 字段：必须为一维数组，元素为 int 且连续递增
            if not isinstance(data["position"], list):
                raise TypeError("字段 'position' 必须是数组类型")
            if not all(isinstance(v, int) for v in data["position"]):
                raise TypeError("字段 'position' 的元素必须是 int 类型")
            # 检查连续递增
            for i in range(1, len(data["position"])):
                if data["position"][i] != data["position"][i-1] + 1:
                    raise ValueError("字段 'position' 的元素必须是连续递增的整数")

            # 检查 value 字段：必须为二维数组，元素为 int 或 float
            if not isinstance(data["value"], list):
                raise TypeError("字段 'value' 必须是数组类型")
            if not all(isinstance(row, list) for row in data["value"]):
                raise TypeError("字段 'value' 必须是二维数组")
            for row in data["value"]:
                if not all(isinstance(v, (int, float)) for v in row):
                    raise TypeError("字段 'value' 的元素必须是 int 或 float 类型")

            # 检查 label 字段：必须为一维数组，元素为 string
            if not isinstance(data["label"], list):
                raise TypeError("字段 'label' 必须是数组类型")
            if not all(isinstance(v, str) for v in data["label"]):
                raise TypeError("字段 'label' 的元素必须是 string 类型")

            # 检查维度匹配
            n = len(data["position"])
            m = len(data["label"])
            if len(data["value"]) != m:
                raise ValueError(f"字段 'value' 的行数({len(data['value'])})与 'label' 的长度({m})不匹配")
            for i, row in enumerate(data["value"]):
                if len(row) != n:
                    raise ValueError(f"字段 'value' 的第{i}行长度({len(row)})与 'position' 的长度({n})不匹配")

            # 验证通过，退出循环
            break
        except (json.JSONDecodeError, IndexError, KeyError, TypeError, ValueError) as e:
            print(f"JSON验证失败: {e}")
            # 让LLM修正，使用独立的message列表
            error_msg = f"你返回的JSON格式不正确，错误信息: {e}。请重新返回符合格式要求的JSON。"
            messages_retry = [{"role": "user", "content": prompt2 + text_in},
                              {"role": "assistant", "content": openai_out},
                              {"role": "user", "content": error_msg}]
            openai_out = client.chat.completions.create(model = llmmodel, messages = messages_retry).choices[0].message.content
            print(openai_out)

    messages2.append({"role": "assistant", "content": openai_out})

    # 并行调用辅助函数
    def call_llm(prompt):
        messages = messages2 + [{"role": "user", "content": prompt + text_in}]
        response = client.chat.completions.create(model = llmmodel, messages = messages).choices[0].message.content
        print(response)
        return json.loads("{" + response.split("{", 1)[1].split("}", 1)[0] + "}")

    # 第3、4、5阶段并行执行
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_style = executor.submit(call_llm, prompt3)
        future_range = executor.submit(call_llm, prompt4)
        future_label = executor.submit(call_llm, prompt5)

        style_config = future_style.result()
        range_config = future_range.result()
        label_config = future_label.result()

    # 作图
    fig = MatplotlibInterface.StairsInterface(data["value"], data["position"], data["label"],
                                              style_config["color"],
                                              range_config["xmin"], range_config["xmax"], range_config["xstep"], range_config["ymin"], range_config["ymax"], range_config["ystep"],
                                              label_config["title"], label_config["xlabel"], label_config["ylabel"])
    return fig, data, style_config, range_config, label_config
