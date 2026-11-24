from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("app start")
    yield
    print("app shutdown")

app = FastAPI(
    title="FastAPI Foundation",
    description="This is my fastapi learning course",
    lifespan=lifespan,
    version="1.0.0"
)    

if __name__== "__main__":
    uvicorn.run(app,host="127.0.0.1",port="8484")