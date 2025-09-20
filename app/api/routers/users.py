from fastapi import APIRouter
from app.controller import user_controller
from app.schemas.user import UserOut
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

router.get("", response_model=List[UserOut])(user_controller.index)
router.get("/{user_id}", response_model=UserOut)(user_controller.show)
router.patch("/{user_id}", response_model=UserOut)(user_controller.update)
router.delete("/{user_id}")(user_controller.delete)
router.post("/{user_id}/restore")(user_controller.restore)
router.delete("/{user_id}/force")(user_controller.force_delete)