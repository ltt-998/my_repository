# 民宿：189100   酒店：189101   别墅：189102
# 只筛选100：已上架，200：下架，300：风险下架

from get_conf import GetConf

conf_path = r'F:\py_project\Sort\sort_conf'
cycle_conf = GetConf(conf_path)

num_cycle, sale_cycle, collect_cycle, visitor_cycle, visit_num_cycle = cycle_conf.get_cycle_1()
print(num_cycle, sale_cycle, collect_cycle, visitor_cycle, visit_num_cycle)


categoty_num = 0
if categoty_num == 0:
    category = cycle_conf.get_conf('CATEGORY', 'homestay_category')
elif categoty_num == 1:
    category = cycle_conf.get_conf('CATEGORY', 'hotel_category')
else:
    category = cycle_conf.get_conf('CATEGORY', 'villa_category')



sql_M_num = '''SELECT A.id goodsId, SUM( C.qty ) AS '商品销量总和' 
FROM xls_goods A
LEFT JOIN xls_travel_goods B ON A.id = B.goods_id
LEFT JOIN xls_order_goods C ON A.id = C.goods_id
WHERE 1 = 1 AND C.create_time BETWEEN (SELECT DATE_SUB((SELECT NOW()),INTERVAL %s DAY)) AND (SELECT NOW())
AND A.goods_status in (100, 200, 300)
AND A.category_code = %s
GROUP BY A.id;''' % (num_cycle, category)


sql_M_sale = '''SELECT A.id goodsId, SUM( D.price_pay_init ) AS '商品销量额总和' 
FROM xls_goods A
LEFT JOIN xls_travel_goods B ON A.id = B.goods_id
LEFT JOIN xls_order_goods C ON A.id = C.goods_id 
LEFT JOIN xls_order D ON C.order_id = D.id
WHERE C.create_time BETWEEN (SELECT DATE_SUB((SELECT NOW()),INTERVAL %s DAY)) AND (SELECT NOW())
AND A.goods_status in (100, 200, 300) 
AND A.category_code = %s
GROUP BY A.id;''' % (sale_cycle, category)


sql_N_collect = '''SELECT collect.goods_id goodsId, count(collect.goods_id) AS '商品收藏量'
FROM xls_goods_collect collect
LEFT JOIN xls_goods A ON collect.goods_id = A.id
LEFT JOIN xls_travel_goods B ON collect.goods_id = B.goods_id
WHERE A.create_time BETWEEN (SELECT DATE_SUB((SELECT NOW()),INTERVAL %s DAY)) AND (SELECT NOW()) 
AND A.goods_status in (100, 200, 300)
AND collect.flag_delete = 0
AND A.category_code = %s
GROUP BY A.id;''' % (collect_cycle, category)


sql_N_visitor = '''SELECT A.goods_id goodsId, count(DISTINCT A.user_id) AS '总访客数'
FROM xls_goods_viewer A
LEFT JOIN xls_goods B ON A.goods_id = B.id
WHERE A.create_time BETWEEN (SELECT DATE_SUB((SELECT NOW()),INTERVAL %s DAY)) AND (SELECT NOW())
AND B.goods_status in (100, 200, 300)
AND B.category_code = %s
GROUP BY goods_id
order by count(DISTINCT A.user_id) DESC;''' % (visitor_cycle, category)


sql_N_visit_num = '''SELECT A.goods_id goodsId, count(A.goods_id) AS '总访问量'
FROM xls_goods_viewer A
LEFT JOIN xls_goods B ON A.goods_id = B.id
WHERE A.create_time BETWEEN (SELECT DATE_SUB((SELECT NOW()),INTERVAL %s DAY)) AND (SELECT NOW())
and B.goods_status in (100, 200, 300)
AND B.category_code = %s
GROUP BY goods_id
order by count(A.goods_id) DESC;''' % (visit_num_cycle, category)






# *************************************************************************************************
sql_M_homestay = '''SELECT A.id AS goodsId, SUM( C.qty ) AS '商品销量总和', SUM( D.price_pay_init ) AS '商品销量额总和'
FROM xls_goods A 
LEFT JOIN xls_travel_goods B ON A.id = B.goods_id 
LEFT JOIN xls_order_goods C ON A.id = C.goods_id 
LEFT JOIN xls_order D ON C.order_id = D.id 
WHERE C.create_time BETWEEN '2021-04-09 00:00:00' AND (SELECT NOW()) 
AND A.goods_status IN ( 100, 200, 300 ) 
AND A.category_code = '189100' 
GROUP BY A.id;'''

sql_M_hotel = '''SELECT A.id AS goodsId, SUM( C.qty ) AS '商品销量总和', SUM( D.price_pay_init ) AS '商品销售额总和' 
FROM xls_goods A 
LEFT JOIN xls_travel_goods B ON A.id = B.goods_id 
LEFT JOIN xls_order_goods C ON A.id = C.goods_id 
LEFT JOIN xls_order D ON C.order_id = D.id 
WHERE C.create_time BETWEEN '2021-04-09 00:00:00' AND (SELECT NOW()) 
AND A.goods_status IN ( 100, 200, 300 ) 
AND A.category_code = '189101' 
GROUP BY A.id;'''

sql_M_villa = '''SELECT A.id AS goodsId, SUM( C.qty ) AS '商品销量总和', SUM( D.price_pay_init ) AS '商品销售额总和' 
FROM xls_goods A 
LEFT JOIN xls_travel_goods B ON A.id = B.goods_id 
LEFT JOIN xls_order_goods C ON A.id = C.goods_id 
LEFT JOIN xls_order D ON C.order_id = D.id 
WHERE C.create_time BETWEEN '2021-04-09 00:00:00' AND (SELECT NOW()) 
AND A.goods_status IN ( 100, 200, 300 ) 
AND A.category_code = '189102' 
GROUP BY A.id'''

sql_N_homestay = '''SELECT A.id goodsId, count( DISTINCT B.user_id ) AS '访客数总和(去重)', count(B.id) AS '访客数总和(不去重)'
FROM xls_goods A
INNER JOIN xls_goods_viewer B ON A.id = B.goods_id 
WHERE A.create_time BETWEEN '2021-04-09 00:00:00' 
AND (SELECT NOW()) -- 只筛选100：已上架，200：下架，300：风险下架
AND A.goods_status IN ( 100, 200, 300 ) 
AND A.category_code = '189100'
GROUP BY A.id;'''

sql_N_hotel = '''SELECT A.id goodsId, count( DISTINCT B.user_id ) AS '访客数总和(去重)', count(B.id) AS '访客数总和(不去重)'
FROM xls_goods A
INNER JOIN xls_goods_viewer B ON A.id = B.goods_id 
WHERE A.create_time BETWEEN '2021-04-09 00:00:00' 
AND (SELECT NOW()) -- 只筛选100：已上架，200：下架，300：风险下架
AND A.goods_status IN ( 100, 200, 300 ) 
AND A.category_code = '189101'
GROUP BY A.id;'''

sql_N_villa = '''SELECT A.id goodsId, count( DISTINCT B.user_id ) AS '访客数总和(去重)', count(B.id) AS '访客数总和(不去重)'
FROM xls_goods A
INNER JOIN xls_goods_viewer B ON A.id = B.goods_id 
WHERE A.create_time BETWEEN '2021-04-09 00:00:00' 
AND (SELECT NOW()) -- 只筛选100：已上架，200：下架，300：风险下架
AND A.goods_status IN ( 100, 200, 300 ) 
AND A.category_code = '189102'
GROUP BY A.id;'''
