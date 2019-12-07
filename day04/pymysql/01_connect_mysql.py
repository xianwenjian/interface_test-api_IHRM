# 1.导包
import pymysql

# 2.创建数据库链接
conn = pymysql.connect(host="localhost", user="root", password="root", database="books", port=3306, charset="utf8")
# 3.获取游标
cursor = conn.cursor()
# 4.执行SQL语句
sql = "select version();"
result = cursor.execute(sql)
version = cursor.fetchone()
print("result = ", result)
print(version)
print("version = ", version[0])
# 5.关闭游标
cursor.close()
# 6.关闭连接
conn.close()
