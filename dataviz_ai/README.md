<div align="center">

# DataViz AI Assistant Skill

**AI 数据可视化命令行工具** — 基于大语言模型的智能图表生成脚本，可集成到 OpenClaw、QwenPaw、Claude Code 等 AI 编程助手中作为 Skill 调用。只需用自然语言描述数据和分析需求，即可自动生成专业的 Matplotlib 可视化图表，输出为 PNG 文件。支持线图、散点图、条形图等 7 种图表类型，兼容 OpenAI 标准 API 及 DeepSeek 等替代平台。

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)](https://matplotlib.org/)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-pink.svg)](https://github.com/openclaw/openclaw)
[![QwenPaw](https://img.shields.io/badge/QwenPaw-Skill-cyan.svg)](https://github.com/agentscope-ai/QwenPaw)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet.svg)](https://claude.ai/code)

[中文](README.md) | [English](README_EN.md)

</div>

---

## 📖 简介

DataViz AI Assistant Skill 是将 [DataVizAiAssistant](https://github.com/AlexisZ12/DataVizAiAssistant) 项目封装为命令行工具。去除原项目的 Web UI 交互层，保留核心的多阶段 LLM 图表生成流程，输出为纯 CLI 接口。可作为独立脚本运行，也可作为 Skill 集成到 OpenClaw、QwenPaw、Claude Code 等 AI 编程助手中自动调用。

---

## ✨ 核心功能

<table>
  <tr>
    <td align="center" width="50%">
      <h3>📊 一键图表生成</h3>
      <p>自然语言输入 → PNG 图片输出，所有诊断信息输出到 stderr，stdout 只打印图片路径，方便脚本集成</p>
    </td>
    <td align="center" width="50%">
      <h3>🌐 多平台兼容</h3>
      <p>通过环境变量配置 API Key、Base URL 和模型，兼容 OpenAI、DeepSeek、Ollama 等所有兼容接口</p>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <h3>🖼️ 7 种图表类型</h3>
      <p>自动识别用户意图选择合适的图表类型，支持线图、散点图、条形图、茎叶图、填充图、堆叠图、阶梯图</p>
    </td>
    <td align="center" width="50%">
      <h3>🔧 可指定输出路径</h3>
      <p>支持 <code>-o</code> 参数自定义输出路径，不指定则保存到系统临时目录</p>
    </td>
  </tr>
</table>

---

## 🛠️ 技术栈

| 类别 | 技术 |
|------|------|
| **后端** | Python 3.10+ |
| **AI SDK** | OpenAI Python SDK |
| **可视化** | Matplotlib + NumPy |

---

## 📦 快速开始

### 安装依赖

```bash
pip install openai matplotlib numpy
```

### 设置环境变量

```bash
export DATAVIZ_AI_API_KEY="sk-your-api-key"
export DATAVIZ_AI_BASE_URL="https://api.openai.com/v1"
export DATAVIZ_AI_MODEL="gpt-4o"
```

三个环境变量均为**必需**，不提供默认值。

### 运行

```bash
cd dataviz_ai
python scripts/dataviz_ai.py "画出2024年各月销售额趋势，1月100,2月200,3月150"
```

### 指定输出路径

```bash
python scripts/dataviz_ai.py "画出上海和北京各季度GDP对比" -o ./chart.png
```

---

## 📋 命令行参数

| 参数 | 必需 | 说明 |
|------|:----:|------|
| `description` | 是 | 位置参数，自然语言描述要生成的图表 |
| `-o`, `--output` | 否 | 输出图片路径，不指定则保存到临时目录 |

---

## 🔧 环境变量

| 变量 | 必需 | 说明 |
|------|:----:|------|
| `DATAVIZ_AI_API_KEY` | 是 | LLM API 密钥 |
| `DATAVIZ_AI_BASE_URL` | 是 | API 基础 URL |
| `DATAVIZ_AI_MODEL` | 是 | 模型名称 |

---

## 🖼️ 支持的图表类型

| ID | 类型 | 适用场景 |
|:--:|:----:|:--------:|
| 0 | 线图 | 时间序列、趋势分析 |
| 1 | 散点图 | 相关性分析、分布模式 |
| 2 | 条形图 | 分类数据比较 |
| 3 | 茎叶图 | 离散数据点分布 |
| 4 | 填充图 | 范围可视化、不确定性区间 |
| 5 | 堆叠图 | 多序列比例构成分析 |
| 6 | 阶梯图 | 分段/步进数据变化 |

---

## 🧭 使用示例

### 示例 1：销售额趋势

**输入：**

```bash
python scripts/dataviz_ai.py \
  "2024年1-6月销售额：1月120万,2月200万,3月150万,4月300万,5月250万,6月400万"
```

**输出：**

```
/tmp/dataviz_x1a2b3.png
```

### 示例 2：多城市对比

**输入：**

```bash
python scripts/dataviz_ai.py \
  "北京和上海2020-2024年GDP对比：北京分别为3.6,4.0,4.1,4.4,4.9万亿；上海分别为3.9,4.3,4.4,4.7,5.3万亿" \
  -o ./gdp_comparison.png
```

**输出：**

```
./gdp_comparison.png
```

---

## 🔄 工作流程

```
用户描述 → [Phase 1: 图表类型选择] → [Phase 2: 数据提取]
                                        ↓
                              [Phase 3-5: 并行设计样式/范围/标签]
                                        ↓
                              [Phase 6: Matplotlib 渲染] → PNG 文件
```

1. **Phase 1** — LLM 根据用户需求选择最佳图表类型（0-6）
2. **Phase 2** — LLM 从描述中提取结构化数据（x, y 值, 标签）
3. **Phase 3-5** — LLM 并行设计样式（标记/颜色/线型）、坐标轴范围和标签（标题、轴标签）
4. **Phase 6** — Matplotlib 渲染图表并保存为 PNG

---

## 🛑 注意事项

- 需要有效的 LLM API 密钥（OpenAI 或兼容服务）
- 图表质量取决于 LLM 对自然语言的理解准确性
- 大数据集建议预处理后再输入
- 本 Skill 仅使用非思考模式，不包含强制思考功能

---

## 🤝 支持与联系

| 渠道 | 链接 |
|:----:|:-----|
| 📂 **GitHub** | [AlexisZ12/DataVizAiAssistant](https://github.com/AlexisZ12/DataVizAiAssistant) |
| 📧 **邮箱** | 2242809239@qq.com |
| 💬 **微信** | `Alexis_12_Z` |

---

<div align="center">

**如果觉得这个项目有帮助，欢迎 ⭐ Star 支持一下！**

</div>
