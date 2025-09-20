from fastapi import APIRouter
from app.controller import auth_controller
from app.schemas.user import UserOut
from app.schemas.auth import TokenOut

router = APIRouter(prefix="/auth", tags=["auth"])

router.post("/register", response_model=UserOut, status_code=201)(auth_controller.register)
router.post("/login", response_model=TokenOut)(auth_controller.login)