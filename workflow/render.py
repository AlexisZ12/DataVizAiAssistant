"""图表渲染层：根据 (图表类型, 数据, 配置) 重建 matplotlib 图形并编码为 base64。

原 MatplotlibInterface 基于全局 pyplot 状态，线程不安全，因此所有渲染用
RENDER_LOCK 串行化，并在每次渲染前 clf() 清空画布、结束后 close() 释放。
"""

import base64
import io
import threading

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from workflow.charts import MatplotlibInterface

RENDER_LOCK = threading.Lock()


def _encode(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return "data:image/png;base64," + base64.b64encode(buf.read()).decode()


def render_atomic(fn):
    """在全局渲染锁内执行 fn（fn 负责作图并返回 image），结束后释放画布。"""
    with RENDER_LOCK:
        plt.clf()
        try:
            return fn()
        finally:
            plt.close("all")


def _build(chart_type, data, config):
    if chart_type == 0:
        return MatplotlibInterface.PlotInterface(
            data["x"], data["y"], data["ylabel"],
            config["marker"], config["linestyle"], config["mcolor"], config["lcolor"],
            config["xmin"], config["xmax"], config["xstep"], config["ymin"], config["ymax"], config["ystep"],
            config["xlabel"], config["ylabel"], config["title"])
    if chart_type == 1:
        return MatplotlibInterface.ScatterInterface(
            data["x"], data["y"],
            config["mcolor"], config["msize"], config["malpha"],
            config["xmin"], config["xmax"], config["xstep"], config["ymin"], config["ymax"], config["ystep"],
            config["xlabel"], config["ylabel"], config["title"])
    if chart_type == 2:
        return MatplotlibInterface.BarInterface(
            data["x"], data["y"], data["ylabel"],
            config["bcolor"], config["hatch"],
            config["xmin"], config["xmax"], config["xstep"], config["ymin"], config["ymax"], config["ystep"],
            config["xlabel"], config["ylabel"], config["title"])
    if chart_type == 3:
        return MatplotlibInterface.StemInterface(
            data["x"], data["y"], data["ylabel"],
            config["marker"], config["linelinestyle"], config["baselinestyle"],
            config["mcolor"], config["lcolor"], config["bcolor"],
            config["xmin"], config["xmax"], config["xstep"], config["ymin"], config["ymax"], config["ystep"],
            config["xlabel"], config["ylabel"], config["title"])
    if chart_type == 4:
        return MatplotlibInterface.FillBetweenInterface(
            data["x"], data["y1"], data["y2"], data["ylabel"],
            config["fcolor"], config["falpha"],
            config["xmin"], config["xmax"], config["xstep"], config["ymin"], config["ymax"], config["ystep"],
            config["title"], config["xlabel"], config["ylabel"])
    if chart_type == 5:
        return MatplotlibInterface.StackplotInterface(
            data["x"], data["y"], data["ylabel"],
            config["fcolor"], config["falpha"],
            config["xmin"], config["xmax"], config["xstep"], config["ymin"], config["ymax"], config["ystep"],
            config["title"], config["xlabel"], config["ylabel"])
    if chart_type == 6:
        return MatplotlibInterface.StairsInterface(
            data["value"], data["position"], data["label"],
            config["color"],
            config["xmin"], config["xmax"], config["xstep"], config["ymin"], config["ymax"], config["ystep"],
            config["title"], config["xlabel"], config["ylabel"])
    raise ValueError(f"不支持的图表类型: {chart_type}")


def render_from_config(chart_type, data, config):
    """直接根据已有数据和配置重建图形（修改链路用），返回 base64 图片。"""
    with RENDER_LOCK:
        plt.clf()
        try:
            return _encode(_build(chart_type, data, config))
        finally:
            plt.close("all")
