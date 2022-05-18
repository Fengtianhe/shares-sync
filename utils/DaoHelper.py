import os
import pymysql
import configparser


class DaoHelper:
    """
    处理数据库
    """

    def __init__(self):
        root_dir = os.path.dirname(os.path.abspath('./shares-sync'))
        config_path = os.path.join(root_dir, "config/db.ini")
        cf = configparser.ConfigParser()
        cf.read(config_path)

        self.conn = pymysql.connect(host=cf.get("mysql", "host"),
                                    user=cf.get("mysql", "user"),
                                    password=cf.get("mysql", "password"),
                                    db=cf.get("mysql", "db"),
                                    port=cf.getint("mysql", "port"),
                                    charset=cf.get("mysql", "charset"),
                                    cursorclass=pymysql.cursors.DictCursor)

        # 定义游标
        self.cursor = self.conn.cursor()

    def select(self, sql, arg=None, is_more=False):
        """

        :param sql: sql语句，字符类型
        :param arg: sql语句的参数，为序列类型
        :param is_more: False or True
        :return: 字典类型或者嵌套字典的列表
        """
        self.cursor.execute(sql, arg)
        self.conn.commit()

        if is_more:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()

        return result

    def execute(self, sql, arg=None):
        self.cursor.execute(sql, arg)
        self.conn.commit()

    def close(self):
        """
        关闭连接
        :return:
        """
        self.cursor.close()
        self.conn.close()
