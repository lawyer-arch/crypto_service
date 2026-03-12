from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models import Prices
from app.db.session import SessionLocal


router = APIRouter()


async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


@router.get("/prices")
async def get_prices(ticker: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Prices).where(Prices.ticker == ticker)
    )
    return result.scalars().all()


@router.get("/price/latest")
async def get_latest_price(ticker: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Prices)
        .where(Prices.ticker == ticker)
        .order_by(Prices.timestamp.desc())
        .limit(1)
    )
    return result.scalar_one_or_none()


@router.get("/price/by-date")
async def get_by_date(
    ticker: str,
    start: int,
    end: int,
    session: AsyncSession = Depends(get_session)
):
    result = await session.execute(
        select(Prices).where(
            Prices.ticker == ticker,
            Prices.timestamp >= start,
            Prices.timestamp <= end
        )
    )
    return result.scalars().all()