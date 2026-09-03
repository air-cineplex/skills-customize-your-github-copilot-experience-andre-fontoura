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


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_task = Task(
        id=max((item.id for item in tasks), default=0) + 1,
        **task.model_dump(),
    )
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskCreate):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = Task(id=task_id, **task_update.model_dump())
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
