from flask import Blueprint, render_template, request, redirect
from .. import db
from ..models import Todo
from sqlalchemy import select


index_bp = Blueprint('task_tracker', __name__)

# --- Routes ---
# python decorator, tell your app to immediately trigger the following function 
# after the user navigates to the specified URL path
@index_bp.route('/', methods=["GET", "POST"])
# view function; Flask executes this function whenever the user visits '/'
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        
        except:
            return "There was an error adding your task."
        
    else:
        print("GET")
        # Create a statement to select all tasks, ordered by their creation date
        statement = select(Todo).order_by(Todo.date_created)

        # Execute the statement and get all results as a list of Todo objects
        tasks = db.session.scalars(statement).all()
        return render_template("index.html", tasks=tasks) # runs index.html with tasks arranged in creation order
