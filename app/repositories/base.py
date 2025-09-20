from __future__ import annotations
from typing import Any, Iterable, Sequence, TypeVar, Generic, Optional
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model: DeclarativeMeta):
        self.session = session
        self.model = model

    async def get(self, id: str, include_deleted: bool = False) -> Optional[T]:
        stmt = select(self.model).where(self.model.id == id)
        if not include_deleted and hasattr(self.model, "deleted_at"):
            stmt = stmt.where(self.model.deleted_at.is_(None))
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def list(self, *, offset=0, limit=20, order_by=None, filters: dict[str, Any] | None = None) -> Sequence[T]:
        stmt = select(self.model)
        if hasattr(self.model, "deleted_at"):
            stmt = stmt.where(self.model.deleted_at.is_(None))
        if filters:
            for col, val in filters.items():
                if hasattr(self.model, col) and val is not None:
                    stmt = stmt.where(getattr(self.model, col) == val)
        if order_by is not None:
            stmt = stmt.order_by(order_by)
        stmt = stmt.offset(offset).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def create(self, obj: T) -> T:
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def update_fields(self, id: str, data: dict[str, Any]) -> Optional[T]:
        stmt = (
            update(self.model)
            .where(self.model.id == id)
            .values(**data)
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def soft_delete(self, id: str) -> bool:
        if not hasattr(self.model, "deleted_at"):
            return False
        from sqlalchemy import func
        stmt = (
            update(self.model)
            .where(self.model.id == id, self.model.deleted_at.is_(None))
            .values(deleted_at=func.now())
        )
        res = await self.session.execute(stmt)
        return res.rowcount > 0

    async def restore(self, id: str) -> bool:
        if not hasattr(self.model, "deleted_at"):
            return False
        stmt = (
            update(self.model)
            .where(self.model.id == id, self.model.deleted_at.is_not(None))
            .values(deleted_at=None)
        )
        res = await self.session.execute(stmt)
        return res.rowcount > 0

    async def force_delete(self, id: str) -> bool:
        stmt = delete(self.model).where(self.model.id == id)
        res = await self.session.execute(stmt)
        return res.rowcount > 0
