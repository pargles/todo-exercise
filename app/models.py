from typing import List, Optional

from pydantic import BaseModel, validator


class Todo(BaseModel):
    name: str
    priority: int

    @validator('name')
    def name_cannot_be_empty(cls, value):
        if len(value) <= 0:
            raise ValueError('todo cannot be empty')
        return value

    @validator('priority')
    def priority_bigger_than_zero(cls, value):
        if value <= 0:
            raise ValueError('priority needs to be bigger than 0')
        return value


class AllTodos(BaseModel):
    current: List
    missing: Optional[List] = []
