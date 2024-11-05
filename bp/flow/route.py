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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from datetime import datetime, timedelta
import time

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
      return f"{self.log}"
    if req==0:
      self.t = threading.Thread(target=self.thred_run)
      self.t.start()
      self.log = "开始"
      self.sq_end=False
      self.count = 0
    return self.log

  def thred_run(self):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1200,1000")
    service = Service('./bp/flow/chromedriver-130.0.6723.91.exe')
    driver = webdriver.Chrome(options=chrome_options, service=service)
    try:
      url = 'http://10.77.77.108/'
      self.log = f"正在加载URL：{url}"
      try:
        driver.get(url)
      except:
        self.log = f"测试结束(无法加载URL：{url})"
        return
      b_load = True
      try:
        element = WebDriverWait(driver, 5).until(
          EC.visibility_of_element_located((By.ID, 'button-1051-btnInnerEl'))
        )
      except TimeoutException:
        b_load = False
      if not b_load:
        self.log = "测试结束(等待超时，网页加载异常)"
        return
      self.log = "测试结束(完成)"
      bt_begin = driver.find_element(By.ID,'button-1051-btnInnerEl')
      if bt_begin.text != "开始":
        self.log = f"{url}测试被占用"
        return
      if bt_begin.text != "开始":
        self.log = "测试结束(开始按钮未识别！！！)"
        return
      time_begin=datetime.now()-timedelta(seconds=30)
      bt_begin.click()
      time.sleep(2)
      while bt_begin.text != "开始":
        self.log = f"等待测试完成"
        time.sleep(1)
    except Exception as e:
      self.log = f"测试结束(异常退出)"
    finally:
        driver.quit()



    # while True:
    #   self.count += 1
    #   sleep(1)
    #   if self.count >20:
    #     self.log = "测试结束(完成)"
    #     return
    #   if self.sq_end:
    #     self.log = "测试结束(中断)"
    #     self.count = 0
    #     return


test = ClsTest()


@bp.route('/update', methods=['POST'])
def update():
  data = request.json  # 获取Ajax请求发送的JSON数据
  req = data.get('count')
  # response = {'message': 'Success', 'new_content': '这是更新后的内容'}  # 模拟处理并返回新内容
  global test
  response = {'message': 'Error1', 'new_content': f'{test.get_value(req)}'}  # 模拟处理并返回新内容

  return jsonify(response)  # 将响应数据封装为JSON格式返回
