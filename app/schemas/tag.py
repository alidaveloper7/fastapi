from __future__ import annotations
from pydantic import BaseModel
from .common import OrmBase

class TagCreate(BaseModel):
    name: str

class TagOut(OrmBase):
    id: str
    name: str
