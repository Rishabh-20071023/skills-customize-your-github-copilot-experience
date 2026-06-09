# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a FastAPI REST API that handles HTTP requests, validates JSON data, and returns structured responses for a simple item collection.

## 📝 Tasks

### 🛠️ Define the API Structure

#### Description

Set up a FastAPI application and create endpoints for working with item resources.

#### Requirements
Completed program should:

- Import `FastAPI` and create an application instance.
- Define a Pydantic model for item data.
- Add endpoints for:
  - `GET /items`
  - `GET /items/{item_id}`
  - `POST /items`
  - `PUT /items/{item_id}`
  - `DELETE /items/{item_id}`
- Return JSON responses for each endpoint.

### 🛠️ Validate Request Data

#### Description

Use Pydantic models to validate incoming JSON and ensure the API accepts only correctly formatted item data.

#### Requirements
Completed program should:

- Define separate request and response models if needed.
- Validate required fields such as `name`, `description`, and `price`.
- Return validation errors for invalid input.
- Preserve the item data format across requests and responses.

### 🛠️ Test API Behavior

#### Description

Run the FastAPI application and verify that all endpoints work correctly using the built-in documentation or sample HTTP requests.

#### Requirements
Completed program should:

- Start the application with a Uvicorn server.
- Use `/docs` or `/redoc` to explore the API.
- Confirm that GET, POST, PUT, and DELETE requests return the expected JSON results.
- Handle missing items with a clear error response.
