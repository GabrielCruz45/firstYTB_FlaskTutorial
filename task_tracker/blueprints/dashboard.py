from flask import Blueprint, render_template, redirect, session, url_for

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    # get the username used in the session

    # check how "username" works
    if "username" in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('index'))