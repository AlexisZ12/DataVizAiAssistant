from openai import OpenAI
import json
import MatplotlibInterface
import io
from pywebio.input import *
from pywebio.output import *

with open('config/configExample.json', 'r', encoding = 'utf-8') as jsExample:
    jsEx = json.load(jsExample)
OpenAiConfigExample = jsEx['OpenAiConfigExample']
DeepSeekConfigExample = jsEx['DeepSeekConfigExample']
OllamaConfigExample = jsEx['OllamaConfigExample']
LmStudioConfigExample = jsEx['LmStudioConfigExample']

with open('prompt/a/prompt1a.txt', 'r', encoding='utf-8') as file:
    prompt1a = file.read()
with open('prompt/b/prompt1b.txt', 'r', encoding='utf-8') as file:
    prompt1b = file.read()
with open('prompt/a/prompt2a0.txt', 'r', encoding='utf-8') as file:
    prompt2a0 = file.read()
with open('prompt/a/prompt2a1.txt', 'r', encoding='utf-8') as file:
    prompt2a1 = file.read()
with open('prompt/a/prompt2a2.txt', 'r', encoding='utf-8') as file:
    prompt2a2 = file.read()
with open('prompt/a/prompt2a3.txt', 'r', encoding='utf-8') as file:
    prompt2a3 = file.read()
with open('prompt/a/prompt2a4.txt', 'r', encoding='utf-8') as file:
    prompt2a4 = file.read()
with open('prompt/a/prompt2a5.txt', 'r', encoding='utf-8') as file:
    prompt2a5 = file.read()
with open('prompt/a/prompt2a6.txt', 'r', encoding='utf-8') as file:
    prompt2a6 = file.read()
with open('prompt/b/prompt2b0.txt', 'r', encoding='utf-8') as file:
    prompt2b0 = file.read()
with open('prompt/b/prompt2b1.txt', 'r', encoding='utf-8') as file:
    prompt2b1 = file.read()
with open('prompt/b/prompt2b2.txt', 'r', encoding='utf-8') as file:
    prompt2b2 = file.read()
with open('prompt/b/prompt2b3.txt', 'r', encoding='utf-8') as file:
    prompt2b3 = file.read()
with open('prompt/b/prompt2b4.txt', 'r', encoding='utf-8') as file:
    prompt2b4 = file.read()
with open('prompt/b/prompt2b5.txt', 'r', encoding='utf-8') as file:
    prompt2b5 = file.read()
with open('prompt/b/prompt2b6.txt', 'r', encoding='utf-8') as file:
    prompt2b6 = file.read()
with open('prompt/a/prompt3a0.txt', 'r', encoding='utf-8') as file:
    prompt3a0 = file.read()
with open('prompt/a/prompt3a1.txt', 'r', encoding='utf-8') as file:
    prompt3a1 = file.read()
with open('prompt/a/prompt3a2.txt', 'r', encoding='utf-8') as file:
    prompt3a2 = file.read()
with open('prompt/a/prompt3a3.txt', 'r', encoding='utf-8') as file:
    prompt3a3 = file.read()
with open('prompt/a/prompt3a4.txt', 'r', encoding='utf-8') as file:
    prompt3a4 = file.read()
with open('prompt/a/prompt3a5.txt', 'r', encoding='utf-8') as file:
    prompt3a5 = file.read()
with open('prompt/a/prompt3a6.txt', 'r', encoding='utf-8') as file:
    prompt3a6 = file.read()
with open('prompt/b/prompt3b0.txt', 'r', encoding='utf-8') as file:
    prompt3b0 = file.read()
with open('prompt/b/prompt3b1.txt', 'r', encoding='utf-8') as file:
    prompt3b1 = file.read()
with open('prompt/b/prompt3b2.txt', 'r', encoding='utf-8') as file:
    prompt3b2 = file.read()
with open('prompt/b/prompt3b3.txt', 'r', encoding='utf-8') as file:
    prompt3b3 = file.read()
with open('prompt/b/prompt3b4.txt', 'r', encoding='utf-8') as file:
    prompt3b4 = file.read()
with open('prompt/b/prompt3b5.txt', 'r', encoding='utf-8') as file:
    prompt3b5 = file.read()
with open('prompt/b/prompt3b6.txt', 'r', encoding='utf-8') as file:
    prompt3b6 = file.read()
with open('prompt/a/prompt4a.txt', 'r', encoding='utf-8') as file:
    prompt4a = file.read()
with open('prompt/b/prompt4b.txt', 'r', encoding='utf-8') as file:
    prompt4b = file.read()
with open('prompt/a/prompt5a.txt', 'r', encoding='utf-8') as file:
    prompt5a = file.read()
with open('prompt/b/prompt5b.txt', 'r', encoding='utf-8') as file:
    prompt5b = file.read()
with open('prompt/a/prompt_newa1.txt', 'r', encoding='utf-8') as file:
    prompt_newa1 = file.read()
with open('prompt/a/prompt_newa2.txt', 'r', encoding='utf-8') as file:
    prompt_newa2 = file.read()
with open('prompt/b/prompt_newb1.txt', 'r', encoding='utf-8') as file:
    prompt_newb1 = file.read()
with open('prompt/b/prompt_newb2.txt', 'r', encoding='utf-8') as file:
    prompt_newb2 = file.read()
    
def main():
    
    while True:
        # 导入大模型
        with open('config/config.json', 'r', encoding = 'utf-8') as jsfile:
            js = json.load(jsfile)
            client = OpenAI(api_key = js['key'], base_url = js['base'])
            llmmodel = js['model']

        # 初始菜单
        input = input_group(
            "AI visualisation data analysis",
            [
                textarea("Please describe what you want to analyse:", rows = 20, placeholder="Elements analysed", name="demand"),
                select("Whether or not it forces thinking:", options=["Yes", "No"], value="No", name="flag"),
                actions(buttons=[{'label': 'Make the figure', 'value': 0},
                                 {'label': "Modify the configuration file", 'value': -1, 'color': 'warning'}], name="act")
            ]
        )

        if input['act'] == -1:
            while True:
                with open('config/config.json', 'r', encoding='utf-8') as file:
                    text = file.read()
                
                config = input_group(
                    "Modify the configuration file",
                    [
                        textarea(value = text, rows = 10, name = "text"),
                        actions(buttons = [{'label': 'Save', 'value': 1},
                                           {'label': 'OpenAi standard format', 'value': 2},
                                           {'label': 'DeepSeek standard format', 'value': 3},
                                           {'label': 'Ollama standard format', 'value': 4},
                                           {'label': 'LmStudio standard format', 'value': 5},
                                           {'label': 'Back', 'value': 0, 'color': 'warning'}], name='action')
                    ]
                )

                match config['action']:
                    case 0:
                        break

                    case 1:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            file.write(config['text'])
                        break

                    case 2:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            json.dump(OpenAiConfigExample, file, ensure_ascii=False, indent=4)

                    case 3:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            json.dump(DeepSeekConfigExample, file, ensure_ascii=False, indent=4)
                    
                    case 4:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            json.dump(OllamaConfigExample, file, ensure_ascii=False, indent=4)

                    case 5:
                        with open('config/config.json', 'w', encoding='utf-8') as file:
                            json.dump(LmStudioConfigExample, file, ensure_ascii=False, indent=4)

            continue

        # 选择是否强制思考
        match input['flag']:

            # 不强制思考
            case 'No':
                text_in = input['demand']

                # 第1阶段：选择图表类型
                messages1 = [{"role": "user", "content": prompt1a + text_in}]
                
                openai_out = client.chat.completions.create(model = llmmodel, messages = messages1).choices[0].message.content
                print(openai_out)
                type = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                messages1.append({"role": "assistant", "content": openai_out})

                match type["id"]:
                    # 线型图
                    case 0:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a0
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a0
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
                        fig = MatplotlibInterface.PlotInterface(data["x"], data["y"], data["ylabel"],
                                                                style["marker"], style["linestyle"], style["mcolor"], style["lcolor"],
                                                                range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                label["xlabel"], label["ylabel"], label["title"])
                    
                    # 散点图
                    case 1:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a1
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a1
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
                        fig = MatplotlibInterface.ScatterInterface(data["x"], data["y"],
                                                                   style["mcolor"], style["msize"], style["malpha"],
                                                                   range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                   label["xlabel"], label["ylabel"], label["title"])
                    
                    # 条形图
                    case 2:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a2
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a2
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
                        fig = MatplotlibInterface.BarInterface(data["x"], data["y"], data["ylabel"],
                                                               style["bcolor"], style["hatch"],
                                                               range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                               label["xlabel"], label["ylabel"], label["title"])

                    # 茎叶图
                    case 3:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a3
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a3
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
                        fig = MatplotlibInterface.StemInterface(data["x"], data["y"], data["ylabel"],
                                                                style["marker"], style["linelinestyle"], style["baselinestyle"], style["mcolor"], style["lcolor"], style["bcolor"],
                                                                range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                label["xlabel"], label["ylabel"], label["title"])

                    # 填充区域图
                    case 4:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a4
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a4
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
                        fig = MatplotlibInterface.FillBetweenInterface(data["x"], data["y1"], data["y2"], data["ylabel"],
                                                                       style["fcolor"], style["falpha"],
                                                                       range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                       label["title"], label["xlabel"], label["ylabel"])

                    # 堆叠区域图
                    case 5:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2a5
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3a5
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
                        fig = MatplotlibInterface.StackplotInterface(data["x"], data["y"], data["ylabel"],
                                                                     style["fcolor"], style["falpha"],
                                                                     range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                     label["title"], label["xlabel"], label["ylabel"])

                    # 阶梯图
                    case 6:
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

                # 组装数据
                config_now = style | range | label
                message_new = [{"role": "user", "content": prompt3.split("### 用户需求:")[0]},
                               {"role": "user", "content": prompt4a.split("### 用户需求:")[0]},
                               {"role": "user", "content": prompt5a.split("### 用户需求:")[0]},
                               {"role": "user", "content": "### 用户需求:\n"+text_in}]

                img_stream = io.BytesIO()
                fig.savefig(img_stream, format='png')
                img_stream.seek(0)
                put_text("Preview image:")
                put_image(img_stream.read())
                
                # 继续修改
                while True:
                    next = input_group(
                        "Continuing modifications",
                        [
                            textarea("Please describe the request you are modifying:", rows = 5, placeholder="Your request", name="demand"),
                            actions(buttons=[{'label': 'Edit the format', 'value': 1},
                                             {'label': 'Edit the data', 'value': 2},
                                             {'label': 'Show the figure', 'value': 0},
                                             {'label': "Reconstruct", 'value': -1, 'color': 'warning'}
                                             ], name="act")
                        ]
                    )

                    match next['act']:
                        case -1:
                            fig.close()
                            clear()
                            break

                        case 0:
                            fig.show()
                        
                        case 1:
                            fig.close()

                            prompt_new = prompt_newa1.format(next['demand'], config_now)

                            openai_out = client.chat.completions.create(model = llmmodel, messages = message_new + [{"role": "user", "content": prompt_new}]).choices[0].message.content
                            print(openai_out)
                            config_now = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        case 2:
                            fig.close()

                            prompt_new = prompt_newa2.format(next['demand'], data)

                            openai_out = client.chat.completions.create(model = llmmodel, messages = [{"role": "user", "content": prompt_new}]).choices[0].message.content
                            print(openai_out)
                            data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")



                    match type["id"]:
                        case 0:
                            fig = MatplotlibInterface.PlotInterface(data["x"], data["y"], data["ylabel"],
                                                                    config_now["marker"], config_now["linestyle"], config_now["mcolor"], config_now["lcolor"],
                                                                    config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                    config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 1:
                            fig = MatplotlibInterface.ScatterInterface(data["x"], data["y"],
                                                                       config_now["mcolor"], config_now["msize"], config_now["malpha"],
                                                                       config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                       config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 2:
                            fig = MatplotlibInterface.BarInterface(data["x"], data["y"], data["ylabel"],
                                                                   config_now["bcolor"], config_now["hatch"],
                                                                   config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                   config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 3:
                            fig = MatplotlibInterface.StemInterface(data["x"], data["y"], data["ylabel"],
                                                                    config_now["marker"], config_now["linelinestyle"], config_now["baselinestyle"], config_now["mcolor"], config_now["lcolor"], config_now["bcolor"],
                                                                    config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                    config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 4:
                            fig = MatplotlibInterface.FillBetweenInterface(data["x"], data["y1"], data["y2"], data["ylabel"],
                                                                           config_now["fcolor"], config_now["falpha"],
                                                                           config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                           config_now["title"], config_now["xlabel"], config_now["ylabel"])
                        
                        case 5:
                            fig = MatplotlibInterface.StackplotInterface(data["x"], data["y"], data["ylabel"],
                                                                         config_now["fcolor"], config_now["falpha"],
                                                                         config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                         config_now["title"], config_now["xlabel"], config_now["ylabel"])
                        
                        case 6:
                            fig = MatplotlibInterface.StairsInterface(data["value"], data["position"], data["label"],
                                                                      config_now["color"],
                                                                      config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                      config_now["title"], config_now["xlabel"], config_now["ylabel"])
                            
                    img_stream = io.BytesIO()
                    fig.savefig(img_stream, format='png')
                    img_stream.seek(0)
                    clear()
                    put_text("Preview image:")
                    put_image(img_stream.read())

            # 强制思考
            case 'Yes':
                text_in = input['demand']

                # 第1阶段：选择图表类型
                messages1 = [{"role": "user", "content": prompt1b + text_in}]

                openai_out = client.chat.completions.create(model = llmmodel, messages = messages1).choices[0].message.content
                print(openai_out)
                type = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                messages1.append({"role": "assistant", "content": openai_out})

                match type["id"]:
                    # 线型图
                    case 0:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b0
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b0
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.PlotInterface(data["x"], data["y"], data["ylabel"],
                                                                style["marker"], style["linestyle"], style["mcolor"], style["lcolor"],
                                                                range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                label["xlabel"], label["ylabel"], label["title"])
                    
                    # 散点图
                    case 1:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b1
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b1
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.ScatterInterface(data["x"], data["y"],
                                                                   style["mcolor"], style["msize"], style["malpha"],
                                                                   range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                   label["xlabel"], label["ylabel"], label["title"])

                    # 条形图
                    case 2:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b2
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b2
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.BarInterface(data["x"], data["y"], data["ylabel"],
                                                               style["bcolor"], style["hatch"],
                                                               range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                               label["xlabel"], label["ylabel"], label["title"])

                    # 茎叶图
                    case 3:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b3
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b3
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.StemInterface(data["x"], data["y"], data["ylabel"],
                                                                style["marker"], style["linelinestyle"], style["baselinestyle"], style["mcolor"], style["lcolor"], style["bcolor"],
                                                                range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                label["xlabel"], label["ylabel"], label["title"])

                    # 填充区域图
                    case 4:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b4
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b4
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.FillBetweenInterface(data["x"], data["y1"], data["y2"], data["ylabel"],
                                                                       style["fcolor"], style["falpha"],
                                                                       range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                       label["title"], label["xlabel"], label["ylabel"])

                    # 堆叠区域图
                    case 5:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b5
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b5
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.StackplotInterface(data["x"], data["y"], data["ylabel"],
                                                                     style["fcolor"], style["falpha"],
                                                                     range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                     label["title"], label["xlabel"], label["ylabel"])

                    # 阶梯图
                    case 6:
                        # 第2阶段：提取数据与数据标签
                        prompt2 = prompt2b6
                        messages2 = [{"role": "user", "content": prompt2 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages2).choices[0].message.content
                        print(openai_out)
                        data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        messages2.append({"role": "assistant", "content": openai_out})

                        # 第3阶段：设计图表样式
                        prompt3 = prompt3b6
                        messages3 = messages2 + [{"role": "user", "content": prompt3 + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages3).choices[0].message.content
                        print(openai_out)
                        style = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第4阶段：设计图表刻度与范围
                        messages4 = messages2 + [{"role": "user", "content": prompt4b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages4).choices[0].message.content
                        print(openai_out)
                        range = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        # 第5阶段：设计图表标签
                        messages5 = messages2 + [{"role": "user", "content": prompt5b + text_in}]

                        openai_out = client.chat.completions.create(model = llmmodel, messages = messages5).choices[0].message.content
                        print(openai_out)
                        label = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")

                        # 作图
                        fig = MatplotlibInterface.StairsInterface(data["value"], data["position"], data["label"],
                                                                  style["color"],
                                                                  range["xmin"], range["xmax"], range["xstep"], range["ymin"], range["ymax"], range["ystep"],
                                                                  label["title"], label["xlabel"], label["ylabel"])
                        
                # 组装数据
                config_now = style | range | label
                message_new = [{"role": "user", "content": prompt3.split("### 用户需求:")[0]},
                               {"role": "user", "content": prompt4b.split("### 用户需求:")[0]},
                               {"role": "user", "content": prompt5b.split("### 用户需求:")[0]},
                               {"role": "user", "content": "### 用户需求:\n"+text_in}]

                img_stream = io.BytesIO()
                fig.savefig(img_stream, format='png')
                img_stream.seek(0)
                put_text("Preview image:")
                put_image(img_stream.read())
                
                # 继续修改
                while True:
                    next = input_group(
                        "Continuing modifications",
                        [
                            textarea("Please describe the request you are modifying:", rows = 5, placeholder="请描述您的要求：", name="demand"),
                            actions(buttons=[{'label': 'Edit the format', 'value': 1},
                                             {'label': 'Edit the data', 'value': 2},
                                             {'label': 'Show the figure', 'value': 0},
                                             {'label': "Reconstruct", 'value': -1, 'color': 'warning'}
                                             ], name="act")
                        ]
                    )

                    match next['act']:
                        case -1:
                            fig.close()
                            clear()
                            break

                        case 0:
                            fig.show()
                        
                        case 1:
                            fig.close()

                            prompt_new = prompt_newb1.format(next['demand'], config_now)

                            openai_out = client.chat.completions.create(model = llmmodel, messages = message_new + [{"role": "user", "content": prompt_new}]).choices[0].message.content
                            print(openai_out)
                            config_now = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                        
                        case 2:
                            fig.close()

                            prompt_new = prompt_newb2.format(next['demand'], data)

                            openai_out = client.chat.completions.create(model = llmmodel, messages = [{"role": "user", "content": prompt_new}]).choices[0].message.content
                            print(openai_out)
                            data = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")



                    match type["id"]:
                        case 0:
                            fig = MatplotlibInterface.PlotInterface(data["x"], data["y"], data["ylabel"],
                                                                    config_now["marker"], config_now["linestyle"], config_now["mcolor"], config_now["lcolor"],
                                                                    config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                    config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 1:
                            fig = MatplotlibInterface.ScatterInterface(data["x"], data["y"],
                                                                       config_now["mcolor"], config_now["msize"], config_now["malpha"],
                                                                       config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                       config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 2:
                            fig = MatplotlibInterface.BarInterface(data["x"], data["y"], data["ylabel"],
                                                                   config_now["bcolor"], config_now["hatch"],
                                                                   config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                   config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 3:
                            fig = MatplotlibInterface.StemInterface(data["x"], data["y"], data["ylabel"],
                                                                    config_now["marker"], config_now["linelinestyle"], config_now["baselinestyle"], config_now["mcolor"], config_now["lcolor"], config_now["bcolor"],
                                                                    config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                    config_now["xlabel"], config_now["ylabel"], config_now["title"])
                        
                        case 4:
                            fig = MatplotlibInterface.FillBetweenInterface(data["x"], data["y1"], data["y2"], data["ylabel"],
                                                                           config_now["fcolor"], config_now["falpha"],
                                                                           config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                           config_now["title"], config_now["xlabel"], config_now["ylabel"])
                        
                        case 5:
                            fig = MatplotlibInterface.StackplotInterface(data["x"], data["y"], data["ylabel"],
                                                                         config_now["fcolor"], config_now["falpha"],
                                                                         config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                         config_now["title"], config_now["xlabel"], config_now["ylabel"])
                        
                        case 6:
                            fig = MatplotlibInterface.StairsInterface(data["value"], data["position"], data["label"],
                                                                      config_now["color"],
                                                                      config_now["xmin"], config_now["xmax"], config_now["xstep"], config_now["ymin"], config_now["ymax"], config_now["ystep"],
                                                                      config_now["title"], config_now["xlabel"], config_now["ylabel"])
                            
                    img_stream = io.BytesIO()
                    fig.savefig(img_stream, format='png')
                    img_stream.seek(0)
                    clear()
                    put_text("Preview image:")
                    put_image(img_stream.read())

