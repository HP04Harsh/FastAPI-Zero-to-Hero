from pymongo import MongoClient
from fastapi import FastAPI

client = MongoClient("mongodb://localhost:27017")
db = client["wakeel_db"]
contracts_collection = db["contracts"]

app = FastAPI()

@app.post("/contracts/")
async def save_contract(title: str, content: str):
    doc = {"title": title, "content": content, "status": "draft"}
    result = contracts_collection.insert_one(doc)
    return {"inserted_id": str(result.inserted_id), "status": "saved"}