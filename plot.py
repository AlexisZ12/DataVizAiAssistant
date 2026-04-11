import MatplotlibInterface
import json
from concurrent.futures import ThreadPoolExecutor

def plot(text_in, client, llmmodel, prompt2, prompt3, prompt4, prompt5):
    # 第2阶段：提取数据与数据标签（必须先执行）
    messages2 = [{"role": "user", "content": prompt2 + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
    print(openai_out)
    data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
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

        style = future_style.result()
        range = future_range.result()
        label = future_label.result()

    # 作图
    fig = MatplotlibInterface.PlotInterface(data["x"], data["y"], data["ylabel"],
                                            style["marker"], style["linestyle"], style["mcolor"], style["lcolor"],
                                            range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                            label["xlabel"], label["ylabel"], label["title"])
    return fig, data, style, range, label
