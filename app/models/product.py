from __future__ import annotations
from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship, foreign
from sqlalchemy import String, Text
from app.db.base import Base, TimestampMixin, SoftDeleteMixin

class Product(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    comments: Mapped[List["Comment"]] = relationship(
        "Comment",
        primaryjoin="and_(foreign(Comment.target_id)==Product.id, Comment.target_type=='product')",
        viewonly=True,
    )
