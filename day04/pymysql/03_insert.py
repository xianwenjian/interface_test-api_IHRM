# 1.导包
import pymysql

# 2.创建数据库链接
conn = pymysql.connect(host="localhost", user="root", password="root", database="books", port=3306, charset="utf8",
                       autocommit=True)
# 3.获取游标
cursor = conn.cursor()
# 4.执行SQL语句
# 新增一条图书数据
insert_sql = "insert into t_book(id,title,pub_date) values(4, '三体', '1986-01-01');"
# 执行插入的语句
cursor.execute(insert_sql)
# 查询执行结果
query_sql = "select * from t_book;"
# 执行查询语句
cursor.execute(query_sql)
print("打印的图书有: {}".format(cursor.fetchall()))

# 5.关闭游标
cursor.close()
# 6.关闭连接
conn.close()
