import asyncio
import json
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

# Async Helper Functions
async def fetch_weather():
    await asyncio.sleep(1) # Simulate API delay
    return {"temp": "30 C", "condition": "Sunny"}

async def fetch_hotels():
    await asyncio.sleep(1) # Simulate API delay
    return [{"name": "Taj Hotel", "price_per_night": 5000}]

# 1. Parallel Aggregation Endpoint (asyncio.gather)
@app.get("/plan/quick")
async def plan_trip_parallel():
    # Both APIs execute simultaneously in 1 second instead of 2 seconds!
    weather, hotels = await asyncio.gather(
        fetch_weather(),
        fetch_hotels()
    )
    return {"weather": weather, "hotels": hotels}


# 2. SSE Stream Endpoint (Server-Sent Events)
async def event_generator():
    messages = ["Searching flights...", "Finding best hotels...", "Checking weather...", "Trip Plan Ready!"]
    for msg in messages:
        await asyncio.sleep(1)
        # SSE Format: data: <json>\n\n
        yield f"event: update\ndata: {json.dumps({'message': msg})}\n\n"

@app.get("/plan/stream")
async def stream_trip_plan():
    return StreamingResponse(event_generator(), media_type="text/event-stream")