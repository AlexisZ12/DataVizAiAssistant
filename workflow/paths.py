"""定位仓库根目录，并把根目录注入 sys.path 以便复用原图表模块。"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def setup_root_path():
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
