from celery import Celery
from app.core.config import settings


celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

# регистрация задачи (ВАЖНО)
celery_app.autodiscover_tasks(["app.celery_worker"])

# настройка запроса каждые 60 секунд
celery_app.conf.beat_schedule = {
    "fetch_prices_every_minute": {
        "task": "app.celery_worker.tasks.fetch_prices",
        "schedule": 60.0,
    }
}
