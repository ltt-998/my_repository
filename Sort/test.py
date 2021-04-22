import pymysql

# host = 'rm-wz9ih626njrt6yelujm.mysql.rds.aliyuncs.com'
# port = 3306
# user = 'xls_server_test'
# password = 'xls_server_test'
# database = 'xls_travel_server_dev'
# charset = 'utf8'
#
# import configparser
#
#
# cf = configparser.ConfigParser()
# cf.read(r'F:\py_project\Sort\sort_conf', encoding='utf-8')
#
# num_cycle = cf.get('CYCLE', 'num_cycle')
# print(num_cycle)
#
# categoty_num = 0
# if categoty_num == 0:
#     category = cf.get('CATEGORY','homestay_category')
#     print(category)
#
#
# conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset=charset)
# cur = conn.cursor()
#
# sql_M_num = f'''SELECT A.id goodsId, SUM( C.qty ) AS '商品销量总和'
# FROM xls_goods A
# LEFT JOIN xls_travel_goods B ON A.id = B.goods_id
# LEFT JOIN xls_order_goods C ON A.id = C.goods_id
# WHERE 1 = 1 AND C.create_time BETWEEN (SELECT DATE_SUB((SELECT NOW()),INTERVAL %s DAY)) AND (SELECT NOW())
# AND A.goods_status in (100, 200, 300)
# AND A.category_code = %s
# GROUP BY A.id;''' % (num_cycle, category)
#
# cur.execute(sql_M_num)
#
# res = cur.fetchall()
# print(res)

import xlwt

wb = xlwt.Workbook()
sheet_1 = wb.add_sheet('xx_1',cell_overwrite_ok=True)
sheet_2 = wb.add_sheet('xx_2',cell_overwrite_ok=True)
wb.save(r'F:\py_project\Sort\test001.xls')
print('ok')







