# init_db.py
import asyncio
from app.db.session import init_models

asyncio.run(init_models())
print("✅ Таблицы созданы")