"""LLM provider 配置：请求字段优先，缺省读项目根目录 .env。"""

import os

from dotenv import load_dotenv

from workflow.paths import REPO_ROOT

load_dotenv(REPO_ROOT / ".env")

_FIELDS = [("api_key", "API_KEY"), ("base_url", "BASE_URL"), ("model", "MODEL")]


def resolve_provider(api_key=None, base_url=None, model=None):
    values = {
        "api_key": api_key or os.environ.get("API_KEY"),
        "base_url": base_url or os.environ.get("BASE_URL"),
        "model": model or os.environ.get("MODEL"),
    }
    missing = [name for name, _ in _FIELDS if not values[name]]
    if missing:
        raise ValueError(
            f"缺少参数: {', '.join(missing)}（请在请求中提供或在项目根目录 .env 中配置）"
        )
    return values["api_key"], values["base_url"], values["model"]
