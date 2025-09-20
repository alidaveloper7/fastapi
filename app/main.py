from __future__ import annotations
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.routers import auth as auth_router
from app.api.routers import users as users_router
from app.middlewares.error_handler import ErrorHandlingMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield

app = FastAPI(title=settings.app_name, lifespan=lifespan)

# Middlewares
app.add_middleware(ErrorHandlingMiddleware)

# Routers
app.include_router(auth_router.router)
app.include_router(users_router.router)

# Health
@app.get("/health", tags=["meta"])
async def health():
    return {"status": "ok"}
