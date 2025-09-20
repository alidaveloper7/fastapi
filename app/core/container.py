from __future__ import annotations
# A tiny, explicit 'container' layer using FastAPI Depends hooks.
# We avoid external DI libs; instead define provider functions here.

from fastapi import Depends
from app.core.config import settings
from app.db.session import get_session, AsyncSession
from app.http.clients.email_client import EmailHttpClient
from app.repositories.user_repo import UserRepository
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.services.email_service import EmailService

# Http Clients
def get_email_client() -> EmailHttpClient:
    return EmailHttpClient(
        base_url=settings.email_api_base,
        send_path=settings.email_send_path,
        token=settings.email_api_token,
    )

# Repositories
def get_user_repository(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session=session)

# Services
def get_email_service(client: EmailHttpClient = Depends(get_email_client)) -> EmailService:
    return EmailService(client=client)

def get_user_service(
    repo: UserRepository = Depends(get_user_repository),
    email_service: EmailService = Depends(get_email_service),
) -> UserService:
    return UserService(repo=repo, email_service=email_service)

def get_auth_service(
    repo: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repo=repo)
