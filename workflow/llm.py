"""LLM 调用与 JSON 容错：提取、校验、失败自动重试（对齐原 function.py 逻辑）。"""

import json


def extract_json(text):
    """从 LLM 输出中截取第一个 {...} 并解析为 dict。"""
    return json.loads("{" + text.split("{", 1)[1].split("}", 1)[0] + "}")


def validate_chart_type(result):
    """Phase 1 校验：id 必须为 0-6 的整数。"""
    if "id" not in result:
        raise KeyError("缺少必需字段 'id'")
    if not isinstance(result["id"], int):
        raise TypeError("字段 'id' 必须是整数类型")
    if result["id"] not in [0, 1, 2, 3, 4, 5, 6]:
        raise ValueError("字段 'id' 必须是 0-6 之间的整数")


def call_and_parse(client, model, base_messages, validator=None):
    """调用 LLM 并解析 JSON；解析或校验失败时带着错误信息重试。"""
    messages = base_messages
    while True:
        out = client.chat.completions.create(
            model=model, messages=messages
        ).choices[0].message.content
        print(out)
        try:
            result = extract_json(out)
            if validator:
                validator(result)
            return result
        except (json.JSONDecodeError, IndexError, KeyError, TypeError, ValueError) as e:
            messages = base_messages + [
                {"role": "assistant", "content": out},
                {
                    "role": "user",
                    "content": f"你返回的JSON格式不正确，错误信息: {e}。请重新返回符合格式要求的JSON。",
                },
            ]
