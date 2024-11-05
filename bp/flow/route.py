from flask import Blueprint, render_template
from decorators import login_required
import glb.ViewBase as vb
import glb.uc as uc
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

bp = Blueprint('flow', __name__, url_prefix='/flow')


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
# <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>  <!-- 引入jQuery库 -->
#
  current_directory = os.path.dirname(os.path.realpath(__file__))
  print(current_directory)
  html = f"""
  <label for="example-textbox">工单:</label>
  <input type="text" id="example-textbox" name="example-textbox">
  <button id="update-button">开始测试</button>
  <script src="/static/jquery-3.6.0.min.js"></script>
  <script src="/static/flow.js"></script>
"""
  return vb.get_view(bp, html)
