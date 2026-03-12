from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.models import Price
from app.db.session import SessionLocal


router = APIRouter()


@router.get("/prices")
async def get_prices(ticker: str, session: AsyncSession = Depends(SessionLocal)):

    result = await session.execute(
        select(Price).where(Price.ticker == ticker)
    )

    return result.scalars().all()


@router.get("/price/latest")
async def get_latest_price(ticker: str, session: AsyncSession = Depends(SessionLocal)):

    result = await session.execute(
        select(Price)
        .where(Price.ticker == ticker)
        .order_by(Price.timestamp.desc())
        .limit(1)
    )

    return result.scalar_one_or_none()


@router.get("/price/by-date")
async def get_by_date(
    ticker: str,
    start: int,
    end: int,
    session: AsyncSession = Depends(SessionLocal)
):

    result = await session.execute(
        select(Price).where(
            Price.ticker == ticker,
            Price.timestamp >= start,
            Price.timestamp <= end
        )
    )

    return result.scalars().all()