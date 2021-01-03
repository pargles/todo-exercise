import uvicorn
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.models import Todo, AllTodos
from app.services import add_todo, delete_todo, list_all_todos

app = FastAPI()

# to make the frontend available
app.mount("/views", StaticFiles(directory="app/views"), name="views")

# to allow localhost requests
origins = [
    "http://localhost:5000",
    "http://127.0.0.1:5000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"health": "all good!"}


@app.post("/todos")
def create_todo(todo: Todo):
    try:
        persisted_todo = add_todo(todo)
        return persisted_todo
    except Exception as error:
        raise HTTPException(status_code=409, detail=str(error))


@app.delete("/todos/{todo_id}")
def remove_todo(todo_id: str):
    try:
        deleted_todo: Todo = delete_todo(int(todo_id))
        return deleted_todo
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


@app.get("/todos")
def list_todos(includeMissingTodos: Optional[bool] = False):
    try:
        all_todos: AllTodos = list_all_todos(includeMissingTodos)
        return all_todos
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000, log_level="info")
