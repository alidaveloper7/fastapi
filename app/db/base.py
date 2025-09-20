from __future__ import annotations
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy import DateTime, func
from typing import Optional

class Base(DeclarativeBase):
    pass

class TimestampMixin:
    created_at: Mapped[Optional["DateTime"]] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[Optional["DateTime"]] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class SoftDeleteMixin:
    deleted_at: Mapped[Optional["DateTime"]] = mapped_column(DateTime(timezone=True), nullable=True)
