<div align="center">

# DataViz AI Assistant Skill

**AI Data Visualization CLI Tool** — An intelligent chart generation script powered by Large Language Models that can be integrated as a Skill into AI coding assistants like OpenClaw, QwenPaw, and Claude Code. Simply describe your data and analysis needs in natural language to automatically generate professional Matplotlib charts as PNG files. Supports 7 chart types including line plots, scatter plots, and bar charts, compatible with OpenAI standard API and alternatives like DeepSeek.

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)](https://matplotlib.org/)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-pink.svg)](https://github.com/openclaw)
[![QwenPaw](https://img.shields.io/badge/QwenPaw-Skill-cyan.svg)](https://github.com/qwenpaw)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet.svg)](https://claude.ai/code)

[中文](README.md) | [English](README_EN.md)

</div>

---

## 📖 Overview

DataViz AI Assistant Skill packages the [DataVizAiAssistant](https://github.com/AlexisZ12/DataVizAiAssistant) project as a CLI tool. It strips away the Web UI layer while preserving the core multi-stage LLM chart generation pipeline as a pure CLI interface. Can run as a standalone script or be integrated as a Skill into AI coding assistants like OpenClaw, QwenPaw, and Claude Code.

---

## ✨ Key Features

<table>
  <tr>
    <td align="center" width="50%">
      <h3>📊 One-Shot Generation</h3>
      <p>Natural language input → PNG output. All diagnostics go to stderr; stdout prints only the image path for easy scripting and piping</p>
    </td>
    <td align="center" width="50%">
      <h3>🌐 Multi-Platform</h3>
      <p>Configure API Key, Base URL, and Model via environment variables. Compatible with OpenAI, DeepSeek, Ollama, and all compatible APIs</p>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <h3>🖼️ 7 Chart Types</h3>
      <p>Automatically detects user intent and selects from line, scatter, bar, stem, fill-between, stackplot, and stairs charts</p>
    </td>
    <td align="center" width="50%">
      <h3>🔧 Custom Output Path</h3>
      <p>Use <code>-o</code> to specify output path; defaults to system temp directory when omitted</p>
    </td>
  </tr>
</table>

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python 3.10+ |
| **AI SDK** | OpenAI Python SDK |
| **Visualization** | Matplotlib + NumPy |

---

## 📦 Quick Start

### Install Dependencies

```bash
pip install openai matplotlib numpy
```

### Set Environment Variables

```bash
export DATAVIZ_AI_API_KEY="sk-your-api-key"
export DATAVIZ_AI_BASE_URL="https://api.openai.com/v1"
export DATAVIZ_AI_MODEL="gpt-4o"
```

All three environment variables are **required** with no defaults.

### Run

```bash
cd dataviz_ai
python scripts/dataviz_ai.py "2024 monthly sales trend: Jan 100, Feb 200, Mar 150"
```

### Specify Output Path

```bash
python scripts/dataviz_ai.py "GDP comparison: Shanghai vs Beijing" -o ./chart.png
```

---

## 📋 CLI Arguments

| Argument | Required | Description |
|----------|:--------:|-------------|
| `description` | Yes | Positional argument — natural language chart description |
| `-o`, `--output` | No | Output image path (default: temp file) |

---

## 🔧 Environment Variables

| Variable | Required | Description |
|----------|:--------:|-------------|
| `DATAVIZ_AI_API_KEY` | Yes | LLM API key |
| `DATAVIZ_AI_BASE_URL` | Yes | API base URL |
| `DATAVIZ_AI_MODEL` | Yes | Model name |

---

## 🖼️ Supported Chart Types

| ID | Type | Best For |
|:--:|:----:|:---------|
| 0 | line plot | Time series, trend analysis |
| 1 | scatter plot | Correlation, distribution patterns |
| 2 | bar chart | Categorical comparison |
| 3 | stem plot | Discrete point distribution |
| 4 | fill between | Range visualization, uncertainty bands |
| 5 | stackplot | Multi-series proportion analysis |
| 6 | stairs plot | Step/segmented data changes |

---

## 🧭 Examples

### Example 1: Sales Trend

**Input:**

```bash
python scripts/dataviz_ai.py \
  "2024 Jan-Jun sales: Jan 120, Feb 200, Mar 150, Apr 300, May 250, Jun 400"
```

**Output:**

```
/tmp/dataviz_x1a2b3.png
```

### Example 2: Multi-City Comparison

**Input:**

```bash
python scripts/dataviz_ai.py \
  "Beijing and Shanghai 2020-2024 GDP comparison: Beijing 3.6,4.0,4.1,4.4,4.9 trillion; Shanghai 3.9,4.3,4.4,4.7,5.3 trillion" \
  -o ./gdp_comparison.png
```

**Output:**

```
./gdp_comparison.png
```

---

## 🔄 Pipeline

```
User input → [Phase 1: Chart type selection] → [Phase 2: Data extraction]
                                                ↓
                              [Phase 3-5: Parallel style/range/label design]
                                                ↓
                              [Phase 6: Matplotlib render] → PNG file
```

1. **Phase 1** — LLM selects the best chart type (0-6) for the request
2. **Phase 2** — LLM extracts structured data (x, y values, labels) from the description
3. **Phase 3-5** — LLM designs style (markers/colors/line styles), axis ranges, and labels (title, axis labels) in parallel
4. **Phase 6** — Matplotlib renders the chart and saves it as PNG

---

## 🛑 Notes

- Requires a valid LLM API key (OpenAI or compatible service)
- Chart quality depends on the LLM's understanding of natural language
- Large datasets should be preprocessed before input
- This Skill uses non-thinking mode only

---

## 🤝 Support & Contact

| Channel | Link |
|:-------:|:-----|
| 📂 **GitHub** | [AlexisZ12/DataVizAiAssistant](https://github.com/AlexisZ12/DataVizAiAssistant) |
| 📧 **Email** | 2242809239@qq.com |
| 💬 **WeChat** | `Alexis_12_Z` |

---

<div align="center">

**If you find this project helpful, please consider giving it a ⭐ Star!**

</div>
