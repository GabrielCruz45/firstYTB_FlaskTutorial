from flask import Blueprint, render_template, request, redirect, session
from .. import db
from ..models import Task, User
from sqlalchemy import select


task_tracker_bp = Blueprint('task_tracker', __name__)

# --- Routes ---
# python decorator, tell your app to immediately trigger the following function 
# after the user navigates to the specified URL path
@task_tracker_bp.route('/', methods=["GET", "POST"])
# view function; Flask executes this function whenever the user visits '/'
def task_tracker():
    if request.method == "POST":
        task_content = request.form['task']
        new_task = Task(content=task_content)

        try:
            # db.session.add(new_task)
            # db.session.commit()
            return redirect('/')
        
        except:
            return "There was an error adding your task."
        
    else:
        print("GET")
        # Create a statement to select all tasks, ordered by their creation date
        statement = select(Task).where(User.username == session['username'])

        # Execute the statement and get all results as a list of Task objects
        tasks = session.scalars(statement).all()
        print(tasks)
        return render_template("index.html", tasks=tasks) # runs index.html with tasks arranged in creation order
