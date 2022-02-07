from typing import Optional
from fastapi import FastAPI
from database import TodoList

app = FastAPI()
todoList = TodoList()

todoList.initialize()
todoList.connect()
todoList.open()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/todos")
def read_todos():

    sql = "SELECT * FROM `todo`;"
    return todoList.select(sql)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}