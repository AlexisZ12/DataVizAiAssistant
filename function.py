from pywebio.input import *
from pywebio.output import *
import MatplotlibInterface
import json
import io
import plot
import scatter
import bar
import stem
import fillbetween
import stackplot
import stairs

with open('config/configExample.json', 'r', encoding = 'utf-8') as jsExample:
    jsEx = json.load(jsExample)
OpenAiConfigExample = jsEx['OpenAiConfigExample']
DeepSeekConfigExample = jsEx['DeepSeekConfigExample']
OllamaConfigExample = jsEx['OllamaConfigExample']
LmStudioConfigExample = jsEx['LmStudioConfigExample']

def analyze(text_in, flag, client, llmmodel):
    match flag:
        # 不强制思考
        case 'No':
            # 第1阶段：选择图表类型
            with open('prompt/a/prompt1a.txt', 'r', encoding='utf-8') as file:
                prompt1a = file.read()
            messages1 = [{"role": "user", "content": prompt1a + text_in}]
            
            openai_out = client.chat.completions.create(model = llmmodel, messages = messages1).choices[0].message.content
            print(openai_out)
            type = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
            messages1.append({"role": "assistant", "content": openai_out})

            with open('prompt/a/prompt4a.txt', 'r', encoding='utf-8') as file:
                prompt4a = file.read()
            with open('prompt/a/prompt5a.txt', 'r', encoding='utf-8') as file:
                prompt5a = file.read()
                
            match type["id"]:
                # 线型图
                case 0:
                    with open('prompt/a/prompt2a0.txt', 'r', encoding='utf-8') as file:
                        prompt2a0 = file.read()
                    with open('prompt/a/prompt3a0.txt', 'r', encoding='utf-8') as file:
                        prompt3a0 = file.read()
                    fig, style, range, label = plot.plot(text_in, client, llmmodel, prompt2a0, prompt3a0, prompt4a, prompt5a)
                    prompt3 = prompt3a0
                    
                # 散点图
                case 1:
                    with open('prompt/a/prompt2a1.txt', 'r', encoding='utf-8') as file:
                        prompt2a1 = file.read()
                    with open('prompt/a/prompt3a1.txt', 'r', encoding='utf-8') as file:
                        prompt3a1 = file.read()
                    fig, style, range, label = scatter.scatter(text_in, client, llmmodel, prompt2a1, prompt3a1, prompt4a, prompt5a)
                    prompt3 = prompt3a1
                    
                # 条形图
                case 2:
                    with open('prompt/a/prompt2a2.txt', 'r', encoding='utf-8') as file:
                        prompt2a2 = file.read()
                    with open('prompt/a/prompt3a2.txt', 'r', encoding='utf-8') as file:
                        prompt3a2 = file.read()
                    fig, style, range, label = bar.bar(text_in, client, llmmodel, prompt2a2, prompt3a2, prompt4a, prompt5a)
                    prompt3 = prompt3a2
                    
                # 茎叶图
                case 3:
                    with open('prompt/a/prompt2a3.txt', 'r', encoding='utf-8') as file:
                        prompt2a3 = file.read()
                    with open('prompt/a/prompt3a3.txt', 'r', encoding='utf-8') as file:
                        prompt3a3 = file.read()
                    fig, style, range, label = stem.stem(text_in, client, llmmodel, prompt2a3, prompt3a3, prompt4a, prompt5a)
                    prompt3 = prompt3a3
                    
                # 填充区域图
                case 4:
                    with open('prompt/a/prompt2a4.txt', 'r', encoding='utf-8') as file:
                        prompt2a4 = file.read()
                    with open('prompt/a/prompt3a4.txt', 'r', encoding='utf-8') as file:
                        prompt3a4 = file.read()
                    fig, style, range, label = fillbetween.fillbetween(text_in, client, llmmodel, prompt2a4, prompt3a4, prompt4a, prompt5a)
                    prompt3 = prompt3a4
                
                # 堆叠区域图
                case 5:
                    with open('prompt/a/prompt2a5.txt', 'r', encoding='utf-8') as file:
                        prompt2a5 = file.read()
                    with open('prompt/a/prompt3a5.txt', 'r', encoding='utf-8') as file:
                        prompt3a5 = file.read()
                    fig, style, range, label = stackplot.stackplot(text_in, client, llmmodel, prompt2a5, prompt3a5, prompt4a, prompt5a)
                    prompt3 = prompt3a5
                
                # 阶梯图
                case 6:
                    with open('prompt/a/prompt2a6.txt', 'r', encoding='utf-8') as file:
                        prompt2a6 = file.read()
                    with open('prompt/a/prompt3a6.txt', 'r', encoding='utf-8') as file:
                        prompt3a6 = file.read()
                    fig, style, range, label = stairs.stairs(text_in, client, llmmodel, prompt2a6, prompt3a6, prompt4a, prompt5a)
                    prompt3 = prompt3a6
            
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
                        actions(buttons=[{'label': 'Edit the Format', 'value': 1},
                                            {'label': 'Edit the Data', 'value': 2},
                                            {'label': 'Show the Figure', 'value': 0},
                                            {'label': "Reconstruct", 'value': -1, 'color': 'warning'}
                                            ], name="act")
                    ]
                )

                match next['act']:
                    case -1:
                        fig.close()
                        clear()
                        return

                    case 0:
                        fig.show()
                    
                    case 1:
                        fig.close()
                        
                        with open('prompt/a/prompt_newa1.txt', 'r', encoding='utf-8') as file:
                            prompt_newa1 = file.read()
                        prompt_new = prompt_newa1.format(next['demand'], config_now)

                        openai_out = client.chat.completions.create(model = llmmodel, messages = message_new + [{"role": "user", "content": prompt_new}]).choices[0].message.content
                        print(openai_out)
                        config_now = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                    
                    case 2:
                        fig.close()
                        
                        with open('prompt/a/prompt_newa2.txt', 'r', encoding='utf-8') as file:
                            prompt_newa2 = file.read()
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
            # 第1阶段：选择图表类型
            with open('prompt/b/prompt1b.txt', 'r', encoding='utf-8') as file:
                prompt1b = file.read()
            messages1 = [{"role": "user", "content": prompt1b + text_in}]

            openai_out = client.chat.completions.create(model = llmmodel, messages = messages1).choices[0].message.content
            print(openai_out)
            type = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
            messages1.append({"role": "assistant", "content": openai_out})

            with open('prompt/b/prompt4b.txt', 'r', encoding='utf-8') as file:
                prompt4b = file.read()
            with open('prompt/b/prompt5b.txt', 'r', encoding='utf-8') as file:
                prompt5b = file.read()

            match type["id"]:
                # 线型图
                case 0:
                    with open('prompt/b/prompt2b0.txt', 'r', encoding='utf-8') as file:
                        prompt2b0 = file.read()
                    with open('prompt/b/prompt3b0.txt', 'r', encoding='utf-8') as file:
                        prompt3b0 = file.read()   
                    
                    fig, style, range, label = plot.plot(text_in, client, llmmodel, prompt2b0, prompt3b0, prompt4b, prompt5b)
                    prompt3 = prompt3b0
                    
                # 散点图
                case 1:
                    with open('prompt/b/prompt2b1.txt', 'r', encoding='utf-8') as file:
                        prompt2b1 = file.read()
                    with open('prompt/b/prompt3b1.txt', 'r', encoding='utf-8') as file:
                        prompt3b1 = file.read()
                    
                    fig, style, range, label = scatter.scatter(text_in, client, llmmodel, prompt2b1, prompt3b1, prompt4b, prompt5b)
                    prompt3 = prompt3b1
                    
                # 条形图
                case 2:
                    with open('prompt/b/prompt2b2.txt', 'r', encoding='utf-8') as file:
                        prompt2b2 = file.read()
                    with open('prompt/b/prompt3b2.txt', 'r', encoding='utf-8') as file:
                        prompt3b2 = file.read()
                    
                    fig, style, range, label = bar.bar(text_in, client, llmmodel, prompt2b2, prompt3b2, prompt4b, prompt5b)
                    prompt3 = prompt3b2
                    
                # 茎叶图
                case 3:    
                    with open('prompt/b/prompt2b3.txt', 'r', encoding='utf-8') as file:
                        prompt2b3 = file.read()
                    with open('prompt/b/prompt3b3.txt', 'r', encoding='utf-8') as file:
                        prompt3b3 = file.read()
                    
                    fig, style, range, label = stem.stem(text_in, client, llmmodel, prompt2b3, prompt3b3, prompt4a, prompt5b)
                    prompt3 = prompt3b3
                    
                # 填充区域图
                case 4:    
                    with open('prompt/b/prompt2b4.txt', 'r', encoding='utf-8') as file:
                        prompt2b4 = file.read()
                    with open('prompt/b/prompt3b4.txt', 'r', encoding='utf-8') as file:
                        prompt3b4 = file.read()
                    
                    fig, style, range, label = fillbetween.fillbetween(text_in, client, llmmodel, prompt2b4, prompt3b4, prompt4b, prompt5b)
                    prompt3 = prompt3b4
                
                # 堆叠区域图
                case 5:    
                    with open('prompt/b/prompt2b5.txt', 'r', encoding='utf-8') as file:
                        prompt2b5 = file.read()
                    with open('prompt/b/prompt3b5.txt', 'r', encoding='utf-8') as file:
                        prompt3b5 = file.read()
                    
                    fig, style, range, label = stackplot.stackplot(text_in, client, llmmodel, prompt2b5, prompt3b5, prompt4b, prompt5b)
                    prompt3 = prompt3b5
                
                # 阶梯图
                case 6:    
                    with open('prompt/b/prompt2b6.txt', 'r', encoding='utf-8') as file:
                        prompt2b6 = file.read()
                    with open('prompt/b/prompt3b6.txt', 'r', encoding='utf-8') as file:
                        prompt3b6 = file.read()
                    fig, style, range, label = stairs.stairs(text_in, client, llmmodel, prompt2b6, prompt3b6, prompt4b, prompt5b)
                    prompt3 = prompt3b6
                    
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
                        actions(buttons=[{'label': 'Edit the Format', 'value': 1},
                                            {'label': 'Edit the Data', 'value': 2},
                                            {'label': 'Show the Figure', 'value': 0},
                                            {'label': "Reconstruct", 'value': -1, 'color': 'warning'}
                                            ], name="act")
                    ]
                )

                match next['act']:
                    case -1:
                        fig.close()
                        clear()
                        return

                    case 0:
                        fig.show()
                    
                    case 1:
                        fig.close()
                        
                        with open('prompt/b/prompt_newb1.txt', 'r', encoding='utf-8') as file:
                            prompt_newb1 = file.read()
                        prompt_new = prompt_newb1.format(next['demand'], config_now)

                        openai_out = client.chat.completions.create(model = llmmodel, messages = message_new + [{"role": "user", "content": prompt_new}]).choices[0].message.content
                        print(openai_out)
                        config_now = json.loads("{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}")
                    
                    case 2:
                        fig.close()
                        
                        with open('prompt/b/prompt_newb2.txt', 'r', encoding='utf-8') as file:
                            prompt_newb2 = file.read()
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
