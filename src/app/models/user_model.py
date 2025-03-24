from .database import Database

class UserModel:
    def create_user(self, username, email, password):
        """
        创建新用户
        :param username: 用户名 (对应users表的username字段)
        :param email: 邮箱 (对应users表的email字段)
        :param password: 密码 (对应users表的password字段)
        :return: 新用户的user_id
        """
        with Database() as cursor:
            sql = """INSERT INTO users 
                     (username, email, password) 
                     VALUES (%s, %s, %s)"""
            cursor.execute(sql, (username, email, password))
            return cursor.lastrowid

    def get_user_by_email(self, email):
        """
        通过邮箱查询用户
        :param email: 用户注册邮箱
        :return: 用户数据字典 或 None
        """
        with Database() as cursor:
            sql = "SELECT * FROM users WHERE email = %s"
            cursor.execute(sql, (email,))
            return cursor.fetchone()
