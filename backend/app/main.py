import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from workflow import engine
from workflow.config import resolve_provider

from .schemas import ChartResult, GenerateRequest, ModifyRequest

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("backend")

app = FastAPI(title="DataVizAiAssistant Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def _mask_key(key):
    if not key:
        return ""
    return f"{key[:4]}***{key[-4:]}" if len(key) > 8 else f"{key[:2]}***{key[-2:]}"


def _provider(req, action):
    try:
        api_key, base_url, model = resolve_provider(req.api_key, req.base_url, req.model)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    logger.info(
        "provider[%s] model=%s base_url=%s api_key=%s",
        action, model, base_url, _mask_key(api_key),
    )
    return api_key, base_url, model


def _run(fn):
    try:
        return fn()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/charts/generate", response_model=ChartResult)
def generate(req: GenerateRequest):
    api_key, base_url, model = _provider(req, "generate")
    return _run(lambda: engine.generate(
        req.description, req.thinking, api_key, base_url, model))


@app.post("/api/charts/modify-data", response_model=ChartResult)
def modify_data(req: ModifyRequest):
    api_key, base_url, model = _provider(req, "modify-data")
    return _run(lambda: engine.modify_data(
        req.demand, req.params, req.thinking, api_key, base_url, model))


@app.post("/api/charts/modify-style", response_model=ChartResult)
def modify_style(req: ModifyRequest):
    api_key, base_url, model = _provider(req, "modify-style")
    return _run(lambda: engine.modify_style(
        req.demand, req.params, req.thinking, api_key, base_url, model))
