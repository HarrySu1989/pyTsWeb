from flask import Blueprint, jsonify, request
import glb.ViewBase
from .Testing import Testing,Values
bp = Blueprint('flow', __name__, url_prefix='/flow')


@bp.route('/', methods=['GET', 'POST'])
def index():
  q = request.args.get('q')
  values=Values(q)
  testing = values.get_testing()
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

  <div ><h1 id="s_flow_log">{testing.s_flow_log}</h1></div>

  </section>
  <main class="form-signin w-100 m-auto">
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="flow_input_ip" value="{values.flow_input_ip}">
				<label for="floatingInput">IP</label>
			</div>
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="flow_input_order" value="{values.flow_input_order}">
				<label for="floatingInput">工单</label>
			</div>
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="flow_input_operator" value="{values.flow_input_operator}" readonly>
				<label for="floatingInput">测试员</label>
			</div>
			<div class="form-floating">
				<input  name="username" type="username" class="form-control" id="flow_input_sec" value="{values.flow_input_sec}">
				<label for="floatingInput">测试时间（分钟）</label>
			</div>
    <button id="button-flow-begin" class="btn btn-secondary w-100 py-2">开始</button>
	</main>
  <script src="/static/jquery-3.6.0.min.js"></script>
  <script src="/static/flow.js"></script>
"""

  # <a href="{url_for('flow.test1')}”>测试1</a>
  return glb.ViewBase.get_view(bp, html)


@bp.route('/update', methods=['POST'])
def update():
  data = request.json  # 获取Ajax请求发送的JSON数据
  s_flow_type = data.get('s_flow_type')
  values = Values(data.get('s_flow_values'))
  testing=values.get_testing()
  testing.values=values
  new_content=f'{testing.get_value(s_flow_type)}'
  response = {'message': 'Error1', 'new_content': new_content}  # 模拟处理并返回新内容

  return jsonify(response)  # 将响应数据封装为JSON格式返回
