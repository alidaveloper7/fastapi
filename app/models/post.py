from __future__ import annotations
from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship, foreign
from sqlalchemy import String, Text, and_
from app.db.base import Base, TimestampMixin, SoftDeleteMixin
from app.models.associations import post_tags, post_responsibles

class Post(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "posts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_by_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)

    # many-to-many
    tags: Mapped[List["Tag"]] = relationship("Tag", secondary=post_tags, back_populates="posts")
    responsibles: Mapped[List["User"]] = relationship("User", secondary=post_responsibles, back_populates="responsible_posts")

    # polymorphic comments (target_type='post')
    comments: Mapped[List["Comment"]] = relationship(
        "Comment",
        primaryjoin="and_(foreign(Comment.target_id)==Post.id, Comment.target_type=='post')",
        viewonly=True,
    )
