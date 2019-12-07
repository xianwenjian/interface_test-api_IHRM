import logging
import unittest
from parameterized import parameterized

from day06.apiTestIHRM import app
from day06.apiTestIHRM.api.login_api import LoginApi
from day06.apiTestIHRM.utils import read_login_data, assert_common


class TestIHRMLogin(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        # 实例化LoginApi对象
        cls.login_api = LoginApi()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # 登陆成功
    @parameterized.expand(read_login_data)
    def test01_login_success(self, mobile, password, http_code, succes, code, message):
        # 调用方法 获取response对象
        response = self.login_api.login(mobile, password)
        logging.info("111登录接口返回的json数据是: {}".format(response.json()))
        # 断言
        assert_common(self, response, http_code, succes, code, message)

        # 获取json数据
        jsonData = response.json()
        # 拼接 token 组成全局变量
        token = "Bearer " + jsonData.get('data')
        # 把token保存到全局变量app.py中
        # 先要在app.py中创建 HEADERS 变量才能保存
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        logging.info("保存登录的token和Content-Type: {}".format(app.HEADERS))