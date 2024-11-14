import traceback
from datetime import datetime

from flask import session


def add_log(param):
  try:
    user = session.get("user_id")
    s_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    return print(f"{s_time}\t[{user}]{param}")
  except Exception as e:
    trace = traceback.format_exc()
    print(trace)


def add_log_b(param):
  try:
    s_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    return print(f"{s_time}\t{param}")
  except Exception as e:
    trace = traceback.format_exc()
    print(trace)
