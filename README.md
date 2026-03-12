# Crypto Price Service
Клиент для криптобиржи. Парсит цены.


Один раз:

```
poetry run python -c "import asyncio; from app.db.session import init_models; asyncio.run(init_models())"
```