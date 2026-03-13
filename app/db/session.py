from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from .models import Base


engine_sync = create_engine(settings.DATABASE_URL)

SessionLocalSync = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_sync
)


def init_models_sync():
    # синхронно создаём таблицы один раз
    Base.metadata.create_all(bind=engine_sync)