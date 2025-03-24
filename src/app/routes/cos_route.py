# FES/src/app/routes/cos_route.py
from flask import Blueprint
cos_bp = Blueprint('cos', __name__)  # 定义蓝图

@cos_bp.route('/test')
def cos_test():
    return "COS Route Works!"
