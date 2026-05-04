---
name: dataviz-ai
description: Generate data visualization charts (line, scatter, bar, stem, fill-between, stackplot, stairs) from natural language descriptions using an LLM-powered matplotlib pipeline. Supports 7 chart types via OpenAI-compatible APIs.
---

# DataViz AI Assistant Skill

Generate matplotlib charts from natural language descriptions using a multi-stage
LLM pipeline. The skill analyzes your request, extracts data, designs the visual
style, and outputs a PNG image.

## Usage

```
python scripts/dataviz_ai.py "your chart description" [-o output.png]
```

| Argument          | Required | Description                                    |
|-------------------|----------|------------------------------------------------|
| `description`     | Yes      | Natural language description of the chart      |
| `-o`, `--output`  | No       | Output image path (default: temp file)         |

All diagnostic messages go to stderr. Only the image path is printed to stdout.

### Example

```bash
python scripts/dataviz_ai.py \
  "2024年各月销售额趋势，1月100,2月200,3月150,4月300,5月250,6月400"

python scripts/dataviz_ai.py \
  "画出上海和北京各季度GDP对比" -o ./gdp_chart.png
```

## Environment Variables

All three variables are **required**:

| Variable          | Description                             |
|-------------------|-----------------------------------------|
| `DATAVIZ_AI_API_KEY`  | API key for the LLM service             |
| `DATAVIZ_AI_BASE_URL` | Base URL for OpenAI-compatible API      |
| `DATAVIZ_AI_MODEL`           | Model name to use                       |

## Supported Chart Types

| ID | Type          | Best for                                    |
|----|---------------|---------------------------------------------|
| 0  | line plot     | Trends and continuous data                  |
| 1  | scatter plot  | Relationships, outliers, correlation        |
| 2  | bar chart     | Comparing categories                        |
| 3  | stem plot     | Discrete data points with structure         |
| 4  | fill between  | Areas between curves, uncertainty bands     |
| 5  | stackplot     | Multiple series over a shared axis          |
| 6  | stairs plot   | Step changes, segmented data                |

## How It Works

1. **Phase 1** — LLM selects the best chart type (0-6) for the request
2. **Phase 2** — LLM extracts structured data (x, y values, labels) from the description
3. **Phase 3-5** — LLM designs style (markers/colors/line styles), axis ranges,
   and labels (title, axis labels) in parallel
4. **Phase 6** — Matplotlib renders the chart and saves it as PNG

## Dependencies

- `openai`
- `matplotlib`
- `numpy`
