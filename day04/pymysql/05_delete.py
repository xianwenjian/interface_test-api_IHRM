# 导包
import pymysql
# 创建数据库连接
connect = pymysql.connect(host="localhost", user="root", password="root", database="books", port=3306, charset="utf8",
                          autocommit=True)
# 3.获取游标
cursor = connect.cursor()
# 4.执行SQL语句
# 创建查询SQL语句
select_sql = "select id, title, `read`, `comment` from t_book;"
# 执行select_sql
cursor.execute(select_sql)
# 打印删除前的查询结果结果
print("删除前的数据1111: ", cursor.fetchall())

#  删除三体语句
delete_sql = "delete from t_book where title='三体'"
# 执行delete_sql
cursor.execute(delete_sql)

print("=============================================")
# 创建查询SQL语句
select_sql = "select id, title, `read`, `comment` from t_book;"
# 执行select_sql
cursor.execute(select_sql)
# 打印删除后的查询结果结果
print("删除后的数据2222: ", cursor.fetchall())

# 5.关闭游标
cursor.close()
# 6.关闭连接
connect.close()



