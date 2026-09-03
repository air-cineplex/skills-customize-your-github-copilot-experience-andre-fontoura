# 📘 Assignment: Building REST APIs with FastAPI Framework

## 🎯 Objective

Build a small REST API that manages tasks or books using FastAPI. Students will learn how to define routes, validate request data with Pydantic models, and return JSON responses from a simple backend service.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a new FastAPI application and create a simple home route that confirms the API is running.

#### Requirements
Completed program should:

- Install and import `fastapi` and `uvicorn`.
- Create an `app = FastAPI()` instance.
- Add a `GET /` route that returns a JSON message such as `"message": "Welcome to the Task API"`.
- Run the app locally with `uvicorn`.

### 🛠️ Build Task Endpoints

#### Description
Create endpoints for managing a list of tasks with a simple in-memory database.

#### Requirements
Completed program should:

- Define a `Task` model with fields like `id`, `title`, `description`, and `completed`.
- Create a `GET /tasks` endpoint that returns all tasks.
- Create a `GET /tasks/{task_id}` endpoint that retrieves one task by ID.
- Create a `POST /tasks` endpoint that accepts a new task and adds it to the list.
- Return JSON responses in a consistent format.
- Validate required values such as a non-empty title.

### 🛠️ Add Update and Delete Behavior

#### Description
Extend the API so it can update or remove tasks while handling missing records gracefully.

#### Requirements
Completed program should:

- Add a `PUT /tasks/{task_id}` endpoint to replace an existing task.
- Add a `DELETE /tasks/{task_id}` endpoint to remove a task.
- Return `404` when a task ID does not exist.
- Use response models or clear JSON messages for success and error cases.
- Test the API using browser requests or a tool such as Postman or curl.

