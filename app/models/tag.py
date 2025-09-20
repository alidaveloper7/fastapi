from __future__ import annotations
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.db.base import Base, TimestampMixin, SoftDeleteMixin
from app.models.associations import post_tags

class Tag(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "tags"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)

    posts: Mapped[List["Post"]] = relationship("Post", secondary=post_tags, back_populates="tags")
