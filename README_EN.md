<div align="center">

# DataVizAiAssistant

**AI-Powered Data Visualization Assistant**

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)](https://matplotlib.org/)
[![PyWebIO](https://img.shields.io/badge/PyWebIO-Web%20UI-purple.svg)](https://pywebio.readthedocs.io/)

[中文](README.md) | [English](README_EN.md)

</div>

---

## 📖 Overview

**DataVizAiAssistant** is an innovative open-source tool that combines AI technology with data visualization capabilities, enabling users to effortlessly generate professional charts from natural language descriptions. The project uses GPT models (via OpenAI API or compatible interfaces) to parse user requirements and automatically generate Matplotlib visualizations with interactive modification support.

---

## 🚀 Quick Start

> **Live Demo**: http://115.190.155.135:8080/  
> **Video Tutorial**: https://www.bilibili.com/video/BV1tqYhzNEbx/

---

## ✨ Key Features

<table>
  <tr>
    <td align="center" width="33%">
      <h3>📊 Intelligent Chart Generation</h3>
      <p>Automatically create 7 professional chart types from natural language descriptions. Supports line charts, scatter plots, bar charts, and more with automatic data extraction and styling.</p>
    </td>
    <td align="center" width="33%">
      <h3>🔄 Interactive Editing</h3>
      <p>Real-time chart preview with support for secondary modifications to data and styling. Iterate without regenerating from scratch.</p>
    </td>
    <td align="center" width="33%">
      <h3>🌐 Multi-Platform Support</h3>
      <p>Supports OpenAI standard API with compatibility for DeepSeek, Ollama, LmStudio, and other alternatives. Easy configuration switching.</p>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <h3>🧠 Thinking Modes</h3>
      <p>Switch between forced thinking mode (deep reasoning) and quick execution mode (simplified workflow).</p>
    </td>
    <td align="center" width="33%">
      <h3>☁️ Flexible Deployment</h3>
      <p>Local deployment (full features) or cloud deployment (optimized for servers).</p>
    </td>
    <td align="center" width="33%">
      <h3>🔒 Secure & Private</h3>
      <p>API keys stored locally, no data uploaded to third-party servers, protecting user privacy.</p>
    </td>
  </tr>
</table>

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python 3.10+ |
| **AI SDK** | OpenAI Python SDK |
| **Visualization** | Matplotlib |
| **Interface** | PyWebIO |

---

## 📦 Installation

### Install Dependencies

```bash
pip install openai matplotlib pywebio python-dotenv
```

### Clone Repository

```bash
git clone https://github.com/AlexisZ12/DataVizAiAssistant.git
cd DataVizAiAssistant
```

### Run the Application

#### Option 1: Local Interactive Mode

```bash
python app.py
```

The browser will open automatically. Settings are saved locally.

#### Option 2: Cloud Deployment Mode

The application runs at http://<your-local-ip>:8080/ by default.

**Interactive Mode**: Run `web.py`, enter API Key and other configurations in the interface after startup. Suitable for scenarios requiring flexible configuration switching.

**Pre-configured Mode**: Run `web_preset.py`, read preset configurations from `.env` file. Suitable for one-click startup or enterprise deployment.

1. Create configuration file:
```bash
cp .env.example .env
```

2. Edit `.env` file:
```env
OPENAI_API_KEY=your-api-key-here
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL=gpt-4o
```

3. Start the service:
```bash
python web_preset.py
```

---

## 🖼️ Supported Chart Types

| Chart Type | Use Case | Preview |
|:----------:|:--------:|:-------:|
| Line Plot | Time series, trend analysis | <img src="pic/plot.png" height="120"> |
| Scatter Plot | Correlation analysis, distribution patterns | <img src="pic/scatter.png" height="120"> |
| Bar Chart | Categorical data comparison | <img src="pic/bar.png" height="120"> |
| Stem Plot | Point value distribution | <img src="pic/stem.png" height="120"> |
| Fill Between | Range visualization | <img src="pic/fill_between.png" height="120"> |
| Stack Plot | Proportion composition analysis | <img src="pic/stackplot.png" height="120"> |
| Stairs Plot | Discrete value changes | <img src="pic/stairs.png" height="120"> |

---

## 🧭 Examples

### Example 1: Global Solar Power Data

**Input Description:**

> In 2025, the global solar power industry experienced rapid growth. According to the International Renewable Energy Agency (IRENA) report, the top five solar power countries have seen significant increases in installed capacity over the past year. Key data: China: 50 GW new capacity, 25% global market share; USA: 30 GW new capacity, 15% global market share; India: 20 GW new capacity, 10% global market share; Germany: 12 GW new capacity, 6% global market share; Japan: 8 GW new capacity, 4% global market share.

**Generated Result:**

<img src="pic/example1.png" height="280">

---

### Example 2: Stock Trend Analysis

**Input Description:**

> From the 1st to the 7th of this month, the stock of TechGen Inc. (TGI) showed some fluctuations. On the 1st, the stock opened at $152.45 and closed at $158.72. The next day, it saw a slight dip, opening at $157.20 and finishing at $155.35...

**Generated Result:**

<img src="pic/example2.png" height="280">

---

## 🛑 Notes

- Requires a valid LLM API key (OpenAI or compatible service)
- Using "forced thinking" mode will consume more tokens
- Chart quality depends on the LLM's understanding of natural language
- Large datasets should be preprocessed before input

---

## 🤝 Support & Contact

| Channel | Link |
|:-------:|:-----|
| 📂 **GitHub** | [AlexisZ12/DataVizAiAssistant](https://github.com/AlexisZ12/DataVizAiAssistant) |
| 🎁 **Afdian** | [AlexisZ12](https://afdian.com/a/AlexisZ12) |
| 📧 **Email** | 2242809239@qq.com |
| 💬 **WeChat** | `Alexis_12_Z` |

---

<div align="center">

**If you find this project helpful, please consider giving it a ⭐ Star!**

</div>
