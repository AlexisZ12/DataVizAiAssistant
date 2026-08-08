<div align="center">

# DataVizAiAssistant

**AI驱动的数据可视化助手** — 基于大语言模型的智能图表生成工具，让数据可视化变得触手可及。无需编程基础，只需用自然语言描述您的数据和分析需求，即可自动生成专业的 Matplotlib 可视化图表。支持线图、散点图、条形图等7种图表类型，并具备交互式修改、思考模式、多平台 API 兼容等高级功能，是数据分析、报告生成、学术研究的得力助手。同时提供 CLI Skill，可集成到 OpenClaw、QwenPaw、Claude Code 等 AI 编程助手中使用。

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-teal.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB.svg)](https://react.dev/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)](https://matplotlib.org/)

[中文](README.md) | [English](README_EN.md)

</div>

---

## 📖 项目简介

**DataVizAiAssistant** 是一个创新的开源工具，结合人工智能技术与数据可视化功能，帮助用户轻松从自然语言描述生成专业的数据可视化图表。项目使用大语言模型（通过 OpenAI 或兼容接口）解析用户需求，自动生成 Matplotlib 可视化图表，并支持对数据和样式的二次修改。

项目采用**前后端分离**架构：

| 模块 | 技术 | 说明 |
|------|------|------|
| **frontend/** | React + Vite | Web 界面（中文，蓝白主题） |
| **backend/** | FastAPI | HTTP API，提供作图 / 编辑数据 / 编辑样式 三个接口 |
| **workflow/** | Python | 图表生成引擎（多阶段 LLM 流水线 + Matplotlib 渲染） |
| **skills/** | Python | CLI Skill，可作为 AI 助手插件使用 |

---

## 🚀 在线体验

> **在线演示**：http://118.25.26.232:5173/  
> **介绍视频**：https://www.bilibili.com/video/BV1tqYhzNEbx/

---

## ✨ 核心功能

<table>
  <tr>
    <td align="center" width="33%">
      <h3>📊 智能图表生成</h3>
      <p>从自然语言描述自动创建7种专业图表类型，支持线图、散点图、条形图等，自动处理数据提取、图表样式、坐标刻度和标签</p>
    </td>
    <td align="center" width="33%">
      <h3>🔄 交互式修改</h3>
      <p>图表实时预览功能，支持数据与样式的二次修改，无需重新生成即可迭代优化</p>
    </td>
    <td align="center" width="33%">
      <h3>🌐 多平台兼容</h3>
      <p>支持OpenAI标准API，兼容DeepSeek、Ollama、LmStudio等替代平台，配置文件管理接口切换</p>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <h3>🧠 思考模式</h3>
      <p>强制思考模式（深度推理）与快速执行模式（简化流程）自由切换</p>
    </td>
    <td align="center" width="33%">
      <h3>🏗️ 前后端分离</h3>
      <p>React 前端 + FastAPI 后端 + 独立图表引擎，支持局域网访问与端口隔离</p>
    </td>
    <td align="center" width="33%">
      <h3>🔒 安全可靠</h3>
      <p>API密钥本地存储，数据不上传第三方服务器，保护用户隐私</p>
    </td>
  </tr>
</table>

---

## 🛠️ 技术栈

| 类别 | 技术 |
|------|------|
| **前端** | React 18 + Vite |
| **后端** | FastAPI + Uvicorn |
| **图表引擎** | Python + Matplotlib |
| **AI SDK** | OpenAI Python SDK |

---

## 🧪 本地测试

适合在本机开发或快速体验。

### 环境要求

- Python 3.10+
- Node.js 18+（前端）

### 1. 克隆项目

```bash
git clone https://github.com/AlexisZ12/DataVizAiAssistant.git
cd DataVizAiAssistant
```

### 2. 配置 API 密钥

在项目根目录创建 `.env`：

```bash
cp .env.example .env
```

编辑 `.env` 填入你的 LLM 配置：

```env
API_KEY=your-api-key-here
BASE_URL=https://api.openai.com/v1
MODEL=gpt-4o
```

> 也可以不填 `.env`，在前端「高级设置」里临时输入 API Key / Base URL / 模型。

### 3. 安装依赖

```bash
# Python 依赖（后端 + 图表引擎）
pip install -r backend/requirements.txt

# 前端依赖
cd frontend && npm install && cd ..
```

### 4. 启动后端

```bash
python3 -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

### 5. 启动前端

新开一个终端：

```bash
cd frontend
npm run dev
```

### 6. 访问

浏览器打开 http://localhost:5173，输入需求描述即可生成图表。

---

## 🚀 服务器部署

适合把服务部署到局域网或公网服务器，供他人访问。

架构特点：**前端对局域网开放，后端只监听本机回环地址**。局域网用户通过前端访问服务，但无法直接调用后端 API 端口。

### 1. 安装依赖（同上）

```bash
pip install -r backend/requirements.txt
cd frontend && npm install && cd ..
```

### 2. 配置 `.env`（同上）

### 3. 启动后端（绑定本机，不对外暴露）

```bash
cd DataVizAiAssistant
setsid nohup python3 -m uvicorn backend.app.main:app \
  --host 127.0.0.1 --port 8000 \
  > /tmp/dataviz_backend.log 2>&1 < /dev/null &
```

### 4. 构建并启动前端

```bash
cd DataVizAiAssistant/frontend
npm run build            # 生成静态文件到 dist/
setsid nohup npm run preview > /tmp/dataviz_frontend.log 2>&1 < /dev/null &
```

> `preview` 会把 `/api` 请求转发给本机 `127.0.0.1:8000` 的后端。代码更新后需重新 `npm run build`。

### 5. 放行前端端口（只放 5173，不放后端 8000）

```bash
# ufw（Ubuntu/Debian）
sudo ufw allow 5173/tcp

# firewalld（CentOS/RHEL）
sudo firewall-cmd --permanent --add-port=5173/tcp && sudo firewall-cmd --reload
```

> 云服务器（阿里云/腾讯云/AWS）还需在**安全组**里放行 5173。后端 8000 绑的是本机回环地址，无需也不应放行。

### 6. 验证

```bash
# 后端健康检查
curl http://127.0.0.1:8000/api/health      # {"status":"ok"}

# 前端 + 代理
curl http://127.0.0.1:5173/api/health      # {"status":"ok"}
```

浏览器访问 http://服务器IP:5173。

### 日志与停止

```bash
tail -f /tmp/dataviz_backend.log     # 后端日志
tail -f /tmp/dataviz_frontend.log    # 前端日志

# 停止
pkill -f "uvicorn backend.app.main" 2>/dev/null
pkill -f "vite preview" 2>/dev/null
```

> **长期运行建议**：用 `systemd` 将前后端注册成服务，实现开机自启和崩溃自动拉起。

---

## 🔌 Skill / CLI 模式

将图表生成能力作为命令行工具或 AI 编程助手 Skill 使用，无 Web UI 依赖，输出为 PNG 文件。

### 安装

```bash
# 1. 安装 Python 依赖
pip install openai matplotlib numpy

# 2. 将技能安装到对应平台

# Claude Code
cp -r skills/dataviz-ai ~/.claude/skills/dataviz-ai

# OpenClaw
cp -r skills/dataviz-ai ~/.openclaw/skills/dataviz-ai

# QwenPaw
cp -r skills/dataviz-ai ~/.copaw/skill_pool/dataviz-ai
```

安装完成后，在对应平台对话中直接调用 `/dataviz-ai` 即可使用。

### 基本用法

**方式一：安装为平台技能（推荐）**

在对应平台对话中直接使用：

```
/dataviz-ai "画出2024年各月销售额趋势，1月100,2月200,3月150"
/dataviz-ai "画出上海和北京各季度GDP对比" -o ./chart.png
```

**方式二：直接运行脚本（测试/调试用途）**

```bash
# 进入脚本目录
cd skills/dataviz-ai/scripts

# 设置环境变量
export DATAVIZ_AI_API_KEY="sk-your-api-key"
export DATAVIZ_AI_BASE_URL="https://api.openai.com/v1"
export DATAVIZ_AI_MODEL="gpt-4o"

# 生成图表
python dataviz_ai.py "画出2024年各月销售额趋势，1月100,2月200,3月150"
# 输出: /tmp/dataviz_xxxxx.png

# 指定输出路径
python dataviz_ai.py "画出上海和北京各季度GDP对比" -o ./chart.png
```

### 参数说明

| 参数 | 必需 | 说明 |
|------|:----:|------|
| `description` | 是 | 位置参数，自然语言描述要生成的图表 |
| `-o`, `--output` | 否 | 输出图片路径，不指定则保存到临时目录 |

### 环境变量

| 变量 | 必需 | 说明 |
|------|:----:|------|
| `DATAVIZ_AI_API_KEY` | 是 | LLM API 密钥 |
| `DATAVIZ_AI_BASE_URL` | 是 | API 基础 URL |
| `DATAVIZ_AI_MODEL` | 是 | 模型名称 |

详见 [skills/README.md](skills/README.md)。

---

## 🖼️ 支持的图表类型

| 图表类型 | 适用场景 | 预览 |
|:--------:|:--------:|:----:|
| 线图 | 时间序列、趋势分析 | <img src="pic/plot.png" height="120"> |
| 散点图 | 相关性分析、分布模式 | <img src="pic/scatter.png" height="120"> |
| 条形图 | 分类数据比较 | <img src="pic/bar.png" height="120"> |
| 茎叶图 | 点值分布 | <img src="pic/stem.png" height="120"> |
| 填充图 | 范围可视化 | <img src="pic/fill_between.png" height="120"> |
| 堆叠图 | 比例构成分析 | <img src="pic/stackplot.png" height="120"> |
| 阶梯图 | 离散数值变化 | <img src="pic/stairs.png" height="120"> |

---

## 🧭 使用示例

### 示例 1：全球太阳能发电数据

**输入描述：**

> 2025年，全球太阳能发电行业经历了快速增长。根据国际可再生能源署（IRENA）的报告，全球五大太阳能发电国的装机容量在过去一年内都有显著增长。以下是这些国家的新增装机容量和占全球市场的比例。  
> 关键数据：  
> 中国：新增装机容量 50 GW，占全球市场的 25%  
> 美国：新增装机容量 30 GW，占全球市场的 15%  
> 印度：新增装机容量 20 GW，占全球市场的 10%  
> 德国：新增装机容量 12 GW，占全球市场的 6%  
> 日本：新增装机容量 8 GW，占全球市场的 4%

**生成结果：**

<img src="pic/example1.png" height="280">

---

### 示例 2：股票走势分析

**输入描述：**

> From the 1st to the 7th of this month, the stock of TechGen Inc. (TGI) showed some fluctuations. On the 1st, the stock opened at $152.45 and closed at $158.72. The next day, it saw a slight dip, opening at $157.20 and finishing at $155.35. On the 3rd, it bounced back, opening at $156.10 and closing at $160.55. The 4th saw a more significant drop, starting at $159.00 and ending at $152.85. Afterward, the stock demonstrated a steady recovery with an opening price of $153.50 on the 5th, closing at $157.90. On the 6th, it slightly rose again, opening at $158.00 and closing at $161.25. Finally, on the 7th, TechGen Inc. saw its highest price of the week, opening at $162.00 and closing at $163.80, ending the week on a positive note.

**生成结果：**

<img src="pic/example2.png" height="280">

---

## 🛑 注意事项

- 需要有效的LLM API密钥（OpenAI或兼容服务）
- 使用"强制思考"模式，API将消耗更多tokens
- 图表质量取决于LLM对自然语言的理解准确性
- 大数据集建议预处理后再输入

---

## 🤝 支持与联系

| 渠道 | 链接 |
|:----:|:-----|
| 📂 **GitHub** | [AlexisZ12/DataVizAiAssistant](https://github.com/AlexisZ12/DataVizAiAssistant) |
| 🎁 **爱发电** | [AlexisZ12](https://afdian.com/a/AlexisZ12) |
| 📧 **邮箱** | 2242809239@qq.com |
| 💬 **微信** | `Alexis_12_Z` |

---

<div align="center">

**如果觉得这个项目有帮助，欢迎 ⭐ Star 支持一下！**

</div>
