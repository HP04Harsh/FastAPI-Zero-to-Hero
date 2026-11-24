from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    name: str = Field(..., min_length=5, max_length=20)
    age: int = Field(..., ge=10, lt=50)
    city: str = Field(..., min_length=1)


@app.get("/")
def get_student(student: Annotated[Student, Query()]):
    return student