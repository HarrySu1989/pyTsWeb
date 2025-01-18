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
  lb_b.clear()
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
text="""
AOC.100G.OM3-QSFPLC-0/5-00-00
AOC.100G.OM3-QSFPLC-01-00-00
AOC.100G.OM3-QSFPLC-01-01-YX
AOC.100G.OM3-QSFPLC-02-00-00
AOC.100G.OM3-QSFPLC-03-01-YX
AOC.100G.OM3-QSFPLC-03-02-00
AOC.100G.OM3-QSFPLC-03-02-01
AOC.100G.OM3-QSFPLC-04-00-00
AOC.100G.OM3-QSFPLC-05-00-00
AOC.100G.OM3-QSFPLC-06-00-00
AOC.100G.OM3-QSFPLC-07-00-00
AOC.100G.OM3-QSFPLC-08-00-00
AOC.100G.OM3-QSFPLC-09-00-00
AOC.100G.OM3-QSFPLC-1/5-00-00c
AOC.100G.OM3-QSFPLC-10-00-00
AOC.100G.OM3-QSFPLC-10-00-01
AOC.100G.OM3-QSFPLC-10-01-00
AOC.100G.OM3-QSFPLC-10-01-YX
AOC.100G.OM3-QSFPLC-11-00-00
AOC.100G.OM3-QSFPLC-12-00-00
AOC.100G.OM3-QSFPLC-13-00-00
AOC.100G.OM3-QSFPLC-15c
AOC.100G.OM3-QSFPLC-16-00-00
AOC.100G.OM3-QSFPLC-17-00-00
AOC.100G.OM3-QSFPLC-18-00-00
AOC.100G.OM3-QSFPLC-2/5-00-00
AOC.100G.OM3-QSFPLC-20-00-00
AOC.100G.OM3-QSFPLC-21-00-00
AOC.100G.OM3-QSFPLC-22-00-00
AOC.100G.OM3-QSFPLC-25-00-YX
AOC.100G.OM3-QSFPLC-27-00-00
AOC.100G.OM3-QSFPLC-28-00-00
AOC.100G.OM3-QSFPLC-30-00-00
AOC.100G.OM3-QSFPLC-31-00-00
AOC.100G.OM3-QSFPLC-34-00-00
AOC.100G.OM3-QSFPLC-35-00-00
AOC.100G.OM3-QSFPLC-40-00-00
AOC.100G.OM3-QSFPLC-5/5-00-00
AOC.100G.OM3-QSFPLC-50-00-00
AOC.100G.OM3-QSFPLC-6/5-00-00
AOC.100G.OM3-QSFPMTP-03-00-YX
AOC.100G.OM3-QSFPMTP-08-00-YX
AOC.100G.OM3-QSFPQSFP-0/2-00-00
AOC.100G.OM3-QSFPQSFP-0/3-00-00
AOC.100G.OM3-QSFPQSFP-0/5-00-CT
AOC.100G.OM3-QSFPQSFP-0/5-01-YX
AOC.100G.OM3-QSFPQSFP-01-00-00
AOC.100G.OM3-QSFPQSFP-01-00-CT
AOC.100G.OM3-QSFPQSFP-01-01-YX
AOC.100G.OM3-QSFPQSFP-01-12-00
AOC.100G.OM3-QSFPQSFP-02-00-CT
AOC.100G.OM3-QSFPQSFP-02-01-00
AOC.100G.OM3-QSFPQSFP-02-01-01
AOC.100G.OM3-QSFPQSFP-02-01-02
AOC.100G.OM3-QSFPQSFP-02-01-YX
AOC.100G.OM3-QSFPQSFP-02-12-00
AOC.100G.OM3-QSFPQSFP-03-01-00
AOC.100G.OM3-QSFPQSFP-03-01-01
AOC.100G.OM3-QSFPQSFP-03-01-02
AOC.100G.OM3-QSFPQSFP-03-01-04
AOC.100G.OM3-QSFPQSFP-03-01-05
AOC.100G.OM3-QSFPQSFP-03-01-YX
AOC.100G.OM3-QSFPQSFP-03-02-00
AOC.100G.OM3-QSFPQSFP-03-02-01
AOC.100G.OM3-QSFPQSFP-03-10-00
AOC.100G.OM3-QSFPQSFP-03-11-YX
AOC.100G.OM3-QSFPQSFP-04-00-00
AOC.100G.OM3-QSFPQSFP-04-01-00
AOC.100G.OM3-QSFPQSFP-04-12-00
AOC.100G.OM3-QSFPQSFP-05-01-00
AOC.100G.OM3-QSFPQSFP-05-01-01
AOC.100G.OM3-QSFPQSFP-05-01-YX
AOC.100G.OM3-QSFPQSFP-05-01/I-YX
AOC.100G.OM3-QSFPQSFP-05-12-00
AOC.100G.OM3-QSFPQSFP-05-TS-00
AOC.100G.OM3-QSFPQSFP-06-00-00
AOC.100G.OM3-QSFPQSFP-06-01-YX
AOC.100G.OM3-QSFPQSFP-07-01-YX
AOC.100G.OM3-QSFPQSFP-07-12-00
AOC.100G.OM3-QSFPQSFP-07-TS-00
AOC.100G.OM3-QSFPQSFP-07-TS-01
AOC.100G.OM3-QSFPQSFP-08-00-00
AOC.100G.OM3-QSFPQSFP-09-00-00
AOC.100G.OM3-QSFPQSFP-09-12-00
AOC.100G.OM3-QSFPQSFP-1/5-00-00
AOC.100G.OM3-QSFPQSFP-10-01-YX
AOC.100G.OM3-QSFPQSFP-10-12-00
AOC.100G.OM3-QSFPQSFP-10-TS-00
AOC.100G.OM3-QSFPQSFP-10-TS-01
AOC.100G.OM3-QSFPQSFP-10-TS-02
AOC.100G.OM3-QSFPQSFP-10-TS-05
AOC.100G.OM3-QSFPQSFP-10-TS-06
AOC.100G.OM3-QSFPQSFP-10-TS-07
AOC.100G.OM3-QSFPQSFP-10-TS-08
AOC.100G.OM3-QSFPQSFP-11-00-00
AOC.100G.OM3-QSFPQSFP-12-01-YX
AOC.100G.OM3-QSFPQSFP-12-TS-00
AOC.100G.OM3-QSFPQSFP-12-TS-01
AOC.100G.OM3-QSFPQSFP-13-00-00
AOC.100G.OM3-QSFPQSFP-15-01-YX
AOC.100G.OM3-QSFPQSFP-15-12-00
AOC.100G.OM3-QSFPQSFP-15-TS-00
AOC.100G.OM3-QSFPQSFP-15-TS-01
AOC.100G.OM3-QSFPQSFP-15-TS-02
AOC.100G.OM3-QSFPQSFP-16-TS-00
AOC.100G.OM3-QSFPQSFP-16-TS-01
AOC.100G.OM3-QSFPQSFP-17-TS-00
AOC.100G.OM3-QSFPQSFP-17-TS-01
AOC.100G.OM3-QSFPQSFP-18-00-00
AOC.100G.OM3-QSFPQSFP-2/5-00-00
AOC.100G.OM3-QSFPQSFP-20-01-YX
AOC.100G.OM3-QSFPQSFP-20-11-YX
AOC.100G.OM3-QSFPQSFP-20-12-00
AOC.100G.OM3-QSFPQSFP-20-TS-00
AOC.100G.OM3-QSFPQSFP-20-TS-01
AOC.100G.OM3-QSFPQSFP-21-TS-00
AOC.100G.OM3-QSFPQSFP-21-TS-01
AOC.100G.OM3-QSFPQSFP-22-TS-00
AOC.100G.OM3-QSFPQSFP-22-TS-01
AOC.100G.OM3-QSFPQSFP-25-01-YX
AOC.100G.OM3-QSFPQSFP-25-12-00
AOC.100G.OM3-QSFPQSFP-25-TS-00
AOC.100G.OM3-QSFPQSFP-25-TS-01
AOC.100G.OM3-QSFPQSFP-27-TS-00
AOC.100G.OM3-QSFPQSFP-27-TS-01
AOC.100G.OM3-QSFPQSFP-28-00-00
AOC.100G.OM3-QSFPQSFP-30-01-YX
AOC.100G.OM3-QSFPQSFP-30-12-00
AOC.100G.OM3-QSFPQSFP-30-TS-00
AOC.100G.OM3-QSFPQSFP-30-TS-01
AOC.100G.OM3-QSFPQSFP-31-00-00
AOC.100G.OM3-QSFPQSFP-34-00-00
AOC.100G.OM3-QSFPQSFP-35-TS-00
AOC.100G.OM3-QSFPQSFP-35-TS-01
AOC.100G.OM3-QSFPQSFP-35-TS-02
AOC.100G.OM3-QSFPQSFP-40-TS-00
AOC.100G.OM3-QSFPQSFP-40-TS-01
AOC.100G.OM3-QSFPQSFP-40-TS-02
AOC.100G.OM3-QSFPQSFP-45-TS-01
AOC.100G.OM3-QSFPQSFP-5/5-00-00
AOC.100G.OM3-QSFPQSFP-50-00-00
AOC.100G.OM3-QSFPQSFP-6/5-00-00
AOC.100G.OM3-QSFPQSFP-60-00-00
AOC.100G.OM3-QSFPQSFP-8/5-00-00
AOC.100G.OM3-QSFPQSFP-9/5-00-00
AOC.100G.OM3-QSFPSFP-0/5-00-00
AOC.100G.OM3-QSFPSFP-01-00-00
AOC.100G.OM3-QSFPSFP-01-01/I-YX
AOC.100G.OM3-QSFPSFP-02-00-00
AOC.100G.OM3-QSFPSFP-03-01-YX
AOC.100G.OM3-QSFPSFP-04-00-00
AOC.100G.OM3-QSFPSFP-05-00-00
AOC.100G.OM3-QSFPSFP-05-00-01
AOC.100G.OM3-QSFPSFP-05-01-YX
AOC.100G.OM3-QSFPSFP-06-00-00
AOC.100G.OM3-QSFPSFP-07-00-00
AOC.100G.OM3-QSFPSFP-07-01-YX
AOC.100G.OM3-QSFPSFP-08-00-00
AOC.100G.OM3-QSFPSFP-09-00-00
AOC.100G.OM3-QSFPSFP-1/5-00-00
AOC.100G.OM3-QSFPSFP-10-00-01
AOC.100G.OM3-QSFPSFP-10-01-YX
AOC.100G.OM3-QSFPSFP-11-00-00
AOC.100G.OM3-QSFPSFP-12-00-00
AOC.100G.OM3-QSFPSFP-13-00-00
AOC.100G.OM3-QSFPSFP-15-00-00
AOC.100G.OM3-QSFPSFP-15-00-01
AOC.100G.OM3-QSFPSFP-15-01-YX
AOC.100G.OM3-QSFPSFP-16-00-00
AOC.100G.OM3-QSFPSFP-2/5-00-00
AOC.100G.OM3-QSFPSFP-20-00-00
AOC.100G.OM3-QSFPSFP-25-00-00
AOC.100G.OM3-QSFPSFP-25-00-01
AOC.100G.OM3-QSFPSFP-3/5-00-00
AOC.100G.OM3-QSFPSFP-30-00-00
AOC.100G.OM3-QSFPSFP-30-00-01
AOC.100G.OM3-QSFPSFP-35-00-00
AOC.100G.OM3-QSFPSFP-4/5-00-00
AOC.100G.OM3-QSFPSFP-5/5-00-00
AOC.100G.OM3-QSFPSFP-50-00-00
AOC.100G.OM3-SDDSDD-03-00-00
AOC.100G.OM3-SDDSDD-05-00-00
AOC.100G.OM3-SDDSDD-05-00-YX
AOC.100G.OM3-SDDSDD-07-00-00
AOC.100G.OM3-SDDSDD-07-00-YX
AOC.100G.OM3-SDDSDD-10-00-00
AOC.100G.OM3-SDDSDD-10-00-YX
AOC.100G.OM3-SDDSDD-15-00-00
AOC.100G.OM3-SDDSDD-15-00-YX
AOC.100G.OM3-SDDSFP-03-00-00
AOC.100G.OM4-QSFPQSFP-100-01-00
AOC.100G.OM4-QSFPQSFP-100-01-YX
AOC.100G.OM4-QSFPQSFP-75-00-00
AOC.10G.M5-SFPLC-05-01-YX
AOC.10G.M5-SFPLC-05-02-00
AOC.10G.M5-SFPSFP-00-01-00
AOC.10G.M5-SFPSFP-00-01-01
AOC.10G.M5-SFPSFP-00-01-02
AOC.10G.M5-SFPSFP-00-01-03
AOC.10G.M5-SFPSFP-00-01-04
AOC.10G.M5-SFPSFP-05-01-00
AOC.10G.M5-SFPSFP-1/75-00-00
AOC.10G.M5-SFPSFP-2/75-00-00
AOC.10G.M5-SFPSFP-3/25-00-00
AOC.10G.M5-SFPSFP-3/75-00-00
AOC.10G.M5-SFPSFP-4/25-00-00
AOC.10G.M5-SFPSFP-4/75-00-00
AOC.10G.M5-SFPSFP-5/25-00-00
AOC.10G.M5-SFPSFP-5/75-00-00
AOC.10G.OM3-SFPSFP-0/12-00-00
AOC.10G.OM3-SFPSFP-0/15-00-00
AOC.10G.OM3-SFPSFP-0/3-00-00
AOC.10G.OM3-SFPSFP-0/5-00-00
AOC.10G.OM3-SFPSFP-0/66-00-00
AOC.10G.OM3-SFPSFP-00-01-00
AOC.10G.OM3-SFPSFP-00-01-01
AOC.10G.OM3-SFPSFP-00-01-02
AOC.10G.OM3-SFPSFP-00-01-03
AOC.10G.OM3-SFPSFP-00-01-04
AOC.10G.OM3-SFPSFP-01-00-01
AOC.10G.OM3-SFPSFP-01-00-02
AOC.10G.OM3-SFPSFP-01-01/I-YX
AOC.10G.OM3-SFPSFP-02-00-00
AOC.10G.OM3-SFPSFP-02-01/I-YX
AOC.10G.OM3-SFPSFP-03-00-00
AOC.10G.OM3-SFPSFP-03-01-00
AOC.10G.OM3-SFPSFP-03-01-YX
AOC.10G.OM3-SFPSFP-03-01/I-YX
AOC.10G.OM3-SFPSFP-04-00-00
AOC.10G.OM3-SFPSFP-05-01-00
AOC.10G.OM3-SFPSFP-05-01-01
AOC.10G.OM3-SFPSFP-05-01-02
AOC.10G.OM3-SFPSFP-05-01/I-YX
AOC.10G.OM3-SFPSFP-06-00-00
AOC.10G.OM3-SFPSFP-07-01-00
AOC.10G.OM3-SFPSFP-07-01-01
AOC.10G.OM3-SFPSFP-08-00-00
AOC.10G.OM3-SFPSFP-09-00-00
AOC.10G.OM3-SFPSFP-10-01-00
AOC.10G.OM3-SFPSFP-10-01-01
AOC.10G.OM3-SFPSFP-10-01/I-YX
AOC.10G.OM3-SFPSFP-100-00-00
AOC.10G.OM3-SFPSFP-11-00-00
AOC.10G.OM3-SFPSFP-12-00-00
AOC.10G.OM3-SFPSFP-13-00-00
AOC.10G.OM3-SFPSFP-14-00-00
AOC.10G.OM3-SFPSFP-15-00-00
AOC.10G.OM3-SFPSFP-15-00-01
AOC.10G.OM3-SFPSFP-15-01/I-YX
AOC.10G.OM3-SFPSFP-150-00-00
AOC.10G.OM3-SFPSFP-16-00-00
AOC.10G.OM3-SFPSFP-17-00-00
AOC.10G.OM3-SFPSFP-18-00-00
AOC.10G.OM3-SFPSFP-19-00-00
AOC.10G.OM3-SFPSFP-2/5-00-YX
AOC.10G.OM3-SFPSFP-20-00-00
AOC.10G.OM3-SFPSFP-20-00-01
AOC.10G.OM3-SFPSFP-20-01/I-YX
AOC.10G.OM3-SFPSFP-21-00-00
AOC.10G.OM3-SFPSFP-25-00-00
AOC.10G.OM3-SFPSFP-25-00-01
AOC.10G.OM3-SFPSFP-25-01/I-YX
AOC.10G.OM3-SFPSFP-30-00-00
AOC.10G.OM3-SFPSFP-30-00-01
AOC.10G.OM3-SFPSFP-30-01/I-YX
AOC.10G.OM3-SFPSFP-35-00-00
AOC.10G.OM3-SFPSFP-40-00-00
AOC.10G.OM3-SFPSFP-42-00-00
AOC.10G.OM3-SFPSFP-45-00-00
AOC.10G.OM3-SFPSFP-46-00-00
AOC.10G.OM3-SFPSFP-50-00-00
AOC.10G.OM3-SFPSFP-50-00-01
AOC.10G.OM3-SFPSFP-50-01/I-YX
AOC.10G.OM3-SFPSFP-52-00-00
AOC.10G.OM3-SFPSFP-55-00-00
AOC.10G.OM3-SFPSFP-60-00-00
AOC.10G.OM3-SFPSFP-65-00-00
AOC.10G.OM3-SFPSFP-70-00-00
AOC.10G.OM3-SFPSFP-70-01/I-YX
AOC.10G.OM3-SFPSFP-72-00-00
AOC.10G.OM3-SFPSFP-75-00-00
AOC.10G.OM3-SFPSFP-76-00-00
AOC.10G.OM3-SFPSFP-80-00-00
AOC.10G.OM3-SFPSFP-95-00-00
AOC.10G.OM3-SFPSFP-95-01/I-YX
AOC.200G.OM3-QDDMTP-02-10-00
AOC.200G.OM3-QDDMTP-02-10-01
AOC.200G.OM3-QDDQDD-0/5-00-00
AOC.200G.OM3-QDDQDD-0/5-00-01
AOC.200G.OM3-QDDQDD-01-01-00
AOC.200G.OM3-QDDQDD-03-01-00
AOC.200G.OM3-QDDQDD-07-00-00
AOC.200G.OM3-QDDQDD-07-00-YX
AOC.200G.OM3-QDDQDD-10-01-00
AOC.200G.OM3-QDDQDD-20-00-00
AOC.200G.OM3-QDDQSFP-03-00-00
AOC.200G.OM3-QDDQSFP-03-01-00
AOC.200G.OM3-QDDQSFP-03-01-02
AOC.200G.OM3-QDDQSFP-04-00-00
AOC.200G.OM3-QDDQSFP-04-00-01
AOC.200G.OM3-QDDQSFP-05-00-00
AOC.200G.OM3-QDDQSFP-05-00-02
AOC.200G.OM3-QDDQSFP-10-00-00
AOC.200G.OM3-QDDQSFP-15-01-00
AOC.200G.OM3-QDDQSFP-25-00-00
AOC.200G.OM3-QDDQSFP-30-00-00
AOC.200G.OM3-QDDQSFP-30-00-YX
AOC.200G.OM3-QDDSFP-01-00-00
AOC.200G.OM3-QDDSFP-02-00-00
AOC.200G.OM3-QDDSFP-03-00-00
AOC.200G.OM3-QDDSFP-10-00-00
AOC.200G.OM3-QDDSFP-15-00-00
AOC.200G.OM3-QDDSFP-20-00-00
AOC.200G.OM3-QDDSFP-30-00-00
AOC.200G.OM3-QSFPQSFP-01-00-00
AOC.200G.OM3-QSFPQSFP-01-10-00
AOC.200G.OM3-QSFPQSFP-02-00-00
AOC.200G.OM3-QSFPQSFP-02-12-02
AOC.200G.OM3-QSFPQSFP-03-00-01
AOC.200G.OM3-QSFPQSFP-03-00-02
AOC.200G.OM3-QSFPQSFP-03-00-03
AOC.200G.OM3-QSFPQSFP-03-00-04
AOC.200G.OM3-QSFPQSFP-03-10-01
AOC.200G.OM3-QSFPQSFP-03-12-01
AOC.200G.OM3-QSFPQSFP-03-12-02
AOC.200G.OM3-QSFPQSFP-03-12-03
AOC.200G.OM3-QSFPQSFP-03-13-00
AOC.200G.OM3-QSFPQSFP-03-13-01
AOC.200G.OM3-QSFPQSFP-03-13-02
AOC.200G.OM3-QSFPQSFP-05-02-01
AOC.200G.OM3-QSFPQSFP-05-02-03
AOC.200G.OM3-QSFPQSFP-05-02-05
AOC.200G.OM3-QSFPQSFP-05-10-00
AOC.200G.OM3-QSFPQSFP-05-10-02
AOC.200G.OM3-QSFPQSFP-05-12-02
AOC.200G.OM3-QSFPQSFP-05-12-03
AOC.200G.OM3-QSFPQSFP-05-12-04
AOC.200G.OM3-QSFPQSFP-10-00-01
AOC.200G.OM3-QSFPQSFP-10-10-05
AOC.200G.OM3-QSFPQSFP-10-10-06
AOC.200G.OM3-QSFPQSFP-10-10-07
AOC.200G.OM3-QSFPQSFP-15-00-01
AOC.200G.OM3-QSFPQSFP-15-10-05
AOC.200G.OM3-QSFPQSFP-15-10-06
AOC.200G.OM3-QSFPQSFP-15-10-07
AOC.200G.OM3-QSFPQSFP-20-00-01
AOC.200G.OM3-QSFPQSFP-20-00-02
AOC.200G.OM3-QSFPQSFP-20-00-03
AOC.200G.OM3-QSFPQSFP-20-10-01
AOC.200G.OM3-QSFPQSFP-20-10-02
AOC.200G.OM3-QSFPQSFP-20-10-03
AOC.200G.OM3-QSFPQSFP-30-00-01
AOC.200G.OM3-QSFPQSFP-30-00-02
AOC.200G.OM3-QSFPQSFP-30-11-YX
AOC.200G.OM3-QSFPQSFP-30-12-00
AOC.200G.OM3-QSFPQSFP-30-12-01
AOC.200G.OM3-QSFPQSFP-30-12-02
AOC.200G.OM3-QSFPQSFP-50-01-00
AOC.200G.OM3-QSFPQSFP-50-01-01
AOC.200G.OM3-QSFPQSFP-50-02-00
AOC.200G.OM3-QSFPQSFP-50-02-01
AOC.200G.OM3-QSFPQSFP-50-02-02
AOC.200G.OM4-QDDQDD-100-00-00
AOC.200G.OM4-QSFPQSFP-02-00-00
AOC.200G.OM4-QSFPQSFP-02-11-00
AOC.200G.OM4-QSFPQSFP-08-00-00
AOC.200G.OM4-QSFPQSFP-08-11-00
AOC.200G.OM4-QSFPQSFP-09-00-00
AOC.200G.OM4-QSFPQSFP-09-11-00
AOC.200G.OM4-QSFPQSFP-10-00-00
AOC.200G.OM4-QSFPQSFP-10-11-00
AOC.200G.OM4-QSFPQSFP-11-00-00
AOC.200G.OM4-QSFPQSFP-11-11-00
AOC.200G.OM4-QSFPQSFP-13-00-00
AOC.200G.OM4-QSFPQSFP-13-11-00
AOC.200G.OM4-QSFPQSFP-16-00-00
AOC.200G.OM4-QSFPQSFP-16-11-00
AOC.200G.OM4-QSFPQSFP-30-11-01
AOC.25G.M5-SFPSFP-00-00-00
AOC.25G.OM3-SFPLC-03-00-00
AOC.25G.OM3-SFPLC-09-00-00
AOC.25G.OM3-SFPSFP-0/15-00-00
AOC.25G.OM3-SFPSFP-0/5-00-00
AOC.25G.OM3-SFPSFP-00-00-00
AOC.25G.OM3-SFPSFP-00-00-01
AOC.25G.OM3-SFPSFP-00-00-02
AOC.25G.OM3-SFPSFP-00-00-03
AOC.25G.OM3-SFPSFP-00-00-04
AOC.25G.OM3-SFPSFP-00-00-05
AOC.25G.OM3-SFPSFP-00-00-06
AOC.25G.OM3-SFPSFP-00-00-07
AOC.25G.OM3-SFPSFP-00-00-08
AOC.25G.OM3-SFPSFP-00-00-09
AOC.25G.OM3-SFPSFP-00-00-10
AOC.25G.OM3-SFPSFP-00-00-11
AOC.25G.OM3-SFPSFP-01-00-00
AOC.25G.OM3-SFPSFP-01-01-00
AOC.25G.OM3-SFPSFP-01-01-YX
AOC.25G.OM3-SFPSFP-02-00-00
AOC.25G.OM3-SFPSFP-02-01-00
AOC.25G.OM3-SFPSFP-02-01-YX
AOC.25G.OM3-SFPSFP-02-01/I-YX
AOC.25G.OM3-SFPSFP-03-01-00
AOC.25G.OM3-SFPSFP-03-01-YX
AOC.25G.OM3-SFPSFP-03-02-00
AOC.25G.OM3-SFPSFP-04-01-00
AOC.25G.OM3-SFPSFP-04-01-YX
AOC.25G.OM3-SFPSFP-05-01-00
AOC.25G.OM3-SFPSFP-05-01-YX
AOC.25G.OM3-SFPSFP-05-02-00
AOC.25G.OM3-SFPSFP-06-00-00
AOC.25G.OM3-SFPSFP-07-01-00
AOC.25G.OM3-SFPSFP-07-01-YX
AOC.25G.OM3-SFPSFP-08-01-00
AOC.25G.OM3-SFPSFP-08-01-01
AOC.25G.OM3-SFPSFP-08-01-YX
AOC.25G.OM3-SFPSFP-09-00-00
AOC.25G.OM3-SFPSFP-10-01-00
AOC.25G.OM3-SFPSFP-10-01-YX
AOC.25G.OM3-SFPSFP-10-02-00
AOC.25G.OM3-SFPSFP-11-00-00
AOC.25G.OM3-SFPSFP-12-00-01
AOC.25G.OM3-SFPSFP-13-00-00
AOC.25G.OM3-SFPSFP-14-00-00
AOC.25G.OM3-SFPSFP-15-01-00
AOC.25G.OM3-SFPSFP-15-01-YX
AOC.25G.OM3-SFPSFP-16-00-00
AOC.25G.OM3-SFPSFP-17-00-00
AOC.25G.OM3-SFPSFP-18-00-00
AOC.25G.OM3-SFPSFP-19-00-00
AOC.25G.OM3-SFPSFP-2/5-00-00
AOC.25G.OM3-SFPSFP-20-00-01
AOC.25G.OM3-SFPSFP-20-00-02
AOC.25G.OM3-SFPSFP-21-00-00
AOC.25G.OM3-SFPSFP-25-00-01
AOC.25G.OM3-SFPSFP-25-00-02
AOC.25G.OM3-SFPSFP-25-01-00
AOC.25G.OM3-SFPSFP-3/5-00-00
AOC.25G.OM3-SFPSFP-30-00-00
AOC.25G.OM3-SFPSFP-30-00-01
AOC.25G.OM3-SFPSFP-35-00-00
AOC.25G.OM3-SFPSFP-40-00-00
AOC.25G.OM3-SFPSFP-42-00-00
AOC.25G.OM3-SFPSFP-45-00-00
AOC.25G.OM3-SFPSFP-46-00-00
AOC.25G.OM3-SFPSFP-50-00-00
AOC.25G.OM3-SFPSFP-50-00-01
AOC.25G.OM3-SFPSFP-52-00-00
AOC.25G.OM3-SFPSFP-55-00-00
AOC.25G.OM3-SFPSFP-60-00-00
AOC.25G.OM3-SFPSFP-65-00-00
AOC.25G.OM3-SFPSFP-70-00-00
AOC.25G.OM4-SFPSFP-00-00-00
AOC.25G.OM4-SFPSFP-100-00-00
AOC.400G.OM3-OSFPOSFP-03-00-05
AOC.400G.OM3-OSFPOSFP-03-01-00
AOC.400G.OM3-OSFPQSFP-03-01-02
AOC.400G.OM3-OSFPQSFP-03-01-ZBNT
AOC.400G.OM3-OSFPQSFP-03-02-00
AOC.400G.OM3-OSFPQSFP-05-00-00
AOC.400G.OM3-OSFPQSFP-15-00-00
AOC.400G.OM3-OSFPQSFP-20-00-00
AOC.400G.OM3-OSFPQSFP-20-02-00
AOC.400G.OM3-OSFPQSFP-30-00-00
AOC.400G.OM3-QDDQDD-01-00-00
AOC.400G.OM3-QDDQDD-03-00-02
AOC.400G.OM3-QDDQDD-03-00-03
AOC.400G.OM3-QDDQDD-05-00-00
AOC.400G.OM3-QDDQDD-07-00-00
AOC.400G.OM3-QDDQDD-1/5-00-00
AOC.400G.OM3-QDDQDD-10-00-00
AOC.400G.OM3-QDDQDD-10-00-YX
AOC.400G.OM3-QDDQDD-15-00-00
AOC.400G.OM3-QDDQDD-50-00-00
AOC.400G.OM3-QDDQSFP-00-00-00
AOC.400G.OM3-QDDQSFP-00-00-01
AOC.400G.OM3-QDDQSFP-00-01-00
AOC.400G.OM3-QDDQSFP-00-01-01
AOC.400G.OM3-QDDQSFP-01-00-YX
AOC.400G.OM3-QDDQSFP-02-00-00
AOC.400G.OM3-QDDQSFP-02-01-00
AOC.400G.OM3-QDDQSFP-02-01-01
AOC.400G.OM3-QDDQSFP-03-00-02
AOC.400G.OM3-QDDQSFP-03-00-03
AOC.400G.OM3-QDDQSFP-03-00-05
AOC.400G.OM3-QDDQSFP-03-01-01
AOC.400G.OM3-QDDQSFP-05-00-00
AOC.400G.OM3-QDDQSFP-05-01-00
AOC.400G.OM3-QDDQSFP-05-01-01
AOC.400G.OM3-QDDQSFP-05-02-00
AOC.400G.OM3-QDDQSFP-05-02-YP
AOC.400G.OM3-QDDQSFP-07-00-00
AOC.400G.OM3-QDDQSFP-07-01-00
AOC.400G.OM3-QDDQSFP-10-00-00
AOC.400G.OM3-QDDQSFP-10-00-01
AOC.400G.OM3-QDDQSFP-10-00-YX
AOC.400G.OM3-QDDQSFP-10-01-00
AOC.400G.OM3-QDDQSFP-15-00-00
AOC.400G.OM3-QDDQSFP-15-00-01
AOC.400G.OM3-QDDQSFP-15-00-02
AOC.400G.OM3-QDDQSFP-15-00-YX
AOC.400G.OM3-QDDQSFP-15-01-00
AOC.400G.OM3-QDDQSFP-20-00-00
AOC.400G.OM3-QDDQSFP-20-01-00
AOC.400G.OM3-QDDQSFP-20-01-01
AOC.400G.OM3-QDDQSFP-20-02-00
AOC.400G.OM3-QDDQSFP-30-00-00
AOC.400G.OM3-QDDQSFP-50-00-00
AOC.400G.OM3-QDDQSFP-70-00-00
AOC.400G.OM3-QDDQSFP-70-00-YX
AOC.400G.OM3-QDDSFP-03-00-00
AOC.400G.OM3-QDDSFP-05-00-00
AOC.40G.M5-QSFPQSFP-03-01-00
AOC.40G.M5-QSFPQSFP-03-01-01
AOC.40G.M5-QSFPQSFP-05-00-01
AOC.40G.M5-QSFPQSFP-10-TS-00
AOC.40G.M5-QSFPSFP-02-11-00
AOC.40G.M5-QSFPSFP-03-01-00
AOC.40G.M5-QSFPSFP-03-01-01
AOC.40G.M5-QSFPSFP-03-11-00
AOC.40G.M5-QSFPSFP-05-11-00
AOC.40G.M5-QSFPSFP-05-TS-00
AOC.40G.M5-QSFPSFP-10-00-00
AOC.40G.M5-QSFPSFP-15-00-00
AOC.40G.OM3-QSFPLC-0/5-00-00
AOC.40G.OM3-QSFPLC-01-00-00
AOC.40G.OM3-QSFPLC-01-00-01
AOC.40G.OM3-QSFPLC-02-00-01
AOC.40G.OM3-QSFPLC-02-01-YX
AOC.40G.OM3-QSFPLC-03-00-00
AOC.40G.OM3-QSFPLC-03-01-YX
AOC.40G.OM3-QSFPLC-03-02-00
AOC.40G.OM3-QSFPLC-03-02-01
AOC.40G.OM3-QSFPLC-03-02-02
AOC.40G.OM3-QSFPLC-04-00-00
AOC.40G.OM3-QSFPLC-05-00-00
AOC.40G.OM3-QSFPLC-05-01-YX
AOC.40G.OM3-QSFPLC-06-00-00
AOC.40G.OM3-QSFPLC-07-00-00
AOC.40G.OM3-QSFPLC-08-00-00
AOC.40G.OM3-QSFPLC-09-00-00
AOC.40G.OM3-QSFPLC-1/5-00-00
AOC.40G.OM3-QSFPLC-1/52-00-00
AOC.40G.OM3-QSFPLC-10-00-00
AOC.40G.OM3-QSFPLC-10-00-01
AOC.40G.OM3-QSFPLC-10-01-00
AOC.40G.OM3-QSFPLC-12-00-00
AOC.40G.OM3-QSFPLC-15-00-00
AOC.40G.OM3-QSFPLC-20-00-00
AOC.40G.OM3-QSFPLC-25-00-00
AOC.40G.OM3-QSFPLC-30-00-00
AOC.40G.OM3-QSFPLC-40-00-00
AOC.40G.OM3-QSFPLC-45-00-00
AOC.40G.OM3-QSFPLC-50-00-00
AOC.40G.OM3-QSFPLC-70-00-00
AOC.40G.OM3-QSFPQSFP-0/3-00-00
AOC.40G.OM3-QSFPQSFP-01-00-00
AOC.40G.OM3-QSFPQSFP-02-00-00
AOC.40G.OM3-QSFPQSFP-03-01-00
AOC.40G.OM3-QSFPQSFP-03-01-01
AOC.40G.OM3-QSFPQSFP-04-00-00
AOC.40G.OM3-QSFPQSFP-05-01-00
AOC.40G.OM3-QSFPQSFP-05-02-00
AOC.40G.OM3-QSFPQSFP-05-02-01
AOC.40G.OM3-QSFPQSFP-06-00-00
AOC.40G.OM3-QSFPQSFP-07-00-01
AOC.40G.OM3-QSFPQSFP-08-00-00
AOC.40G.OM3-QSFPQSFP-09-00-00
AOC.40G.OM3-QSFPQSFP-10-00-00
AOC.40G.OM3-QSFPQSFP-100-00-00
AOC.40G.OM3-QSFPQSFP-15-00-00
AOC.40G.OM3-QSFPQSFP-150-00-00
AOC.40G.OM3-QSFPQSFP-200-00-00
AOC.40G.OM3-QSFPQSFP-25-00-00
AOC.40G.OM3-QSFPQSFP-35-00-00
AOC.40G.OM3-QSFPQSFP-36-00-00
AOC.40G.OM3-QSFPQSFP-45-00-00
AOC.40G.OM3-QSFPQSFP-50-00-00
AOC.40G.OM3-QSFPQSFP-56-00-00
AOC.40G.OM3-QSFPQSFP-60-00-00
AOC.40G.OM3-QSFPQSFP-70-00-00
AOC.40G.OM3-QSFPQSFP-75-00-00
AOC.40G.OM3-QSFPQSFP-80-00-00
AOC.40G.OM3-QSFPSFP-01-00-00
AOC.40G.OM3-QSFPSFP-01-11-00
AOC.40G.OM3-QSFPSFP-02-00-00
AOC.40G.OM3-QSFPSFP-02-11-00
AOC.40G.OM3-QSFPSFP-03-00-00
AOC.40G.OM3-QSFPSFP-03-01-YX
AOC.40G.OM3-QSFPSFP-03-11-00
AOC.40G.OM3-QSFPSFP-04-00-00
AOC.40G.OM3-QSFPSFP-05-00-00
AOC.40G.OM3-QSFPSFP-05-00-01
AOC.40G.OM3-QSFPSFP-05-11-00
AOC.40G.OM3-QSFPSFP-06-00-00
AOC.40G.OM3-QSFPSFP-07-00-00
AOC.40G.OM3-QSFPSFP-07-00-01
AOC.40G.OM3-QSFPSFP-07-11-00
AOC.40G.OM3-QSFPSFP-10-00-00
AOC.40G.OM3-QSFPSFP-10-00-01
AOC.40G.OM3-QSFPSFP-10-00-02
AOC.40G.OM3-QSFPSFP-100-00-00
AOC.40G.OM3-QSFPSFP-12-00-00
AOC.40G.OM3-QSFPSFP-14-00-00
AOC.40G.OM3-QSFPSFP-15-00-00
AOC.40G.OM3-QSFPSFP-15-00-01
AOC.40G.OM3-QSFPSFP-15-00-02
AOC.40G.OM3-QSFPSFP-16-00-00
AOC.40G.OM3-QSFPSFP-18-00-00
AOC.40G.OM3-QSFPSFP-20-00-00
AOC.40G.OM3-QSFPSFP-25-00-00
AOC.40G.OM3-QSFPSFP-25-00-01
AOC.40G.OM3-QSFPSFP-30-00-00
AOC.40G.OM3-QSFPSFP-30-00-01
AOC.40G.OM3-QSFPSFP-35-00-00
AOC.40G.OM3-QSFPSFP-38-00-00
AOC.40G.OM3-QSFPSFP-40-00-00
AOC.40G.OM3-QSFPSFP-43-00-00
AOC.40G.OM3-QSFPSFP-50-00-00
AOC.40G.OM3-QSFPSFP-70-00-00
AOC.40G.OM3-QSFPSFP-80-00-00
AOC.40G.OM4-QSFPLC-02-00-00
AOC.40G.OM4-QSFPLC-02-00-01
AOC.40G.OM4-QSFPLC-05-00-00
AOC.40G.OM4-QSFPLC-05-00-01
AOC.40G.OM4-QSFPLC-05-00-02
AOC.40G.OM4-QSFPQSFP-10-00-00
AOC.56G.OM3-QSFPQSFP-01-00-00
AOC.56G.OM3-QSFPQSFP-02-00-00
AOC.56G.OM3-QSFPQSFP-03-01-00
AOC.56G.OM3-QSFPQSFP-03-01-01
AOC.56G.OM3-QSFPQSFP-04-00-00
AOC.56G.OM3-QSFPQSFP-05-00-00
AOC.56G.OM3-QSFPQSFP-06-00-00
AOC.56G.OM3-QSFPQSFP-07-00-00
AOC.56G.OM3-QSFPQSFP-08-00-00
AOC.56G.OM3-QSFPQSFP-09-00-00
AOC.56G.OM3-QSFPQSFP-10-00-00
AOC.56G.OM3-QSFPQSFP-10-01-YX
AOC.56G.OM3-QSFPQSFP-100-00-00
AOC.56G.OM3-QSFPQSFP-11-00-00
AOC.56G.OM3-QSFPQSFP-12-00-00
AOC.56G.OM3-QSFPQSFP-13-00-00
AOC.56G.OM3-QSFPQSFP-14-00-00
AOC.56G.OM3-QSFPQSFP-15-00-00
AOC.56G.OM3-QSFPQSFP-15-00-01
AOC.56G.OM3-QSFPQSFP-150-00-00
AOC.56G.OM3-QSFPQSFP-16-00-00
AOC.56G.OM3-QSFPQSFP-17-00-00
AOC.56G.OM3-QSFPQSFP-18-00-00
AOC.56G.OM3-QSFPQSFP-19-00-00
AOC.56G.OM3-QSFPQSFP-20-00-01
AOC.56G.OM3-QSFPQSFP-23-00-00
AOC.56G.OM3-QSFPQSFP-25-00-00
AOC.56G.OM3-QSFPQSFP-30-00-00
AOC.56G.OM3-QSFPQSFP-35-00-00
AOC.56G.OM3-QSFPQSFP-36-00-00
AOC.56G.OM3-QSFPQSFP-45-00-00
AOC.56G.OM3-QSFPQSFP-50-00-01
AOC.56G.OM3-QSFPQSFP-56-00-00
AOC.56G.OM3-QSFPQSFP-60-00-00
AOC.56G.OM3-QSFPQSFP-70-00-00
AOC.56G.OM3-QSFPQSFP-75-00-00
AOC.56G.OM3-QSFPQSFP-80-00-00
AOC.56G.OM3-SFPSFP-01-00-00
AOC.56G.OM3-SFPSFP-02-00-00
AOC.56G.OM3-SFPSFP-03-00-00
AOC.56G.OM3-SFPSFP-05-00-00
AOC.800G.OM3-OSFPOSFP-03-00-00
AOC.800G.OM3-QDDQDD-03-00-00
AOC.80G.OM3-QDDSFP-10-00-00
AOC.80G.OM3-QDDSFP-10-00-01
AOCH.OSFP.PCBA-00-01
AOCH.OSFP.PCBA-00-03
AOCH.OSFP.PCBA-01-00
AOCH.QSFP.PCBA-03-00
AOCH.QSFP.PCBA-03-01
AOCH.QSFP.PCBA-03-02
AOCH.QSFP112.PCBA-00-00
AOCH.QSFP28.PCBA-01-01
AOCH.QSFP28.PCBA-01-02
AOCH.QSFP28.PCBA-01-03
AOCH.QSFP28.PCBA-01-04
AOCH.QSFP56.PCBA-01-00
AOCH.QSFP56.PCBA-01-01
AOCH.QSFP56.PCBA-01-02
AOCH.QSFP56.PCBA-02-00
AOCH.QSFP56.PCBA-02-02
AOCH.QSFPDD.PCBA-00-00
AOCH.QSFPDD.PCBA-00-02
AOCH.QSFPDD.PCBA-02-00
AOCH.QSFPDD.PCBA-02-03
AOCH.SFP.PCBA-02-03
AOCH.SFP.PCBA-02-04
AOCH.SFP.PCBA-04-00
AOCH.SFP28.PCBA-01-01
AOCH.SFP28.PCBA-01-02
AOCH.SFP56.PCBA-00-00
AOCH.SFPDD.PCBA-00-00
MP.AOC.10G.02-OM3-00-30-04-10M-TS-00-00
MP.AOC.10G.02-OM3-00-30-04-1M-TS-00-00
MP.AOC.10G.02-OM3-00-30-04-2M-TS-00-00
MP.AOC.10G.02-OM3-00-30-04-3M-TS-00-00
MP.AOC.10G.02-OM3-00-30-04-5M-TS-00-00
MP.AOC.400G.16-OM3-01-30-01-5M-TS-00-00
XCVR.10G.SFP+.MM-850-SR-L-C-00-01
XCVR.10G.SFP+.MM-850-SR-L-C-00-02
XCVR.10G.SFP+.MM-850-SR-L-C-00-04
XCVR.10G.SFP+.MM-850-SR-M-I-00-00
XCVR.10G.SFP+.MM-850-SR-MDC-C-00-00
XCVR.10G.SFP+.SM-1310-LR-L-C-00-00
XCVR.10G.SFP.SM-1310-LR-L-C-02-00
XCVR.1HG.QSFP.MM-850-00-00-C-00-00
XCVR.1HG.QSFP.MM-850-SR4-M-C-01-00
XCVR.1HG.QSFP.MM-850-SR4-M-C-02-00
XCVR.1HG.QSFP.MM-850-SR4-M-C-02-01
XCVR.1HG.QSFP.MM-850-SR4-M-I-01-00
XCVR.1HG.QSFP.MM-850-SW4-M-C-00-00
XCVR.1HG.QSFP.MM-850-SW4-M-C-01-00
XCVR.1HG.QSFP.MM-850-SW4-M-C-01-01
XCVR.1HG.QSFP.SM-CWDM-02-L-C-03-00
XCVR.200G.QDD.MM-850-SR8-M-C-00-00
XCVR.200G.QDD.MM-850-SR8-M-C-00-01
XCVR.200G.QSFP.MM-850-SR4-M-C-01-00
XCVR.200G.QSFP.MM-850-SR4-M-C-01-01
XCVR.200G.QSFP.MM-850-SR4-M-C-01-02
XCVR.25G.SFP.MM-850-SR-L-C-00-00
XCVR.25G.SFP.MM-850-SR-L-C-00-01
XCVR.25G.SFP.MM-850-SR-L-C-02-02
XCVR.25G.SFP.MM-850-SR-L-C-02-03
XCVR.25G.SFP.MM-850-SR-M-I-00-00
XCVR.25G.SFP.MM-850-SR-M-I-00-01
XCVR.25G.SFP.MM-850-SR-MDC-C-00-00
XCVR.400G.OSFP.MM-850-00-M-C-00-00
XCVR.400G.OSFP.MM-850-00-M-C-00-01
XCVR.400G.OSFP.MM-850-00-M-C-01-00
XCVR.400G.OSFP.MM-850-00-M-C-01-02
XCVR.400G.OSFP.MM-850-00-M-C-02-00
XCVR.400G.OSFP.MM-850-00-M-C-02-01
XCVR.400G.OSFP.MM-850-00-M-C-02-02
XCVR.400G.OSFP.MM-850-00-M-C-02-03
XCVR.400G.QDD.MM-850-00-M-C-00-00
XCVR.400G.QDD.MM-850-00-M-C-00-01
XCVR.400G.QDD.MM-850-00-M-C-00-02
XCVR.400G.QDD.MM-850-SR8-M-C-00-00
XCVR.400G.QDD.MM-850-SR8-M-C-00-02
XCVR.400G.QSFP.MM-850-SR4-M-C-00-00
XCVR.40G.QSFP.MM-850-00-00-C-00-00
XCVR.40G.QSFP.MM-850-00-00-C-01-00
XCVR.40G.QSFP.MM-850-SR4-M-C-01-00
XCVR.40G.QSFP.MM-850-SR4-M-C-02-00
XCVR.40G.QSFP.MM-850-SR4-M-C-02-01
XCVR.40G.QSFP.MM-850-SR4-M-I-00-00
XCVR.40G.QSFP.MM-850-SR4-M-I-01-00
XCVR.40G.QSFP.MM-850-SR4-M-I-02-00
XCVR.40G.QSFP.MM-850-SR4-M-I-02-01
XCVR.40G.QSFP.SM-LR4-10-L-C-01-00
XCVR.800G.OSFP.MM-850-0-M-C-00-00
XCVR.800G.OSFP.MM-850-0-M-C-00-01
XCVR.800G.OSFP.MM-850-0-M-C-01-00
XCVR.800G.OSFP.MM-850-0-M-C-01-01
XCVR.800G.QDD.MM-850-00-M-C-00-00
XCVRH.QSFP.PCBA-02-00
XCVRH.QSFP.PCBA-03-00
XCVRH.SFP.PCBA-01-01-00
XCVRH.SFP.PCBA-01-01-01
XCVRH.SFP28.PCBA-00-00-00
"""

@bp.route('/', methods=['GET', 'POST'])
def index():
  if not set_begin():
    return

  list=text.split('/n')
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