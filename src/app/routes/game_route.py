# FES/src/app/routes/game_route.py
from flask import Blueprint
game_bp = Blueprint('game', __name__)  # 定义蓝图

@game_bp.route('/test')
def game_test():
    return "Game Route Works!"
