from flask import Blueprint, render_template, request, redirect
from .. import db
from ..models import Todo
from sqlalchemy import select

delete_bp = Blueprint('delete', __name__)

@delete_bp.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    
    except:
        return 'There was a problem to deleting that task'