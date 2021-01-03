from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException

from app.models import Todo, AllTodos
from app.services import add_todo, delete_todo, list_all_todos

app = FastAPI()


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
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")