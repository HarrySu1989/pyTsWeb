from  flask import session
from datetime import datetime
def add(param):
  user = session.get("user_id")
  s_time=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
  return print(f"{s_time}\t[{user}]{param}")