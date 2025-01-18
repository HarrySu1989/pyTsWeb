from flask import Blueprint, jsonify, request
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
bp = Blueprint('K3', __name__, url_prefix='/K3')
@bp.route('/', methods=['GET', 'POST'])
def index():
  chrome_options = Options()
  chrome_options.add_argument("--window-size=1200,1000")
  s_path = os.path.dirname(__file__)
  s_path=s_path.replace("K3","")
  s_exe = f"{s_path}flow\\chromedriver-130.0.6723.91.exe"
  service = Service(s_exe)
  driver = webdriver.Chrome(options=chrome_options, service=service)
  driver.get("http://erp.china-tscom.com")
  time.sleep(1)
  bt_begin = None
  for i in range(10):
    try:
      bt_begin = driver.find_element(By.ID, 'user')
      if not bt_begin:
        break
      time.sleep(1)
    except:
      print("等待用户窗口")
      time.sleep(1)
  if not bt_begin:
    return "无法获取用户窗口"

  bt_begin.send_keys("徐俊松")
  tb_password = driver.find_element(By.ID, 'password')
  tb_password.send_keys("Ts.123456")
  bt_login = driver.find_element(By.ID, 'btnLogin')
  bt_login.click()
  # 物料清单正查
  bt_a=None
  for i in range(30):
    try:
      bt_a = driver.find_element(By.XPATH,"//*[contains(text(), '物料清单正查')]")
      if not bt_a:
        break
      time.sleep(1)
    except:
      print("等待物料清单正查")
      time.sleep(1)
  if not bt_a:
    return "无法获取物料清单正查"
  bt_a.click()
  print("成功进入物料清单正查")
  lb_a=None
  for i in range(30):
    try:
      # 1f8c18f9-0061-4b41-ad7d-f69a0797124c-FBILLMATERIALID
      # 1f8c18f9-0061-4b41-ad7d-f69a0797124c-
      # 假设你要定位一个 ID 包含 "partialIdString" 的元素
      partial_id_string = "FBILLMATERIALID-EDITOR"
      xpath_expression = f"//*[contains(@id, '{partial_id_string}')]"
      lb_a = driver.find_element(By.XPATH, xpath_expression)
      if not bt_a:
        break
      time.sleep(1)
    except:
      print("等待物料编码")
      time.sleep(1)
  if not lb_a:
    return "无法获取物物料编码"
  print("获取物物料编码")
  time.sleep(10)
  return s_exe