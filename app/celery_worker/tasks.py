from app.deribit_client.client import DeribitClient
from app.db.models import Prices
from app.db.session import SessionLocalSync
from app.celery_worker.celery_app import celery_app
import time

@celery_app.task
def fetch_prices():
    tickers = ["btc_usd", "eth_usd"]

    session = SessionLocalSync()
    try:
        client = DeribitClient()

        for ticker in tickers:
            price = client.get_index_price(ticker)

            obj = Prices(
                ticker=ticker,
                price=price,
                timestamp=int(time.time())
            )
            session.add(obj)

        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
