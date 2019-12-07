import json

import pymysql
from requests import Response

# 断言
from day06.apiTestIHRM import app


def assert_common(self, response, status_code, success, code, message):
    """
    @type response:Response
    """
    jsonData = response.json()  # type:dict
    # 断言响应状态码
    self.assertEqual(status_code, response.status_code)
    # 断言success
    self.assertEqual(success, jsonData.get("success"))
    # 断言code
    self.assertEqual(code, jsonData.get("code"))
    # 断言message
    self.assertEqual(message, jsonData.get("message"))


class DBUtils:
    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(host, user, password, database)

    # __enter__和__exit__这两个魔法函数是pyshon内置函数
    # 打开with时 执行__enter__   退出with时 执行__exit__
    #  使用方法: with DBUtils() as db:
    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


# 登录
def read_login_data():
    login_data_path = app.BASE_DIR + "/data/login_data.json"
    with open(login_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        for login_data in jsonData:
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            http_code = login_data.get("http_code")
            success = login_data.get("succes")
            code = login_data.get("code")
            message = login_data.get("message")
            result_list.append((mobile, password, http_code, success, code, message))
    print("result_list的值为: ", result_list)
    return result_list


# read_login_data()


# 添加员工
def read_add_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        # 使用json工具读取数据文件, 加载成json的数据类型
        jsonData = json.load(f)
        result_list = []
        add_emp_data = jsonData.get("add_emp")
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        result_list.append((username, mobile, http_code, success, code, message))
    print("add_emp  result_list的值为: ", result_list)
    return result_list


read_add_emp_data()


# 查询员工
def read_query_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        # 使用json工具读取数据文件, 加载成json的数据类型
        jsonData = json.load(f)
        result_list = []
        query_emp_data = jsonData.get("query_emp")
        http_code = query_emp_data.get("http_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        result_list.append((http_code, success, code, message))
    print("query emp data(查询): ", result_list)
    return result_list


read_query_emp_data()


# 修改员工
def read_modify_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        modify_emp_data = jsonData.get("modify_emp")
        username = modify_emp_data.get("username")
        http_code = modify_emp_data.get("http_code")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        result_list.append((username, http_code, success, code, message))

    print("modify emp data: ", result_list)
    return result_list


read_modify_emp_data()


# 删除员工
def read_delete_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        delete_emp_data = jsonData.get("query_emp")
        http_code = delete_emp_data.get("http_code")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        result_list.append((http_code, success, code, message))

    print("delete emp data: ", result_list)
    return result_list


read_delete_emp_data()
