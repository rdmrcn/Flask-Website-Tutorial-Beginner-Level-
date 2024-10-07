from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Task

views = Blueprint("views", __name__)

@views.route("/")
def home():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@views.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    date = request.form.get("date")
    if task and date:
        new_task = Task(task=task, date=date)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("views.home"))

@views.route("/complete/<int:task_id>")
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.done = True
        db.session.commit()
    return redirect(url_for("views.home"))
