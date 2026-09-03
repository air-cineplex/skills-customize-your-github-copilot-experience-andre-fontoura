from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = ""
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks = [
    Task(id=1, title="Write essay", description="Draft the introduction", completed=False),
    Task(id=2, title="Review notes", description="Study for the quiz", completed=True),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


@app.get("/tasks")
def get_tasks():
    return tasks


# TODO: Add a route to get one task by id.
# TODO: Add a route to create a new task.
# TODO: Add a route to update an existing task.
# TODO: Add a route to delete a task.
