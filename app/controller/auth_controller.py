from fastapi import Depends, HTTPException, status, BackgroundTasks
from app.schemas.auth import LoginIn, TokenOut
from app.schemas.user import UserCreate, UserOut
from app.core.container import get_user_service, get_auth_service
from app.services.user_service import UserService
from app.services.auth_service import AuthService

async def register(
    payload: UserCreate,
    background: BackgroundTasks,
    svc: UserService = Depends(get_user_service)
) -> UserOut:
    user = await svc.create(payload)
    background.add_task(svc.send_welcome_email, user.email)
    return user

async def login(
    payload: LoginIn,
    auth: AuthService = Depends(get_auth_service)
) -> TokenOut:
    token = await auth.authenticate(email=payload.email, password=payload.password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return TokenOut(access_token=token)