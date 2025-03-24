# FES/src/app/main.py
import sys, os
#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 确保 src 在路径中

from  pathlib import  Path
sys.path.append(str(Path(__file__).parent.parent))
#print(sys.path)  # 添加这行代码打印路径列表
from app.models import db
from app.models import user_model
from app import create_app

def test_connection():
    with db as cursor:
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()
        print(f"数据库连接成功！MySQL版本：{result[0]}")

if __name__ == "__main__":
    test_connection()

def test_user_creation():
    # 测试创建用户
    # new_user_id = user_model.create_user(
    #     username="test_user",
    #     email="test@example.com",
    #     password="test123"
    # )
    #print(f"创建用户成功！用户ID：{new_user_id}")

    #测试用户查询
    user =user_model.get_user_by_email("test@example.com")
    print("查询到用户数据",user)


if __name__=="__main__"and not os.environ.get('WERKZEUG_RUN_MAIN'):
    test_user_creation()

app = create_app()

if __name__ =="__main__":
    app.run(debug=True,port=5000)

print("成功导入用户模型",user_model.UserModel)