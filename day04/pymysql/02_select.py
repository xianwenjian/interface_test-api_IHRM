"""
1).连接到数据库（host:localhost username:root password:root database:books）
2).查询图书表的数据（包括：图书id、图书名称、阅读量、评论量）
3).获取查询结果的总记录数
4).获取查询结果的第一条数据
5).获取全部的查询结果
"""

# 1.导包
import pymysql
# 2.创建数据库连接
conn = pymysql.connect(host="localhost", user="root", password="root", database="books", port=3306, charset="utf8")
# 3.获取游标
cursor = conn.cursor()
# 4.执行SQL语句
# 查询图书表数据
query_sql = "select id, title, `read`, `comment` from t_book;"
# 执行查询语句
cursor.execute(query_sql)
# 获取总记录数
count = cursor.rowcount
print("总记录数:%d" % count)
# 查看全部查询结果
book_all_list = cursor.fetchall()
# 输出book_all_list
print("book_all_list {}".format(book_all_list))
# 遍历 book_all_list
for book in book_all_list:
    print("书名:", book[1])
# 获取查询结果的第一条数据
query_one_sql = "select id, title, `read`, `comment` from t_book limit 1;"
# 执行查询一条的SQL语句
cursor.execute(query_one_sql)
print("===============================")
# 打印程序的第一条SQL语句
book = cursor.fetchone()
print("book:{}".format(book))

# 5.关闭游标
cursor.close()
# 6.关闭连接
conn.close()


