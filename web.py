from openai import OpenAI, APIConnectionError, AuthenticationError, APIStatusError
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import re
import function

def CheckOpenAi(client):
    try:
        response = client.models.list()       
        if not response.data or len(response.data) == 0:
            toast("⚠️ OpenAi服务测试失败", color='warning')
            return False, []
        model_ids = [model.id for model in response.data]
        toast(f"✅ OpenAi服务连接成功")
        return True, model_ids
        
    except AuthenticationError:
        toast("⛔ OpenAi API密钥无效", color='error')
        return False, []
    except APIConnectionError as e:
        toast("🌐 OpenAi网络连接失败", color='error')
        return False, []
    except APIStatusError as e:
        toast("🚨 OpenAi服务异常", color='error')
        return False, []
    except Exception as e:
        toast("🔥 OpenAi未知错误", color='error')
        return False, []

def main():
    url = "https://api.openai.com/v1"
    
    while True:
        setting = input_group("config",
                            [
                                input("API Key", name='key'),
                                input("Base URL", name='base', value=url),
                                actions("", [{'label': 'OpenAi Standard Format', 'value': 1},
                                             {'label': 'DeepSeek Standard Format', 'value': 2},
                                             {'label': 'Check', 'value': 0, 'color': 'warning'}], name="act")
                            ])

        match setting['act']:
            case 1:
                url = "https://api.openai.com/v1"
                continue
            case 2:
                url = "https://api.deepseek.com"
                continue
            case 0:
                client = OpenAI(api_key=setting['key'], base_url=setting['base'])
                state, modellist = CheckOpenAi(client)
                if state:
                    break
                continue
    
    modellist = [model for model in modellist if model.startswith('gpt-') and not re.search(r'-\d+$', model)]
    
    while True:
        inputs = input_group(
            "AI visualisation data analysis",
            [
                textarea("Please describe what you want to analyse:", rows = 15, placeholder="Elements analysed", name="demand", required=True),
                select("Which model to be used for analysis:", options=modellist, name="model", required=True),
                radio("Whether or not it forces thinking:", options=["Yes", "No"], value="No", name="flag"),
                actions(buttons=[{'label': 'Make the Figure', 'value': 0}], name="act")
            ]
        )
        
        function.analyze(inputs['demand'], inputs['flag'], client, inputs['model'])
    
if __name__ == '__main__':
    start_server(main, port=8080)