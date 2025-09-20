from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
from .common import OrmBase

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    is_active: Optional[bool] = None

class UserOut(OrmBase):
    id: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool
