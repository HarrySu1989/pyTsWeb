from flask import Blueprint, render_template
from decorators import login_required
bp = Blueprint('flow', __name__, url_prefix='/flow')
@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # guide=Guide()
    # html=guide.get_html()
    # html+=guide.item_gx.get_html_body()
    # return vb.get_view(bp, html)
    return "hello world"
