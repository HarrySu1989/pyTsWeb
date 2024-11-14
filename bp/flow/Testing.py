
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import datetime, timedelta
import time
import threading

from wx.lib.agw.pyprogress import Continue

import uc.uc_pd as pd
import bp.flow.sql as sql

class Testing:
  def __init__(self):
    self.values=Values()
    self.t = None
    self.count = 0
    self.sq_end = False
    self.s_flow_log = "请录入工单，点击开始测试"
    self.driver = None
    self.bt_begin = None
    self.time_begin = None

#string url = @"http://192.168.8.146:5000/flow/?q=10.77.77.108,123345,harry,1";matebook
#string url = @"http://192.168.8.146:5000/flow/?q=baidu.com,123345,harry,1";matebook
#string url = @"http://172.16.12.89:5000/flow/?q=10.77.77.108,123345,harry,1";


  def get_value(self, s_flow_type:str):
    if self.t and self.t.is_alive():
      if s_flow_type=="开始申请":
        return "当前流量仪正在测试"
      elif s_flow_type == "结束申请":
        self.sq_end = True
        return "结束申请"
      return f"{self.s_flow_log}"
    if s_flow_type=="开始申请":
      self.t = threading.Thread(target=self.thread_run)
      self.t.start()
      self.sq_end = False
      self.count = 0
    return self.s_flow_log

  def element_driver(self):
    #noinspection PyBroadException
    try:
      self.s_flow_log = "正在加载chromedriver"
      chrome_options = Options()
      chrome_options.add_argument("--window-size=1200,1000")
      # service = Service('./bp/flow/chromedriver-130.0.6723.91.exe')
      service = Service('D:/Git/pyTsWeb/bp/flow/chromedriver-130.0.6723.91.exe')
      self.driver = webdriver.Chrome(options=chrome_options, service=service)
      print(f"self.driver:{self.driver}")
      return True
    except Exception as e:
      self.s_flow_log = "测试结束(加载chromedriver异常)"
      print(e)
      return False

  def element_url(self,url=None):
    # noinspection all
    # if not url:url= f"""http://{self.values.flow_input_ip}/"""
    if not url:url= f"""{self.values.flow_input_ip}"""
    self.s_flow_log = f"正在加载URL：{url}"
    #noinspection all
    try:
      self.driver.get(url)
    except:
      self.s_flow_log = f"测试结束(无法加载URL：{url})"
      return False
    try:
        WebDriverWait(self.driver, 5).until(
        expected_conditions.visibility_of_element_located((By.ID, 'button-1051-btnInnerEl'))
      )
    except TimeoutException:
      self.s_flow_log = "测试结束(等待超时，网页加载异常)"
      return False
    return True

  def element_begin(self):
    #noinspection PyBroadException
    try:
      for i in range(3):
        self.bt_begin = self.driver.find_element(By.ID, 'button-1051-btnInnerEl')
        break
    except:
      self.s_flow_log = "测试结束(获取开始按钮异常！！！)"
      return False
    if self.bt_begin.text != "开始":
      self.s_flow_log = f"""测试结束({self.values.flow_input_ip}测试被占用)"""
      return False
    if self.bt_begin.text != "开始":
      self.s_flow_log = "测试结束(开始按钮未识别！！！)"
      return False
    #noinspection all
    try:
      #noinspection all
      input_time = self.driver.find_element(By.ID, 'numberfield-1075-inputEl')
      input_time.clear()
      input_time.send_keys(self.values.flow_input_sec)
    except:
      self.s_flow_log = "测试结束(设置测试时长异常！！！)"
      return False
    self.time_begin = datetime.now() - timedelta(seconds=30)
    #noinspection PyBroadException
    try:
      self.bt_begin.click()
    except:
      self.s_flow_log = "测试结束(开始按钮按下异常！！！)"
      return False
    for i in range(3):
      self.s_flow_log = f"测试按钮按下延时({i})"
      time.sleep(1)
    return True

  def element_wait(self):
    #noinspection PyBroadException
    try:
      while self.bt_begin.text != "开始":
        text_time = self.driver.find_element(By.ID, 'component-1084')
        self.s_flow_log = f"等待测试完成({text_time.text})"
        time.sleep(1)
        if self.sq_end:
          self.bt_begin.click()
          self.s_flow_log = "测试结束(中断)"
          self.sq_end = False
          return False
      return True
    except:
      self.s_flow_log = "测试结束(测试状态监控异常)"
      return False

  def element_page(self):
    list_id=["tab-1379-btnInnerEl",'tab-1408-btnInnerEl']
    for id_x in list_id:
      # noinspection all
      try:
        tab_log = self.driver.find_element(By.ID, id_x)
        tab_log.click()
        time.sleep(2)
        return True
      except:
        pass
    self.s_flow_log = f"测试结束(无法找到日志页面{list_id})"
    return False

  def element_df_get_table(self):
    # noinspection all
    list_id= []
    list_id.append('[style*="width: 2372px; transform: translate3d(0px, 0px, 0px);"]')
    #新日志界面里的table
    list_id.append('[style*="width: 2232px; transform: translate3d(0px, 0px, 0px);"]')
    #width: 2372px; transform: translate3d(0px, 0px, 0px);
    #width: 2232px; transform: translate3d(0px, 0px, 0px);
    for id_x in list_id:
      # noinspection all
      try:
        table = self.driver.find_element(By.CSS_SELECTOR,id_x)
        return table
      except:
        pass
    self.s_flow_log = f"测试结束(无法找到table页面{list_id})"
    return None

  def element_df(self, time_begin):
    list_dic = []
    table = self.element_df_get_table()
    if not table: return None
    #noinspection PyBroadException
    try:

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
          if s_name == "测试结果":
            s_name="bResult"
            dic_a[s_name] = "True" if s_value == "P" else "False"
          else:
            dic_a[s_name] = s_value

        if datetime.strptime(dic_a["开始时间"], "%Y-%m-%d %H:%M:%S")< time_begin:
          return
        bb = element_row.find_element(By.TAG_NAME, 'table')
        trs = bb.find_elements(By.TAG_NAME, 'tr')
        for tr in trs:
          tds = tr.find_elements(By.TAG_NAME, 'td')
          if len(tds) != 2:
            continue
          s_key = tds[0].find_element(By.TAG_NAME, 'b').get_attribute("innerHTML").replace("：", "").replace(" ","")
          if s_key =="序列号":
            s_key = "FSN"
          dic_a[s_key] = tds[1].get_attribute("innerHTML").strip()
        self.s_flow_log = element_class
        list_dic.append(dic_a)
    except Exception:
      self.s_flow_log = "测试结束(获取测试数据异常)"
    finally:
      df = pd.get_df(list_dic)
      return df

  def thread_run(self):
    try:
      if not self.element_driver(): return
      if not self.element_url(): return
      if not self.element_begin(): return
      if not self.element_wait(): return
      if not self.element_page(): return
      df=self.element_df(self.time_begin)
      if not df:return
      sql.set_insert(df, self.values.flow_input_operator,self.values.flow_input_order)
      self.s_flow_log = "测试结束(完成)"
    except Exception as e:
      print(e)
      self.s_flow_log = f"测试结束(异常退出)"
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
dict_testing:{Testing}={}
class Values:
  def __init__(self,s_flow_values=None):
    if s_flow_values is None:
      s_flow_values="10.77.77.108,test,test,1"
    buf = s_flow_values.split(",")
    self.flow_input_ip = buf[0].strip()
    self.flow_input_order = buf[1].strip()
    self.flow_input_operator = buf[2].strip()
    self.flow_input_sec = buf[3].strip()
  def get_testing(self)->Testing:
    if self.flow_input_ip not in dict_testing.keys():
      dict_testing[self.flow_input_ip] = Testing()
    return dict_testing[self.flow_input_ip]