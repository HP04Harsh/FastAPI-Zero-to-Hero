from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, create_engine, Session, select
from fastapi import FastAPI, Depends

# Database Engine Setup
sqlite_url = "sqlite:///./app.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# Database Model
class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movie_name: str
    rating: int
    review_text: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

SQLModel.metadata.create_all(engine)

# DB Session Dependency
def get_db():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.post("/reviews/", response_model=Review)
async def create_review(review: Review, db: Session = Depends(get_db)):
    db.add(review)
    db.commit()
    db.refresh(review)
    return review