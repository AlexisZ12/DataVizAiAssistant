"""提示词模块：fast=快速模式，thinking=思考模式。"""
from . import fast, thinking


def get(mode: str):
    """按模式返回提示词模块，mode 为 'fast' 或 'thinking'。"""
    if mode == "thinking":
        return thinking
    return fast
