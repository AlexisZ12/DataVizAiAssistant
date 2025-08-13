from pywebio.output import *
from pywebio.input import *

def MainUI():
    put_markdown("""
# 🚀 AI 数据可视化分析平台

## 🌟 项目简介
**DataVizAiAssistant** 是一个利用大型语言模型进行智能数据分析和可视化展示的工具。只需简单描述你的分析需求，AI将自动完成数据处理、分析并生成专业的图表结果。
- 📂 **GitHub项目仓库**: [AlexisZ12/DataVizAiAssistant](https://github.com/AlexisZ12/DataVizAiAssistant)
- 📂 **爱发电项目仓库**: [DataVizAiAssistant](https://afdian.com/album/9049811c77e711f085b352540025c377)
- ⭐ **欢迎Star**: 如果喜欢这个项目，请在GitHub上点个Star支持我们
- ✉️ **联系邮箱**: 2242809239@qq.com
- 💬 **微信**: `Alexis_12_Z`
- 💖 **爱发电**: [AlexisZ12](https://afdian.com/a/AlexisZ12)

## ✨ 核心功能
- 🧠 自然语言驱动的数据分析
- 📊 一键式图表生成（折线图/柱状图/散点图/饼图等）
- 🤖 支持多款顶尖AI模型（GPT系列/DeepSeek/Kimi等）
- 🔄 交互式数据处理流程
- 📈 专业级数据可视化输出

## 🔑 开始使用
1. 在下方输入您的 **API Key**
2. 选择服务提供商或使用默认设置
3. 点击"Check"验证连接
4. 开始您的数据分析之旅！

<div style="background-color: #e6f7ff; padding: 15px; border-radius: 10px; margin: 20px 0;">
⚠️ 安全提示  
您的API Key仅用于本次会话，不会被存储或上传至任何服务器。请妥善保管您的密钥，避免泄露。
</div>

""")
    actions(buttons=[{'label': '🚀 开始', 'value': 0}])
    clear()