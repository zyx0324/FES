# FES/src/app/routes/__init__.py
from .user_route import user_bp
from .game_route import game_bp
from .cos_route import cos_bp

__all__ = ['user_bp', 'game_bp', 'cos_bp']  # 使用列表格式
