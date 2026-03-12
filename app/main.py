from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Crypto Price Service")

app.include_router(router)