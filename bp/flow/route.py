from flask import Blueprint, render_template
from decorators import login_required
import glb.ViewBase as vb

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
bp = Blueprint('flow', __name__, url_prefix='/flow')
@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # guide=Guide()
    # html=guide.get_html()
    # html+=guide.item_gx.get_html_body()
    # return vb.get_view(bp, html)
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1200,1000")
    service = Service('./bp/flow/chromedriver-130.0.6723.91.exe')
    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.get("https://www.baidu.com")

    return vb.get_view(bp, "hello world")
