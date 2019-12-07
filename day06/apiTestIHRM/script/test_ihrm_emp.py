# 导包
import logging
import unittest
import pymysql
from day06.apiTestIHRM import app
from day06.apiTestIHRM.api.emp_api import EmpAPI
from day06.apiTestIHRM.utils import assert_common
from day06.apiTestIHRM.utils import DBUtils


class TestIHRMEmp(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.emp_api = EmpAPI()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # 添加员工
    def test01_add_emp(self):
        # 调用添加员工接口
        response = self.emp_api.add_emp("哪吒xwj66677", "13844440010")
        logging.info("添加员工接口返回的数据为: {}".format(response.json()))

        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功！")

        # 获取添加员工接口返回的json数据
        jsonData = response.json()
        # 获取员工id
        emp_id = jsonData.get('data').get('id')
        # 保存id到全局变量
        # 需要先创建一个员工id到app.py中 然后导入app
        app.EMPID = emp_id
        # 打印查看有没有保存成功
        logging.info("保存员工的id: {}".format(app.EMPID))

    # 查询员工
    def test02_query_emp(self):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 打印日志
        logging.info("查询员工接口返回的数据: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功！")

    # 修改员工
    def test03_modify_emp(self):
        # 调用修改员工接口 要传参
        response = self.emp_api.modify_emp("奥特曼888")
        # 打印日志
        logging.info("修改员工接口返回的数据: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功！")

        with DBUtils("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm") as db:
            # 执行查询语句
            query_sql = "select username from bs_user where id={} limit 1".format(app.EMPID)
            db.execute(query_sql)
            result = db.fetchone()

        # 打印日志
        logging.info("-------查询数据库中员工id为{} 的username是: {}".format(app.EMPID, result[0]))

        # 断言
        self.assertEqual("奥特曼888", result[0])

    # 删除员工
    def test04_delete_emp(self):
        # 调用修改员工接口
        response = self.emp_api.delete_emp()
        logging.info("删除员工接口返回的数据: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功！")
