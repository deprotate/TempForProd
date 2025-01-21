from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from core.models.Promo import Promo
from promos.schemas import PromoCreate


async def create_promo(session: AsyncSession, promo_data: PromoCreate) -> Promo:
    promo = Promo(**promo_data.dict())
    session.add(promo)
    await session.commit()
    await session.refresh(promo)
    return promo


async def get_promo(session: AsyncSession, promo_id: int) -> Promo | None:
    result = await session.execute(select(Promo).where(Promo.id == promo_id))
    return result.scalars().first()


async def update_promo(session: AsyncSession, promo_id: int, promo_data: dict) -> Promo | None:
    await session.execute(
        update(Promo).where(Promo.id == promo_id).values(**promo_data)
    )
    await session.commit()
    return await get_promo(promo_id)


async def delete_promo(session: AsyncSession, promo_id: int) -> bool:
    result = await session.execute(delete(Promo).where(Promo.id == promo_id))
    await session.commit()
    return 0 < bool(result.rowcount)


async def get_promos(session: AsyncSession, limit: int, offset: int, category: str):
    query = select(Promo).where(Promo.category == category).limit(limit).offset(offset)
    result = await session.execute(query)
    return result.scalars().all()



