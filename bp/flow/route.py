from flask import Blueprint, jsonify, request
import glb.ViewBase
import os
from datetime import datetime
import time
from .Testing import Testing
import bp.flow.sql as sql

bp = Blueprint('flow', __name__, url_prefix='/flow')


@bp.route('/', methods=['GET', 'POST'])
def index():
  q = request.args.get('q')
  s_ip=""
  s_order=""
  s_user=""
  s_sec="1"
  if q:
    buf=q.split(',')
    s_ip=buf[0]
    s_order=buf[1]
    s_user=buf[2]
    s_sec=buf[3]
    print(s_ip)
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

  <div ><h1 id="s_flow_log">{test.s_flow_log}</h1></div>

  </section>
  <main class="form-signin w-100 m-auto">
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="flow_input_ip" value="{s_ip}">
				<label for="floatingInput">IP</label>
			</div>
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="flow_input_order" value="{s_order}">
				<label for="floatingInput">工单</label>
			</div>
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="flow_input_operator" value="{s_user}" readonly>
				<label for="floatingInput">测试员</label>
			</div>
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="flow_input_sec" value="{s_sec}">
				<label for="floatingInput">测试时间（分钟）</label>
			</div>
    <button id="button-flow-begin" class="btn btn-secondary w-100 py-2">开始</button>
	</main>
  <script src="/static/jquery-3.6.0.min.js"></script>
  <script src="/static/flow.js"></script>
"""

  # <a href="{url_for('flow.test1')}”>测试1</a>
  return glb.ViewBase.get_view(bp, html)

test = Testing()
# http://192.168.8.146:5000/flow/test/open
@bp.route('/test/open')
def open_test():
  if not test.element_driver():return
  # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
  project_root = os.path.join(os.path.dirname(__file__))
  print(project_root)
  url = f"{project_root}/LyApp.mhtml"
  test.driver.get(url)
  time.sleep(1)
  time_a = datetime.strptime(f"2024-11-04 17:00:12", "%Y-%m-%d %H:%M:%S")
  df = test.element_df(time_a)
  print(df)
  print(df.columns)
  dict_value={"flow_input_operator":"harry","flow_input_order":"20110101001"}
  sql.set_insert(df,dict_value)
  return glb.ViewBase.get_view(bp, "open")

@bp.route('/update', methods=['POST'])
def update():
  data = request.json  # 获取Ajax请求发送的JSON数据
  s_flow_type = data.get('s_flow_type')
  s_flow_values = data.get('s_flow_values')
  # response = {'message': 'Success', 'new_content': '这是更新后的内容'}  # 模拟处理并返回新内容
  global test
  response = {'message': 'Error1', 'new_content': f'{test.get_value(s_flow_type,s_flow_values)}'}  # 模拟处理并返回新内容

  return jsonify(response)  # 将响应数据封装为JSON格式返回
