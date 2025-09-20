from __future__ import annotations

from typing import Optional
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base, TimestampMixin, SoftDeleteMixin


class UserProfile(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "user_profiles"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)

    # real FK + keep one-to-one uniqueness
    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )

    avatar_url: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)
    bio: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # FK is enough; no primaryjoin string needed
    user: Mapped["User"] = relationship("User", back_populates="profile")
