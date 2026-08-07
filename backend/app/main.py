from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from workflow import engine
from workflow.config import resolve_provider

from .schemas import ChartResult, GenerateRequest, ModifyRequest

app = FastAPI(title="DataVizAiAssistant Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def _provider(req):
    try:
        return resolve_provider(req.api_key, req.base_url, req.model)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


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
    api_key, base_url, model = _provider(req)
    return _run(lambda: engine.generate(
        req.description, req.thinking, api_key, base_url, model))


@app.post("/api/charts/modify-data", response_model=ChartResult)
def modify_data(req: ModifyRequest):
    api_key, base_url, model = _provider(req)
    return _run(lambda: engine.modify_data(
        req.demand, req.params, req.thinking, api_key, base_url, model))


@app.post("/api/charts/modify-style", response_model=ChartResult)
def modify_style(req: ModifyRequest):
    api_key, base_url, model = _provider(req)
    return _run(lambda: engine.modify_style(
        req.demand, req.params, req.thinking, api_key, base_url, model))
