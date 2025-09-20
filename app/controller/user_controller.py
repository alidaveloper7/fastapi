from fastapi import Depends, HTTPException
from typing import List
from app.schemas.user import UserOut, UserUpdate
from app.core.container import get_user_service
from app.api.deps import get_current_user_id
from app.services.user_service import UserService

async def index(
    page: int = 1,
    per_page: int = 20,
    sort: str = "created_at",
    dir: str = "desc",
    svc: UserService = Depends(get_user_service),
    _user_id: str = Depends(get_current_user_id)
) -> List[UserOut]:
    return await svc.list(page=page, per_page=per_page, sort=sort, dir=dir)

async def show(
    user_id: str,
    svc: UserService = Depends(get_user_service),
    _uid=Depends(get_current_user_id)
) -> UserOut:
    user = await svc.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    return user

async def update(
    user_id: str,
    payload: UserUpdate,
    svc: UserService = Depends(get_user_service),
    _uid=Depends(get_current_user_id)
) -> UserOut:
    user = await svc.update(user_id, payload)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    return user

async def delete(
    user_id: str,
    svc: UserService = Depends(get_user_service),
    _uid=Depends(get_current_user_id)
):
    ok = await svc.soft_delete(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found or already deleted")
    return {"status": "deleted"}

async def restore(
    user_id: str,
    svc: UserService = Depends(get_user_service),
    _uid=Depends(get_current_user_id)
):
    ok = await svc.restore(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found or not deleted")
    return {"status": "restored"}

async def force_delete(
    user_id: str,
    svc: UserService = Depends(get_user_service),
    _uid=Depends(get_current_user_id)
):
    ok = await svc.force_delete(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return {"status": "force-deleted"}