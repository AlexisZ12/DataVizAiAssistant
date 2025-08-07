import MatplotlibInterface
import json

def stairs_nothink(text_in, client, llmmodel, prompt2a6, prompt3a6, prompt4a, prompt5a):
    # 第2阶段：提取数据与数据标签
    prompt2 = prompt2a6
    messages2 = [{"role": "user", "content": prompt2 + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
    print(openai_out)
    data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
    messages2.append({"role": "assistant", "content": openai_out})

    # 第3阶段：设计图表样式
    prompt3 = prompt3a6
    messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
    print(openai_out)
    style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

    # 第4阶段：设计图表刻度与范围
    messages4 = messages2 + [{"role": "user", "content": prompt4a + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
    print(openai_out)
    range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
    
    # 第5阶段：设计图表标签
    messages5 = messages2 + [{"role": "user", "content": prompt5a + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
    print(openai_out)
    label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

    # 作图
    fig = MatplotlibInterface.StairsInterface(data["value"], data["position"], data["label"],
                                                style["color"],
                                                range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                label["title"], label["xlabel"], label["ylabel"])
    return fig, style, range, label