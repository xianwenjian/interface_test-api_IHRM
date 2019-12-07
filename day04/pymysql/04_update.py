# 导包
import pymysql

# 创建数据库连接
connect = pymysql.connect(host="localhost", user="root", password="root", database="books", port=3306, charset="utf8",
                          autocommit=True)
# 3.获取游标
cursor = connect.cursor()
# 4.执行SQL语句
# 创建查询语句 更改前
select_sql = "select id, title, `read`, `comment` from t_book where id=4;"
cursor.execute(select_sql)
print("更改前阅读量是:", cursor.fetchone()[2])

# 把三体的阅读量+1
update_sql = "update t_book set `read`=`read`+1 where title='三体';"
# 执行update_sql
cursor.execute(update_sql)
# 创建查询语句
select_sql = "select id, title, `read`, `comment` from t_book where id=4;"
cursor.execute(select_sql)
print("更改后阅读量是:", cursor.fetchone()[2])

# 5.关闭游标
cursor.close()
# 6.关闭连接
connect.close()
