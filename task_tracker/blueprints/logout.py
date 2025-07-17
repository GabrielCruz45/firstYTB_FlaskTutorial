from flask import Blueprint, redirect, session, url_for


# There's a list of users currently in session. In order to log them out, you just need to pop them off!
# ['bob', 'gabs', 'fulano', 'sultano', 'mengano']

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))