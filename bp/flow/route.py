from flask import Blueprint, jsonify, request,session

from decorators import login_required
import glb.ViewBase as vb
import os
from datetime import datetime, timedelta
import time
from .Testing import Testing
import bp.flow.sql as sql

bp = Blueprint('flow', __name__, url_prefix='/flow')


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
  # <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>  <!-- 引入jQuery库 -->
  #
  # current_directory = os.path.dirname(os.path.realpath(__file__))
  # print(current_directory)
  s_style = """
          <style>
          html,
  body {
    height: 100%;
  }

  .form-signin {
    max-width: 330px;
    padding: 1rem;
  }

  .form-signin .form-floating:focus-within {
    z-index: 2;
  }

  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }

  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }

          </style>
          """
  html = f"""
  {s_style}
  <section class="py-5 text-center container">

  <div ><h1 id="div-flow-status">{test.log}</h1></div>

  </section>
  <main class="form-signin w-100 m-auto">
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="floatingInput">
				<label for="floatingInput">IP</label>
			</div>
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="floatingInput" value="test">
				<label for="floatingInput">工单</label>
			</div>
    <button id="button-flow-begin" class="btn btn-secondary w-100 py-2">开始</button>
	</main>
  <script src="/static/jquery-3.6.0.min.js"></script>
  <script src="/static/flow.js"></script>
"""

  # <a href="{url_for('flow.test1')}”>测试1</a>
  return vb.get_view(bp, html)

test = Testing()
# http://192.168.8.146:5000/flow/test/open
@bp.route('/test/open')
def open():
  if not test.element_driver():return
  # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
  project_root = os.path.join(os.path.dirname(__file__))
  print(project_root)
  url = f"{project_root}/LyApp.mhtml"
  test.driver.get(url)
  time.sleep(1)
  time_a = datetime.now()
  time_a = datetime.strptime(f"2024-11-04 17:00:12", "%Y-%m-%d %H:%M:%S")
  df = test.element_df(time_a)
  print(df)
  print(df.columns)
  user = session.get("user_id")
  sql.set_insert(df,user)
  return vb.get_view(bp, "open")

@bp.route('/update', methods=['POST'])
def update():
  data = request.json  # 获取Ajax请求发送的JSON数据
  req = data.get('count')
  # response = {'message': 'Success', 'new_content': '这是更新后的内容'}  # 模拟处理并返回新内容
  global test
  response = {'message': 'Error1', 'new_content': f'{test.get_value(req)}'}  # 模拟处理并返回新内容

  return jsonify(response)  # 将响应数据封装为JSON格式返回
