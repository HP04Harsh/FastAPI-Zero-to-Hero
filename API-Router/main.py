from fastapi import FastAPI
from routes.order import router as order_router

app = FastAPI(title="Modular FastAPI App")

app.include_router(order_router)