from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from core.DbHelper import db_helper
from . import CRUD as crud

promos_router = APIRouter(prefix="/user")

@promos_router.get("/feed")
async def get_promos(
    limit: int = Query(10),
    offset: int = Query(0),
    category: str = Query(...),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_promos(session=session, limit=limit, offset=offset, category=category)
@promos_router.post("/create")
async def create_promo(
        promo_data: dict = Query(...),
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_promo(session=session, promo_data=promo_data)
