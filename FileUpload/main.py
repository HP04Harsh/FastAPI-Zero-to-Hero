import os
import uuid
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Mount Static Files Directory (e.g., http://localhost:8000/uploads/xyz.jpg)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

@app.post("/upload/file")
async def upload_document(file: UploadFile = File(...)):
    # 1. Extension check
    allowed_types = ["image/jpeg", "image/png", "application/pdf"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file format!")

    # 2. Unique name create karo
    ext = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4().hex}.{ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # 3. Read & Save File Bytes
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    return {
        "status": "success",
        "original_name": file.filename,
        "saved_path": f"/uploads/{unique_filename}",
        "file_size_bytes": len(contents)
    }