from flask import redirect, url_for
from flask_login import current_user
from functools import wraps

def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for("dashboard.home"))
        return f(*args, **kwargs)
    return decorated_function