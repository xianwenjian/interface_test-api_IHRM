import logging
import unittest
from day06.apiTestIHRM import app
from day06.apiTestIHRM.api.emp_api import EmpAPI
from day06.apiTestIHRM.utils import assert_common, read_add_emp_data, read_query_emp_data, read_modify_emp_data, \
    DBUtils, read_delete_emp_data
from parameterized import parameterized


class TestIHRMEmp2(unittest.TestCase):
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
    @parameterized.expand(read_add_emp_data)
    def test01_add_emp(self, username, mobile, http_code, succes, code, message):
        # 调用添加员工接口
        response = self.emp_api.add_emp(username, mobile)
        logging.info("parameterized添加员工接口返回的数据为: {}".format(response.json()))

        # 断言
        assert_common(self, response, http_code, succes, code, message)

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
    @parameterized.expand(read_query_emp_data)
    def test02_query_emp(self, http_code, succes, code, message):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 打印日志
        logging.info("parameterized查询员工接口返回的数据为: {}".format(response.json()))

        # 断言
        assert_common(self, response, http_code, succes, code, message)

    # 修改员工
    @parameterized.expand(read_modify_emp_data)
    def test03_modify_emp(self, username, http_code, success, code, message):
        # 调用修改员工接口
        response = self.emp_api.modify_emp(username)
        # 打印
        logging.info("parameterized修改员工接口返回的数据为： {}".format(response.json()))

        # 断言
        assert_common(self, response, http_code, success, code, message)
        # 断言数据库中的数据
        with DBUtils('182.92.81.159', 'readuser', 'iHRM_user_2019', 'ihrm') as db:
            # 执行查询语句
            query_sql = "select username from bs_user where id={} limit 1".format(app.EMPID)
            db.execute(query_sql)
            result = db.fetchone()
        logging.info("----------------查询数据库中员工id为{} 的username是：{}".format(app.EMPID, result[0]))

        # 断言数据库中返回的数据
        self.assertEqual(username, result[0])

    # 删除员工
    @parameterized.expand(read_delete_emp_data)
    def test04_delete_emp(self, http_code, success, code, message):
        # 调用删除员工接口
        response = self.emp_api.delete_emp()
        # 打印
        logging.info("parameterized删除员工接口返回的数据为： {}".format(response.json()))
        # 断言
        assert_common(self, response, http_code, success, code, message)