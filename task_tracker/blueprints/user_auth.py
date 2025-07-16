from flask import Blueprint, render_template, request, redirect, session, url_for
from .. import db
from ..models import Todo
from sqlalchemy import select # query-building toolkit
from flask_sqlalchemy import SQLAlchemy # provides the session to execute those queries
from werkzeug.security import generate_password_hash, check_password_hash


user_auth_bp = Blueprint('user_auth', __name__)

@user_auth_bp.route('/user_auth')
def user_auth():
    if "username" in session: # checks if user is logged in
        return redirect(url_for("dashboard.html"))
    
    return render_template("user_auth.html")