from openai import OpenAI, APIConnectionError, AuthenticationError, APIStatusError
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import matplotlib
import function
import ui
import os
from dotenv import load_dotenv

def CheckOpenAi(client):
    try:
        response = client.models.list()
        if not response.data or len(response.data) == 0:
            toast("⚠️ Service test failed", color='warning')
            return False

        toast(f"✅ Service connected successfully")
        return True

    except AuthenticationError:
        toast("⛔ API key invalid", color='error')
        return False
    except APIConnectionError as e:
        toast("🌐 Network connection failed", color='error')
        return False
    except APIStatusError as e:
        toast("🚨 Service exception", color='error')
        return False
    except Exception as e:
        toast("🔥 Unknown error", color='error')
        return False

def main():
    # 加载 .env 文件
    load_dotenv()

    # 从环境变量读取配置
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model = os.getenv("MODEL")

    # 检查配置是否存在
    if not api_key or not base_url or not model:
        toast("❌ Missing configuration in .env file", color='error')
        return

    ui.MainUI_preset()

    matplotlib.use('Agg')

    # 创建客户端
    client = OpenAI(api_key=api_key, base_url=base_url)

    # 检查连接
    if not CheckOpenAi(client):
        return

    while True:
        inputs = input_group(
            "AI visualisation data analysis",
            [
                textarea("Please describe what you want to analyse:", rows=15, placeholder="Elements analysed", name="demand", required=True),
                actions(buttons=[{'label': 'Make the Figure', 'value': 0}], name="act")
            ]
        )

        # 强制关闭思考功能，使用 .env 中的模型
        function.analyze(inputs['demand'], "No", client, model)

if __name__ == '__main__':
    start_server(main, port=8080)
