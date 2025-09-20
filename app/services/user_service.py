from __future__ import annotations
from typing import Sequence, Optional
from uuid import uuid4
from sqlalchemy import asc, desc
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User
from app.core.security import hash_password
from app.services.email_service import EmailService

class UserService:
    def __init__(self, repo: UserRepository, email_service: EmailService):
        self.repo = repo
        self.email_service = email_service

    async def list(self, *, page: int = 1, per_page: int = 20, sort: str = "created_at", dir: str = "desc") -> Sequence[User]:
        offset = (page - 1) * per_page
        order = desc(getattr(User, sort)) if dir == "desc" else asc(getattr(User, sort))
        return await self.repo.list(offset=offset, limit=per_page, order_by=order)

    async def get(self, user_id: str) -> Optional[User]:
        return await self.repo.get(user_id)

    async def create(self, data: UserCreate) -> User:
        user = User(
            id=str(uuid4()),
            email=data.email.strip().lower(),
            password_hash=hash_password(data.password),
            full_name=data.full_name,
            is_active=True,
        )
        await self.repo.create(user)
        return user

    async def update(self, user_id: str, data: UserUpdate) -> Optional[User]:
        payload = {k: v for k, v in data.model_dump(exclude_unset=True).items()}
        return await self.repo.update_fields(user_id, payload)

    async def soft_delete(self, user_id: str) -> bool:
        return await self.repo.soft_delete(user_id)

    async def restore(self, user_id: str) -> bool:
        return await self.repo.restore(user_id)

    async def force_delete(self, user_id: str) -> bool:
        return await self.repo.force_delete(user_id)

    async def send_welcome_email(self, to_email: str) -> None:
        await self.email_service.send_welcome(to=to_email)
