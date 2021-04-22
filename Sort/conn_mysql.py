import pymysql

class ConnMysql():
    def __init__(self, host, port, user, password, database, charset,):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset


    def conn_db(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database, charset=self.charset)
        cur = conn.cursor()
        return conn, cur


    def excute_sql(self,sql):
        conn, cur = self.conn_db()
        cur.execute(sql)
        res = cur.fetchall()
        fields = cur.description
        cur.close()
        conn.close()
        return res, fields


if __name__ == '__main__':
    host = 'rm-wz9ih626njrt6yelujm.mysql.rds.aliyuncs.com'
    port = 3306
    user = 'xls_server_test'
    password = 'xls_server_test'
    database = 'xls_travel_server_dev'
    charset = 'utf8'
    from query_sql import *

    a = ConnMysql(host, port, user, password, database, charset)
    res, fields = a.excute_sql(sql_M_num)
    print(res)
    print(fields)