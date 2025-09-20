from __future__ import annotations
from typing import Optional
from app.repositories.user_repo import UserRepository
from app.core.security import verify_password, create_access_token

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def authenticate(self, email: str, password: str) -> Optional[str]:
        email = email.strip().lower()
        user = await self.user_repo.get_by_email(email)
        if not user or not verify_password(password, user.password_hash) or not user.is_active:
            return None
        token = create_access_token(subject=user.id, extra={"email": user.email})
        return token
