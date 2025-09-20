from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .common import OrmBase

class CommentCreate(BaseModel):
    content: str
    target_type: Literal["post", "product"]
    target_id: str

class CommentOut(OrmBase):
    id: str
    content: str
    target_type: str
    target_id: str
    user_id: str
