"""编排入口：generate / modify_data / modify_style。

7 个图表模块位于 workflow/charts/，每个负责一种图表的多阶段生成
（数据/样式/范围/标签提取 + 渲染）。流水线逻辑对齐原 function.py：
Phase1 选类型 → 图表模块内部完成 Phase2-5 → 渲染。
"""

import json

from openai import OpenAI

from workflow.prompts import get as get_prompts
from workflow.charts import (
    bar,
    fillbetween,
    plot,
    scatter,
    stackplot,
    stairs,
    stem,
)

from workflow import llm, render

CHART_MODULES = [
    plot.plot, scatter.scatter, bar.bar, stem.stem,
    fillbetween.fillbetween, stackplot.stackplot, stairs.stairs,
]


def generate(description, thinking, api_key, base_url, model):
    client = OpenAI(api_key=api_key, base_url=base_url)
    prompts = get_prompts("thinking" if thinking else "fast")

    prompt1 = prompts.CHART_TYPE_SELECT
    result = llm.call_and_parse(
        client, model,
        [{"role": "user", "content": prompt1 + description}],
        llm.validate_chart_type,
    )
    chart_type = result["id"]

    prompt4 = prompts.RANGE
    prompt5 = prompts.LABELS
    prompt2 = prompts.DATA_EXTRACT[chart_type]
    prompt3 = prompts.STYLE[chart_type]

    def _do():
        fig, data, style_config, range_config, label_config = CHART_MODULES[chart_type](
            description, client, model, prompt2, prompt3, prompt4, prompt5
        )
        config = {**style_config, **range_config, **label_config}
        return data, config, render._encode(fig)

    data, config, image = render.render_atomic(_do)

    params = {
        "chart_type": chart_type,
        "description": description,
        "data": data,
        "config": config,
    }
    return {"image": image, "params": params, "thinking": thinking}


def modify_data(demand, params, thinking, api_key, base_url, model):
    client = OpenAI(api_key=api_key, base_url=base_url)
    prompts = get_prompts("thinking" if thinking else "fast")

    message = [{"role": "user", "content": prompts.MODIFY_DATA.format(
        demand, json.dumps(params["data"], ensure_ascii=False))}]
    new_data = llm.call_and_parse(client, model, message)

    image = render.render_from_config(params["chart_type"], new_data, params["config"])
    new_params = {**params, "data": new_data}
    return {"image": image, "params": new_params, "thinking": thinking}


def modify_style(demand, params, thinking, api_key, base_url, model):
    client = OpenAI(api_key=api_key, base_url=base_url)
    prompts = get_prompts("thinking" if thinking else "fast")
    chart_type = params["chart_type"]

    message_new = [
        {"role": "user", "content": prompts.STYLE[chart_type].split("### 用户需求:")[0]},
        {"role": "user", "content": prompts.RANGE.split("### 用户需求:")[0]},
        {"role": "user", "content": prompts.LABELS.split("### 用户需求:")[0]},
        {"role": "user", "content": "### 用户需求:\n" + params["description"]},
    ]
    message = message_new + [{"role": "user", "content": prompts.MODIFY_STYLE.format(
        demand, json.dumps(params["config"], ensure_ascii=False))}]
    new_config = llm.call_and_parse(client, model, message)

    image = render.render_from_config(chart_type, params["data"], new_config)
    new_params = {**params, "config": new_config}
    return {"image": image, "params": new_params, "thinking": thinking}
