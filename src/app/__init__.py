# FES/src/app/__init__.py
from flask import Flask
#from app.routes import user_bp, game_bp, cos_bp  # 从 app 包开始导入

import os

def create_app():
    from .routes.user_route import user_bp
    from .routes.game_route import game_bp
    from .routes.cos_route import cos_bp
    app = Flask(__name__)
    app.static_folder='static'
    app.secret_key = os.urandom(24)

    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(game_bp, url_prefix='/api/game')
    app.register_blueprint(cos_bp, url_prefix='/api/cos')

    return app
