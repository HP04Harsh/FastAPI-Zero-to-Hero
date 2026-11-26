# FastAPI: Zero to Hero

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Learning-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

A practical collection of small FastAPI applications for learning APIs, validation, routing, async programming, databases, file uploads, and AI integration. Each folder is independent and can be run with Uvicorn.

> This is an educational repository. Demo credentials, local database settings, and simplified file handling should not be used unchanged in production.

## What You'll Learn

- Build FastAPI applications and expose interactive API documentation
- Validate path and query parameters
- Return HTTP errors and response models
- Organize endpoints with `APIRouter`
- Reuse logic with FastAPI dependencies
- Run concurrent async operations
- Stream responses with Server-Sent Events
- Upload and serve files
- Create SQLite records with SQLModel
- Connect to MongoDB with PyMongo
- Send an image to a Groq vision model

## Examples

| Module | Topics | Main endpoints |
| --- | --- | --- |
| [`FastAPI-Foundation`](FastAPI-Foundation) | Lifespan events and app metadata | `/docs` |
| [`FastAPI-Codes`](FastAPI-Codes) | Path parameters and HTTP errors | `GET /pincode/{code}` |
| [`FastAPI-Query,PathandOthers`](FastAPI-Query,PathandOthers) | Query parameters and Pydantic models | `GET /` |
| [`API-Router`](API-Router) | Modular routes with `APIRouter` | `GET /order/order` |
| [`Depends`](Depends) | Headers and reusable dependencies | `GET /admin/chai-stats` |
| [`Async&Stream`](Async&Stream) | `asyncio.gather` and SSE streaming | `GET /plan/quick`, `GET /plan/stream` |
| [`FileUpload`](FileUpload) | Multipart uploads and static files | `POST /upload/file`, `GET /uploads/{filename}` |
| [`Database/rdbms.py`](Database/rdbms.py) | SQLModel and SQLite | `POST /reviews/` |
| [`Database/mongo.py`](Database/mongo.py) | PyMongo and MongoDB | `POST /contracts/` |
| [`AI Integration`](AI%20Integration) | Image resizing, encoding, and Groq vision | `POST /ai/vision-analyze` |

## Prerequisites

- Python 3.10 or later
- `pip`
- MongoDB running locally for the MongoDB example
- A Groq API key for the AI vision example

## Installation

Clone the repository and create an isolated environment from the project root:

```powershell
git clone https://github.com/HP04Harsh/FastAPI-Zero-to-Hero.git
cd FastAPI-Zero-to-Hero
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirement.txt
```

Install the optional packages used by the database and AI examples:

```powershell
pip install sqlmodel pymongo pillow groq python-multipart
```

## Run the Examples

Run each command from the repository root. Replace the module path to explore a different app.

### Standard apps

```powershell
python -m uvicorn main:app --reload --app-dir "FastAPI-Foundation" --port 8484
python -m uvicorn main:app --reload --app-dir "FastAPI-Codes"
python -m uvicorn main:app --reload --app-dir "FastAPI-Query,PathandOthers"
python -m uvicorn main:app --reload --app-dir "API-Router"
python -m uvicorn main:app --reload --app-dir "Depends"
python -m uvicorn main:app --reload --app-dir "Async&Stream"
python -m uvicorn main:app --reload --app-dir "FileUpload"
python -m uvicorn main:app --reload --app-dir "AI Integration"
```

The default server address is `http://127.0.0.1:8000`. Open `/docs` to try endpoints interactively.

> The foundation example uses port `8484`, so open `http://127.0.0.1:8484/docs`.

### Database apps

```powershell
python -m uvicorn rdbms:app --reload --app-dir "Database"
python -m uvicorn mongo:app --reload --app-dir "Database"
```

## Quick API Examples

Pincode lookup:

```text
GET /pincode/411001
GET /pincode/400001
GET /pincode/110001
```

Dependency example:

```text
GET /admin/chai-stats?skip=0&limit=10
X-API-Key: secret-chai-123
```

SQL review example:

```json
POST /reviews/

{
  "movie_name": "Arrival",
  "rating": 5,
  "review_text": "A thoughtful and engaging film."
}
```

MongoDB contract example:

```text
POST /contracts/?title=Sample&content=Example
```

The async, file upload, and AI endpoints are easiest to test from Swagger UI at `/docs`, where uploaded files can be submitted as multipart form data.

## Configuration

Set a Groq API key as an environment variable before running the AI example:

```powershell
$env:GROQ_API_KEY="your-api-key"
python -m uvicorn main:app --reload --app-dir "AI Integration"
```

Never commit API keys or other secrets. The MongoDB example expects the default local connection:

```text
mongodb://localhost:27017
```

## Project Notes

- `Database/rdbms.py` creates `app.db` in the current working directory.
- `Database/mongo.py` uses the local database `contractDB`.
- `FileUpload/main.py` stores uploaded files in `uploads/`.
- `Depends/main.py` uses a demo API key for learning only.
- `AI Integration/main.py` requires an image and returns JSON analysis fields.
- Add authentication, strict file validation, limits, logging, and secure secret management before deploying.

## Contributing

Contributions are welcome. Keep examples small and focused, follow the existing folder structure, and document any new endpoint or dependency in this README.
