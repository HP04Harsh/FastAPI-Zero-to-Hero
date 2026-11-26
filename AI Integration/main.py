import io
import base64
import json
import os
from PIL import Image
from fastapi import FastAPI, UploadFile, File, HTTPException
from groq import Groq

app = FastAPI()
groq_api_key = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=groq_api_key) if groq_api_key else None

@app.post("/ai/vision-analyze")
async def analyze_crop_photo(file: UploadFile = File(...)):
    if groq_client is None:
        raise HTTPException(
            status_code=503,
            detail="GROQ_API_KEY is not configured.",
        )

    # Step 1: Read Bytes
    contents = await file.read()

    # Step 2: PIL Image Processing (Resize if > 2048px)
    img = Image.open(io.BytesIO(contents))
    img.thumbnail((2048, 2048))
    
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    resized_bytes = buffer.getvalue()

    # Step 3: Base64 Encoding
    b64_string = base64.b64encode(resized_bytes).decode("utf-8")

    # Step 4: Groq Free Vision AI Call
    response = groq_client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this crop disease and return strict JSON with 'crop', 'disease', and 'treatment'."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{b64_string}"}
                    }
                ]
            }
        ]
    )

    return json.loads(response.choices[0].message.content)