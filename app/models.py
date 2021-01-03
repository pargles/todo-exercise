from typing import List, Optional

from pydantic import BaseModel


class Todo(BaseModel):
    name: str
    priority: int  # todo, validate non-negative numbers here


class AllTodos(BaseModel):
    current: List
    missing: Optional[List] = []
