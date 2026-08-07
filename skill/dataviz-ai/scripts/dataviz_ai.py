#!/usr/bin/env python3
"""
DataVizAiAssistant Skill Script
Generates a matplotlib chart from a natural language description using an LLM.

Usage:
    python dataviz_ai.py "画出2024年各月销售额趋势"

Environment variables (all required):
    DATAVIZ_AI_API_KEY     API key for OpenAI-compatible service
    DATAVIZ_AI_BASE_URL    Base URL of the API
    DATAVIZ_AI_MODEL       Model name to use

Output:
    Prints the path to the generated PNG image on stdout.
"""

import argparse
import sys
import os
import json
from openai import OpenAI

import matplotlib
matplotlib.use("Agg")

# Ensure local modules can be imported
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)

_PROMPT_DIR = os.path.join(_SCRIPT_DIR, "prompts")


def _read_prompt(filename):
    with open(os.path.join(_PROMPT_DIR, filename), "r", encoding="utf-8") as f:
        return f.read()


def _call_llm_and_parse_json(client, model, messages):
    """Call LLM and parse JSON from response, with retry on failure."""
    while True:
        openai_out = client.chat.completions.create(
            model=model, messages=messages
        ).choices[0].message.content
        print(f"[LLM output] {openai_out}", file=sys.stderr)

        try:
            result = json.loads(
                "{" + openai_out.split("{", 1)[1].split("}", 1)[0] + "}"
            )
            return result, openai_out
        except (json.JSONDecodeError, IndexError) as e:
            print(f"[JSON parse error] {e}, retrying...", file=sys.stderr)
            messages.append({"role": "assistant", "content": openai_out})
            messages.append(
                {
                    "role": "user",
                    "content": f"你返回的JSON格式不正确，错误信息: {e}。请重新返回符合格式要求的JSON。",
                }
            )


def _validate_phase1_result(result):
    """Validate Phase 1 result: must have 'id' as int in 0-6."""
    if "id" not in result:
        raise KeyError("缺少必需字段 'id'")
    if not isinstance(result["id"], int):
        raise TypeError("字段 'id' 必须是整数类型")
    if result["id"] not in [0, 1, 2, 3, 4, 5, 6]:
        raise ValueError("字段 'id' 必须是 0-6 之间的整数")
    return True


def generate(text_in, output=None):
    # Read environment variables
    api_key = os.environ.get("DATAVIZ_AI_API_KEY")
    base_url = os.environ.get("DATAVIZ_AI_BASE_URL")
    model = os.environ.get("DATAVIZ_AI_MODEL")

    for name, value in [("DATAVIZ_AI_API_KEY", api_key), ("DATAVIZ_AI_BASE_URL", base_url), ("DATAVIZ_AI_MODEL", model)]:
        if not value:
            print(f"Error: {name} environment variable is required", file=sys.stderr)
            sys.exit(1)

    client = OpenAI(api_key=api_key, base_url=base_url)

    # ------------------------------------------------------------------
    # Phase 1: Choose chart type
    # ------------------------------------------------------------------
    prompt1 = _read_prompt("prompt1a.txt")
    messages1 = [{"role": "user", "content": prompt1 + text_in}]

    print("[Phase 1] Selecting chart type...", file=sys.stderr)

    while True:
        result, openai_out = _call_llm_and_parse_json(client, model, messages1)
        try:
            _validate_phase1_result(result)
            break
        except (KeyError, TypeError, ValueError) as e:
            print(f"[Validation error] {e}, retrying...", file=sys.stderr)
            messages1.append({"role": "assistant", "content": openai_out})
            messages1.append(
                {
                    "role": "user",
                    "content": f"你返回的JSON格式不正确，错误信息: {e}。请重新返回符合格式要求的JSON。",
                }
            )

    chart_type = result["id"]
    print(f"[Phase 1] Selected chart type: {chart_type}", file=sys.stderr)

    # ------------------------------------------------------------------
    # Phase 2-5: Extract data, design style/range/labels (handled by module)
    # ------------------------------------------------------------------
    prompt4 = _read_prompt("prompt4a.txt")
    prompt5 = _read_prompt("prompt5a.txt")

    chart_names = [
        "plot",
        "scatter",
        "bar",
        "stem",
        "fillbetween",
        "stackplot",
        "stairs",
    ]
    module_name = chart_names[chart_type]

    prompt2 = _read_prompt(f"prompt2a{chart_type}.txt")
    prompt3 = _read_prompt(f"prompt3a{chart_type}.txt")

    print(f"[Phase 2-5] Extracting data and designing chart via '{module_name}'...", file=sys.stderr)

    mod = __import__(module_name)
    fn = getattr(mod, module_name)
    fig, data, style_config, range_config, label_config = fn(
        text_in, client, model, prompt2, prompt3, prompt4, prompt5
    )

    # ------------------------------------------------------------------
    # Save chart to file
    # ------------------------------------------------------------------
    if output:
        output_path = output
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    else:
        from datetime import datetime
        output_dir = os.path.join(os.getcwd(), "tmp")
        os.makedirs(output_dir, exist_ok=True)
        filename = f"dataviz_{datetime.now().strftime('%Y%m%d%H%M')}.png"
        output_path = os.path.join(output_dir, filename)
    fig.savefig(output_path, format="png")
    fig.close()

    print(f"[Done] Chart saved to: {output_path}", file=sys.stderr)
    print(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a matplotlib chart from a natural language description using an LLM."
    )
    parser.add_argument(
        "description",
        type=str,
        help="Natural language description of the chart to generate.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Output image path. Defaults to a temp file.",
    )
    args = parser.parse_args()
    generate(args.description, output=args.output)
