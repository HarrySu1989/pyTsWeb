from flask import Blueprint, jsonify, request
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

from sqlalchemy.testing import fails

bp = Blueprint('K3', __name__, url_prefix='/K3')
chrome_options = Options()
chrome_options.add_argument("--window-size=1200,1000")
s_path = os.path.dirname(__file__)
s_path=s_path.replace("K3","")
s_exe = f"{s_path}flow\\chromedriver-130.0.6723.91.exe"
service = Service(s_exe)
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get("http://erp.china-tscom.com")
def set_begin():
  bt_begin = None
  for i in range(10):
    try:
      bt_begin = driver.find_element(By.ID, 'user')
      break
    except:
      print("等待用户窗口")
      time.sleep(1)
  if not bt_begin:
    print("无法获取用户窗口")
    return False

  bt_begin.send_keys("徐俊松")
  tb_password = driver.find_element(By.ID, 'password')
  tb_password.send_keys("Ts.123456")
  bt_login = driver.find_element(By.ID, 'btnLogin')
  bt_login.click()
  return True

def set_物料(s_物料):
  # 物料清单正查
  bt_a = None
  for i in range(30):
    try:
      bt_a = driver.find_element(By.XPATH, "//*[contains(text(), '物料清单正查')]")
      break
    except:
      print("等待物料清单正查")
      time.sleep(1)
  if not bt_a:
    print("无法获取物料清单正查")
    return False
  bt_a.click()
  print("成功进入物料清单正查")
  lb_a = None
  for i in range(30):
    try:
      # 1f8c18f9-0061-4b41-ad7d-f69a0797124c-FBILLMATERIALID
      # 1f8c18f9-0061-4b41-ad7d-f69a0797124c-
      # 假设你要定位一个 ID 包含 "partialIdString" 的元素

      lb_a = driver.find_element(By.XPATH, f"//*[contains(@id, 'FBILLMATERIALID-EDITOR')]")
      break
    except:
      print("等待物料编码")
      time.sleep(1)
  if not lb_a:
    print("无法获取物物料编码")
    return False
  # ui-poplistedit-displayname
  # ui-poplistedit-displayname
  lb_b=lb_a.find_element(By.CLASS_NAME, f'k-input')
  print(lb_b)
  # 使用 JavaScript 执行器更新 span 元素的内容
  lb_b.send_keys(s_物料)
  time.sleep(0.2)
  lb_b.send_keys(Keys.RETURN)  # 或者使用 Keys.ENTER，它们是等价的
  time.sleep(0.2)
  lb_a = driver.find_element(By.XPATH, f"//*[contains(@id, 'FREFRESH_c')]")
  # print(lb_a.text)
  lb_a.click()
  return True
def set_download():
  lb_a = driver.find_element(By.XPATH, f"//*[contains(@id, 'BILLMENU_TOOLBAR-tbExport')]")
  lb_a.click()
  lb_a = None
  for i in range(30):
    try:
      # 1f8c18f9-0061-4b41-ad7d-f69a0797124c-FBILLMATERIALID
      # 1f8c18f9-0061-4b41-ad7d-f69a0797124c-
      # 假设你要定位一个 ID 包含 "partialIdString" 的元素

      lb_a = driver.find_element(By.XPATH, f"//*[contains(@id, 'FBTNOK_c')]")
      break
    except:
      print("等待确认按钮")
      time.sleep(1)
  if not lb_a:
    print("无法获取确认按钮")
    return False

  lb_a.click()
  lb_a = None
  for i in range(30):
    try:
      # 1f8c18f9-0061-4b41-ad7d-f69a0797124c-FBILLMATERIALID
      # 1f8c18f9-0061-4b41-ad7d-f69a0797124c-
      # 假设你要定位一个 ID 包含 "partialIdString" 的元素

      lb_a = driver.find_element(By.XPATH, f"//*[contains(@id, 'FDOWNLOAD_c')]")
      break
    except:
      print("等待下载按钮")
      time.sleep(1)
  if not lb_a:
    print("无法获取下载按钮")
    return False

  lb_a.click()
  time.sleep(1)
  lb_a = driver.find_element(By.CLASS_NAME, f"k-window-actions")
  lb_a.click()
  return True

@bp.route('/', methods=['GET', 'POST'])
def index():
  if not set_begin():
    return
  list=[]
  list.append("AOC.100G.OM3-QSFPLC-28-00-00")
  list.append("AOC.100G.OM3-QSFPLC-30-00-00")
  list.append("AOC.100G.OM3-QSFPLC-31-00-00")
  for s in list:
    if not set_物料(s):
      continue
    time.sleep(2)
    if not set_download():
      continue

  #

#
  time.sleep(10000000)
  return s_exe