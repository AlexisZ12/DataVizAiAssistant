from typing import Any, Optional

from pydantic import BaseModel


class GenerateRequest(BaseModel):
    description: str
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    model: Optional[str] = None
    thinking: bool = False


class ModifyRequest(BaseModel):
    demand: str
    params: dict[str, Any]
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    model: Optional[str] = None
    thinking: bool = False


class ChartResult(BaseModel):
    image: str
    params: dict[str, Any]
    thinking: bool
