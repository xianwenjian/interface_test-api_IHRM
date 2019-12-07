# transaction 事务
# 1.导包
import pymysql

connect = None
cursor = None
# 2.创建数据库连接
connect = pymysql.connect(host="localhost", user="root", password="root", database="books", port=3306, charset="utf8",
                          autocommit=False)
# 3.获取游标
cursor = connect.cursor()
try:
    # 4.执行SQL语句
    # 添加数据
    add_book_sql = "insert into t_book(id,title,pub_date) values(4, '创新公司', '1986-01-01');"
    add_hero_sql = "insert into t_hero(`name`, gender, book_id) values('乔布斯', 1, 4);"
    # 执行add_book_sql和add_hero_sql
    cursor.execute(add_book_sql)
    cursor.execute(add_hero_sql)
    # 模拟产生异常
    raise Exception("人为模拟产生异常,用来测试抛出异常后，会不会回滚事务")
    # 加上提交语句就可以提交事务
    print("没有异常,数据插入成功")
    connect.commit()
except Exception as e:
    print(e)
    print("出现异常, 数据插入失败")
    connect.rollback()

finally:
    # 5.关闭游标
    if cursor:
        cursor.close()
    # 6.关闭连接
    if connect:
        connect.close()
