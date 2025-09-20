from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel
from .common import OrmBase

class PostCreate(BaseModel):
    title: str
    body: Optional[str] = None

class PostUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None

class PostOut(OrmBase):
    id: str
    title: str
    body: Optional[str] = None
