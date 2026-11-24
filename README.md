# FastAPI: Zero to Hero

A hands-on collection of small FastAPI examples, organized by topic. Each folder is a separate application you can run and explore independently. The examples cover routing, request validation, dependency injection, async work, streaming responses, file uploads, databases, and an AI vision integration.

> These examples are for learning. Demo credentials, local database settings, and simplified file handling are not production-ready.

## Contents

| Folder | What you'll learn | Example routes |
| --- | --- | --- |
| `FastAPI-Foundation` | App metadata and lifespan events | `/docs` |
| `FastAPI-Codes` | Path parameters, validation, and HTTP errors | `GET /pincode/{code}` |
| `FastAPI-Query,PathandOthers` | Query parameters and Pydantic models | `GET /` |
| `API-Router` | Splitting routes into modules with `APIRouter` | `GET /order/order` |
| `Depends` | Dependencies, headers, and pagination | `GET /admin/chai-stats` |
| `Async&Stream` | Concurrent async tasks and Server-Sent Events | `GET /plan/quick`, `GET /plan/stream` |
| `FileUpload` | Uploading and serving files | `POST /upload/file`, `GET /uploads/{filename}` |
| `Database` | SQLModel with SQLite and MongoDB with PyMongo | `POST /reviews/`, `POST /contracts/` |
| `AI Integration` | Image processing and a Groq vision API call | `POST /ai/vision-analyze` |

## Requirements

- Python 3.10 or later
- pip
- MongoDB running locally if you want to use `Database/mongo.py`
- A Groq API key if you want to use `AI Integration/main.py`

## Set up

From the project root, create and activate a virtual environment:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirement.txt
```

Some examples need additional packages not included in `requirement.txt`:

```powershell
pip install sqlmodel pymongo
pip install groq pillow
```

The file upload example uses multipart form data; installing `fastapi[standard]` from `requirement.txt` provides the required standard extras.

## Run an example

Run commands from the project root. Each command starts a different application on `http://127.0.0.1:8000` (the foundation example uses port `8484`):

```powershell
python -m uvicorn main:app --reload --app-dir "FastAPI-Foundation" --port 8484
python -m uvicorn main:app --reload --app-dir "FastAPI-Codes"
python -m uvicorn main:app --reload --app-dir "FastAPI-Query,PathandOthers"
python -m uvicorn main:app --reload --app-dir "API-Router"
python -m uvicorn main:app --reload --app-dir "Depends"
python -m uvicorn main:app --reload --app-dir "Async&Stream"
python -m uvicorn main:app --reload --app-dir "FileUpload"
```

The `Database` folder contains two separate apps, so start either one directly instead:

```powershell
python -m uvicorn rdbms:app --reload --app-dir "Database"
python -m uvicorn mongo:app --reload --app-dir "Database"
```

For any running app, open `http://127.0.0.1:8000/docs` to try its routes interactively. Use `http://127.0.0.1:8484/docs` for the foundation app.

### Example requests

- Pincode lookup: `GET /pincode/411001` (try `400001` or `110001` too).
- Router example: `GET /order/order`.
- Dependency example: `GET /admin/chai-stats?skip=0&limit=10`; include the demo header `X-API-Key: secret-chai-123`.
- Async examples: `GET /plan/quick` and `GET /plan/stream`.
- SQLModel example: `POST /reviews/` with JSON such as `{"movie_name":"Arrival","rating":5,"review_text":"Great film"}`.
- MongoDB example: `POST /contracts/?title=Sample&content=Example`; MongoDB must be available at `mongodb://localhost:27017`.
- File upload and AI vision routes accept an uploaded file; use the interactive docs to submit multipart form data.

## Notes

- `Database/rdbms.py` creates a local SQLite database named `app.db`.
- `FileUpload/main.py` writes uploaded files to an `uploads/` directory.
- `Depends/main.py` uses a hard-coded demonstration API key. Do not use it as real authentication.
- `AI Integration/main.py` contains a placeholder Groq API key. Configure a valid key before using the endpoint, and never commit real credentials.
- This repository is a learning project; validate uploads, handle credentials securely, and add production-grade error handling before deploying.
