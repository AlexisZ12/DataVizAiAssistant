from openai import OpenAI, APIConnectionError, AuthenticationError, APIStatusError
from pywebio.input import *
from pywebio.output import *
import json
import function
import ui

def contains_gpt(my_list):
    for s in my_list:
        if isinstance(s, str) and "gpt" in s:
            return True
    return False

def CheckOpenAi(client):
    try:
        response = client.models.list()       
        if not response.data or len(response.data) == 0:
            toast("⚠️ Service test failed", color='warning')
            return False, []
        model_ids = [model.id for model in response.data]
        toast(f"✅ Service connected successfully")
        return True, model_ids
        
    except AuthenticationError:
        toast("⛔ API key invalid", color='error')
        return False, []
    except APIConnectionError as e:
        toast("🌐 Network connection failed", color='error')
        return False, []
    except APIStatusError as e:
        toast("🚨 Service exception", color='error')
        return False, []
    except Exception as e:
        toast("🔥 Unknown error", color='error')
        return False, []

def main():
    ui.MainUI()
    
    with open('config/config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        
    key = config['key']
    url = config['base']
    
    while True:
        setting = input_group("config",
                            [
                                input("API Key", name='key', value=config['key'], type='password'),
                                input("Base URL", name='base', value=config['base']),
                                actions("", [{'label': 'OpenAi Standard Format', 'value': 1},
                                             {'label': 'DeepSeek Standard Format', 'value': 2},
                                             {'label': 'Kimi Standard Format', 'value': 3},
                                             {'label': 'Check', 'value': 0, 'color': 'warning'}], name="act")
                            ])

        match setting['act']:
            case 1:
                config['base'] = "https://api.openai.com/v1"
                continue
            case 2:
                config['base'] = "https://api.deepseek.com"
                continue
            case 3:
                config['base'] = "https://api.moonshot.cn/v1"
                continue
            case 0:
                client = OpenAI(api_key=setting['key'], base_url=setting['base'])
                config = {
                    'key': setting['key'],
                    'base': setting['base']
                }
                with open('config/config.json', 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=4, ensure_ascii=False)
                state, modellist = CheckOpenAi(client)
                if state:
                    break
                continue
    
    if contains_gpt(modellist):
        modellist = list(set(modellist) & set(["gpt-4", "gpt-4-turbo", "gpt-4o", "gpt-4o-mini", "o1-preview", "o1-mini"]))
    
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
    main()