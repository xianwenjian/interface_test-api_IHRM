"""
1 使用pymysql连接ihrm数据库，查询员工表中第100条到第110条数据

host:182.92.81.159
username：readuser
password：iHRM_user_2019
数据库：ihrm
表：bs_user
"""
# 1.导包
import pymysql

# 2.创建数据库连接
connect = pymysql.connect(host="182.92.81.159", user="readuser", password="iHRM_user_2019", database="ihrm")
# 3.获取游标
cursor = connect.cursor()
# 4.执行SQL语句
# 查询员工表中第100条到第110条数据
ihrm_sql = "select * from bs_user limit 10,10;"
# 执行ihrm_sql
cursor.execute(ihrm_sql)
# 打印
print("总数", cursor.rowcount)
print(cursor.fetchall())

# 关闭游标
cursor.close()
# 6.关闭连接
connect.close()
