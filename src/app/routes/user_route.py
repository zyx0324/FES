from flask import Blueprint, request, jsonify,render_template
from app.models import  user_model
import re
user_bp = Blueprint('user', __name__)
@user_bp.route('/test')
def user_test():
   return render_template("register.html")

@user_bp.route('/register', methods=['POST'])
def register():
    """用户注册接口"""
    data = request.json
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, data.get('email', '')):
        return jsonify({
            "code": 400,
            "message": "邮箱格式不正确"
        }), 400
    try:
        user_id = user_model.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        return jsonify({
            "code": 200,
            "user_id": user_id,
            "message": "注册成功"
        }), 200
    except Exception as e:
        return jsonify({
            "code": 500,
            "message": f"注册失败: {str(e)}"
        }), 500
@user_bp.route('/register-page', methods=['GET'])
def register_page():
    return render_template('register.html')