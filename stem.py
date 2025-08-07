import MatplotlibInterface
import json

def stem_nothink(text_in, client, llmmodel, prompt2, prompt3, prompt4, prompt5):
    # 第2阶段：提取数据与数据标签
    messages2 = [{"role": "user", "content": prompt2 + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
    print(openai_out)
    data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
    messages2.append({"role": "assistant", "content": openai_out})

    # 第3阶段：设计图表样式
    messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
    print(openai_out)
    style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

    # 第4阶段：设计图表刻度与范围
    messages4 = messages2 + [{"role": "user", "content": prompt4 + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
    print(openai_out)
    range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
    
    # 第5阶段：设计图表标签
    messages5 = messages2 + [{"role": "user", "content": prompt5 + text_in}]

    openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
    print(openai_out)
    label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

    # 作图
    fig = MatplotlibInterface.StemInterface(data["x"], data["y"], data["ylabel"],
                                            style["marker"], style["linelinestyle"], style["baselinestyle"], style["mcolor"], style["lcolor"], style["bcolor"],
                                            range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                            label["xlabel"], label["ylabel"], label["title"])
    return fig, style, range, label