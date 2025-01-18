from flask import Blueprint, jsonify, request
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
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
  driver.get("www.baidu.com")
  return s_exe