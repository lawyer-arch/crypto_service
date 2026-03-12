import asyncio
import time

from app.deribit_client.client import DeribitClient
from app.db.models import Price
from app.db.session import SessionLocal
from .celery_app import celery_app


@celery_app.task
def fetch_prices():

    async def run():

        tickers = ["btc_usd", "eth_usd"]

        async with SessionLocal() as session:

            client = DeribitClient()

            for ticker in tickers:

                price = await client.get_index_price(ticker)

                obj = Price(
                    ticker=ticker,
                    price=price,
                    timestamp=int(time.time())
                )

                session.add(obj)

            await session.commit()

    asyncio.run(run())