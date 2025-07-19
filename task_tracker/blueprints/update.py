from flask import Blueprint, render_template, request, redirect
from .. import db
from ..models import Task

update_bp = Blueprint('update', __name__)

@update_bp.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    
    task = db.get_or_404(Task, id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        
        except:
            return 'There was an issue updating your task.'
        
    else:
        return render_template("update.html", task=task)