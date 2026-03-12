from celery import Celery
from app.core.config import settings


celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery_app.conf.beat_schedule = {
    "fetch_prices_every_minute": {
        "task": "app.workers.tasks.fetch_prices",
        "schedule": 60.0,
    }
}