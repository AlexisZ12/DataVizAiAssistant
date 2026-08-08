import logging

import matplotlib

matplotlib.use("Agg")

__version__ = "0.1.0"

# 统一日志格式。root 已有 handler（如 uvicorn 运行时）则保持 uvicorn 的配置；
# 独立运行（skill/脚本）时兜底配置一个，避免日志静默丢失。
if not logging.getLogger().handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
