# Crypto Price Service
___Сервис для сбора и предоставления цен на криптовалюты с биржи Deribit.___

Требования
```
Python 3.11+

PostgreSQL 12+

Redis 6+

Poetry (для управления зависимостями)
```

### Подготовка окружения:
1. Клонирование репозитория

```
git clone https://github.com/lawyer-arch/crypto_service.git
cd crypto_service

```
2. Создание виртуального окружения и установка зависимостей

```
poetry install
```
Активируйте виртуальное окружение:
```
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate  # Windows
```

### Настройка конфигурации
1. Создание файла окружения\
Скопируйте пример файла конфигурации:

```
cp .env.example .env
```
2. Редактирование .env
Отредактируйте файл .env, указав актуальные параметры вашей БД и Redis:
```
POSTGRES_USER="your_username"
POSTGRES_PASSWORD="your_password"
POSTGRES_DB="crypto_prices"
POSTGRES_HOST="localhost"
POSTGRES_PORT=5432
DATABASE_URL=postgresql://your_username:your_password@localhost:5432/crypto_prices
REDIS_URL=redis://localhost:6379/0
```

### Настройка базы данных
1. Запуск PostgreSQL

2. Создание базы данных (если не существует)\
Подключитесь к PostgreSQL и создайте БД:

```
CREATE DATABASE crypto_prices;
```
или через командную строку
```
createdb crypto_prices
```
3. Создание таблиц
Запустите скрипт инициализации БД:

```
poetry run python app/db/init_db.py
```

### Запуск сервисов
1. Запуск Redis\
Убедитесь, что Redis запущен:
```
docker run -d --name redis-crypto -p 6379:6379 redis:7-alpine
```

2. Запуск Celery Worker и Beat\
Откройте отдельное окно терминала в папке проекта\
Перейдите в директорию app:
```
cd app
```
и выполните:
```
poetry run celery -A app.celery_worker.celery_app worker -B --loglevel=info
```

3. Запуск FastAPI приложения\
Откройте ещё одно окно терминала и выполните:
```
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Приложение будет доступно по адресу: http://localhost:8000

## Структура проекта:
.crypto_service
├── app
│   ├── api
│   │   ├── __pycache__
│   │   │   └── routes.cpython-312.pyc
│   │   └── routes.py
│   ├── celerybeat-schedule
│   ├── celery_worker
│   │   ├── celery_app.py
│   │   ├── __pycache__
│   │   │   ├── celery_app.cpython-312.pyc
│   │   │   └── tasks.cpython-312.pyc
│   │   └── tasks.py
│   ├── core
│   │   ├── config.py
│   │   └── __pycache__
│   │       └── config.cpython-312.pyc
│   ├── db
│   │   ├── init_db.py
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── models.cpython-312.pyc
│   │   │   └── session.cpython-312.pyc
│   │   └── session.py
│   ├── deribit_client
│   │   ├── client.py
│   │   └── __pycache__
│   │       └── client.cpython-312.pyc
│   ├── __init__.py
│   ├── main.py
│   └── __pycache__
│       ├── __init__.cpython-312.pyc
│       └── main.cpython-312.pyc
├── poetry.lock
├── pyproject.toml
└── README.md