#auther: Manlou
#date: 2020/10/20

import pymysql
from warnings import filterwarnings

# 忽略Mysql告警信息
filterwarnings("ignore", category=pymysql.Warning)


class MysqlDb:

    def __init__(self):
        # 建立数据库连接
        self.conn = pymysql.connect("127.0.0.1", "root", "789852123@a", "autotest")

        # 使用 cursor 方法获取操作游标，得到一个可以执行sql语句，并且操作结果作为字典返回
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

    def query(self, sql, state="all"):
        """
        查询
        :param sql: 查询语句
        :param state: all是默认查询全部
        :return:
        """
        self.cur.execute(sql)

        if state == "all":
            # 查询全部
            data = self.cur.fetchall()
        else:
            # 查询单条
            data = self.cur.fetchone()
        return data

    def execute(self, sql):
        """
        更新、删除、新增
        :param sql:
        :return:
        """
        print(sql)
        try:
            # 使用execute操作sql
            rows = self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
            return rows
        except Exception as e:
            print("数据库操作异常 {0}".format(e))
            # 回滚修改
            self.conn.rollback()


if __name__ == '__main__':
    mydb = MysqlDb()
    r = mydb.query("select * from `case`")
    r1 = mydb.execute("insert into `case` (`app`) values('cg')")
    print(r, r1)
