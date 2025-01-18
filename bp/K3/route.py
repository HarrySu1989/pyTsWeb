from flask import Blueprint, jsonify, request
bp = Blueprint('K3', __name__, url_prefix='/K3')
@bp.route('/', methods=['GET', 'POST'])
def index():
  pass