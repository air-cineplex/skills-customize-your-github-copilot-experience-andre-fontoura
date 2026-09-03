# 📘 Assignment: Testing FastAPI APIs with pytest

## 🎯 Objective

Write automated tests for a FastAPI task API using pytest and FastAPI's TestClient. You will learn how to check successful responses, validate request data, and verify that an API handles missing resources correctly.

## 📝 Tasks

### 🛠️ Set Up the Test Environment

#### Description
Install the testing dependencies and create a test file that can send requests to the FastAPI application without starting a separate server.

#### Requirements
Completed program should:

- Install `pytest`, `fastapi`, and `httpx` in the project environment.
- Create a `test_api.py` file.
- Import the `app` object from `starter_code.py`.
- Create a `TestClient` for the application.
- Run the test suite with `pytest`.

### 🛠️ Test Successful API Requests

#### Description
Test the API's normal behavior for reading and creating tasks. Each test should verify both the HTTP status code and important values in the JSON response.

#### Requirements
Completed program should:

- Test that `GET /` returns status `200` and the expected welcome message.
- Test that `GET /tasks` returns status `200` and a JSON list.
- Test that `GET /tasks/1` returns the task with ID `1`.
- Test that `POST /tasks` accepts a valid task and returns status `201` or the status documented by the API.
- Use assertions that check response data rather than only checking that a request does not crash.

### 🛠️ Test Validation and Error Handling

#### Description
Add tests for requests that should fail. These tests protect the API contract by confirming that invalid input and unknown task IDs receive predictable error responses.

#### Requirements
Completed program should:

- Test that requesting an unknown task ID returns status `404`.
- Test that creating a task with an empty title is rejected with a client-error status such as `422`.
- Test that updating an unknown task ID returns status `404`.
- Test that deleting an unknown task ID returns status `404`.
- Include at least one test that checks a useful detail from the error response.

### 🛠️ Stretch Goal: Isolate Test Data

#### Description
Make the tests repeatable by ensuring that one test's changes do not unexpectedly affect another test.

#### Requirements
Completed program should:

- Explain in a short comment or README note how test data is isolated.
- Use a fixture or another clear reset strategy when appropriate.
- Pass when the complete suite is run more than once.
