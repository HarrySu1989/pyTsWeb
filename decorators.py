from functools import wraps
from  flask import session,redirect,url_for



def login_required(func):
    # 保留func的信息
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = session.get("user_id")
        if username is None:
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return wrapper