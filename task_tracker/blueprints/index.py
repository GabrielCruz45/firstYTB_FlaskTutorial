from flask import Blueprint, render_template, redirect, session, url_for


index_bp = Blueprint('index', __name__)

@index_bp.route('/index')
def index():
    if "username" in session: # checks if user is logged in 
        # (i.e. if the key-value pair "username" : "aactual-username" was added to the session dictionary)
        return redirect(url_for("dashboard"))
    
    return render_template("index.html")