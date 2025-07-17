from flask import Blueprint, render_template, request, redirect, session, url_for
from ..models import Users



login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    # collect info from the form
    username = request.form['username']
    password = request.form['password']

    # check if its int the db / login
    # create an obeject of the users.db in order to make a query
    user = Users.query.filter_by(username=username).first()
    if user and user.check_password(password):
        # if true, log user in
        session['username'] = username
        session.permanent = True # creates cookie for mantaining logged in status
        return redirect(url_for('dashboard'))
    
    # otherwise show homepage
    else:
        return render_template("index.html")