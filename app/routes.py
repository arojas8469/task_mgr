from flask import Flask, request
from app.database import task

app = Flask(__name__)

# ReST - Representational State Transfer
# ReST - is an achitectural design pattern for building network-connected services.


@app.get("/")
@app.get("/task")
def get_tasks():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out

@app.get("/task/<int:pk>/")
def get_single_task(pk):
    out = {
        "task": task.select_by_id(pk),
        "ok": True
    }
    return out

@app.post("/task")
def create_task():
    task.create_task(request.json)
    return "", 204

@app.put("/tasks/<int:pk>/")
def update_task(pk):
    task.update_task_by_id(request.json, pk)
    return "", 204

@app.delete("/task/<int:pk>/")
def delete_task(pk):
    task.delete_task_by_id(pk)
    return "", 204


