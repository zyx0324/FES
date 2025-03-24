import pymysql
from app.config import DB_CONFIG

class Database:
    def __enter__(self):
        self.conn = pymysql.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.cursor.close()
        self.conn.close()
