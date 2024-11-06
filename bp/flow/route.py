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
import uc.uc_pd as pd
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
    self.driver = None

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

  def element_page(self):
    try:
      tab_log = self.driver.find_element(By.ID, 'tab-1379-btnInnerEl')
      tab_log.click()
      time.sleep(2)
    except:
      self.log = "测试结束(无法找到日志页面)"
      return
  def thred_run(self):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1200,1000")
    service = Service('./bp/flow/chromedriver-130.0.6723.91.exe')
    self.driver = webdriver.Chrome(options=chrome_options, service=service)
    try:
      url = 'http://10.77.77.108/'
      self.log = f"正在加载URL：{url}"
      try:
        self.driver.get(url)
      except:
        self.log = f"测试结束(无法加载URL：{url})"
        return
      b_load = True
      try:
        element = WebDriverWait(self.driver, 5).until(
          EC.visibility_of_element_located((By.ID, 'button-1051-btnInnerEl'))
        )
      except TimeoutException:
        b_load = False
      if not b_load:
        self.log = "测试结束(等待超时，网页加载异常)"
        return

      bt_begin = self.driver.find_element(By.ID,'button-1051-btnInnerEl')
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
        text_time = self.driver.find_element(By.ID,'component-1084')
        self.log = f"等待测试完成({text_time.text})"

        time.sleep(1)
        if self.sq_end:
          bt_begin.click()
          self.log = "测试结束(中断)"
          self.sq_end=False
          return
      # <span id="tab-1379-btnInnerEl" data-ref="btnInnerEl" unselectable="on" class="x-tab-inner x-tab-inner-default">日志</span>
      if not self.element_page():
        return


      list_dic = []
      # table = self.chrome.get_element_id('ext-element-45')
      table = self.driver.find_element(By.CSS_SELECTOR,
                                              '[style*="width: 2372px; transform: translate3d(0px, 0px, 0px);"]')
      # aa=table.find_elements(By.TAG_NAME,'table')
      element_s_row = table.find_elements(By.CSS_SELECTOR, '.x-grid-item.x-grid-row-collapsed')
      for element_row in element_s_row:
        element_class = element_row.get_attribute('id')
        # ******************************************************************************************************************
        list_name = ["端口", "Peer", "端口速率", "端口限速", "模块速率", "模块厂商", "开始时间", "测试时长", "测试类型",
                     "测试结果", "丢包数", "丢包率", "Link闪烁"]
        # print(f"{element_class}***********************************************************")
        if element_class == "tableview-1360-record-738":
          pass
        td = element_row.find_elements(By.TAG_NAME, 'td')
        dic_a = {}
        for i in range(2, 15):
          s_name = list_name[i - 2]
          s_value = td[i].text
          if s_name == "开始时间":
            dic_a[s_name] = datetime.strptime(s_value, "%Y-%m-%d %H:%M:%S")
          elif s_name == "测试结果":
            dic_a[s_name] = True if s_value == "P" else False
          else:
            dic_a[s_name] = s_value
        if dic_a["开始时间"] < time_begin:
          return
        bb = element_row.find_element(By.TAG_NAME, 'table')
        trs = bb.find_elements(By.TAG_NAME, 'tr')
        for tr in trs:
          tds = tr.find_elements(By.TAG_NAME, 'td')
          if len(tds) != 2:
            continue
          s_key = tds[0].find_element(By.TAG_NAME, 'b').get_attribute("innerHTML").replace("：", "").strip()
          dic_a[s_key] = tds[1].get_attribute("innerHTML").strip()
        self.log =element_class
        list_dic.append(dic_a)
        df=pd.get_df(list_dic)
        print(df)
      self.log = "测试结束(完成)"
    except Exception as e:
      print(e)
      self.log = f"测试结束(异常退出)"
    finally:
        self.driver.quit()



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
