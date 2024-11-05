from flask import Blueprint, render_template
from decorators import login_required
import glb.ViewBase as vb
import glb.uc as uc
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import threading
from time import sleep
from flask import Flask, render_template, jsonify, request

bp = Blueprint('flow', __name__, url_prefix='/flow')


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
# <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>  <!-- 引入jQuery库 -->
#
  # current_directory = os.path.dirname(os.path.realpath(__file__))
  # print(current_directory)

  html = f"""
  <div ><h3 id="div-flow-status">{test.log}</h3></div>
  <div>
    <label for="example-textbox">工单:</label>
    <input type="text" id="example-textbox" name="example-textbox">
    <button id="button-flow-begin">开始</button>
    <script src="/static/jquery-3.6.0.min.js"></script>
    <script src="/static/flow.js"></script>
  </div>
 
"""
  return vb.get_view(bp, html)


class ClsTest():
  def __init__(self):
    self.t = None
    self.count = 0
    self.sq_end=False
    self.log = "请录入工单，点击开始测试"

  def get_value(self, req):
    if self.t and self.t.is_alive():
      if req==0:
        return "当前流量仪正在测试"
      elif req==-1:
        self.sq_end=True
        return "结束申请"
      return f"{self.log}[{self.count}]"
    if req==0:
      self.t = threading.Thread(target=self.thred_run)
      self.t.start()
      self.log = "开始"
      self.sq_end=False
      self.count = 0
    return self.log

  def thred_run(self):
    while True:
      self.count += 1
      sleep(1)
      if self.count >20:
        self.log = "测试结束(完成)"
        return
      if self.sq_end:
        self.log = "测试结束(中断)"
        self.count = 0
        return


test = ClsTest()


@bp.route('/update', methods=['POST'])
def update():
  data = request.json  # 获取Ajax请求发送的JSON数据
  req = data.get('count')
  # response = {'message': 'Success', 'new_content': '这是更新后的内容'}  # 模拟处理并返回新内容
  global test
  response = {'message': 'Error1', 'new_content': f'{test.get_value(req)}'}  # 模拟处理并返回新内容

  return jsonify(response)  # 将响应数据封装为JSON格式返回
