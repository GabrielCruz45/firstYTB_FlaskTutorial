from flask import Blueprint, render_template, request, redirect, session, url_for
from .. import db
from ..models import Users


register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    # collect user input
    username = request.form['username']
    password = request.form['password']
    user = Users.query.filter_by(username=username).first()

    # check if the user is NOT already in the database
    if user:
        return render_template("index.html", error="User already registered")
    
    else:
        # if not on db, create user with user input
        new_user = Users(username=username)
        new_user.set_password(password)

        # add new object to db, and fully commit
        db.session.add(new_user)
        db.session.commit()

        # log in user to new session and redirect
        session['username'] = username
        session.permanent = True # creates cookie for mantaining logged in status
        return redirect(url_for('dashboard.dashboard'))
    pass