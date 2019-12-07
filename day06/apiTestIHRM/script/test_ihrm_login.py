# 导包
import logging
import unittest
import requests
from day06.apiTestIHRM.api.login_api import LoginApi
from day06.apiTestIHRM.utils import assert_common
from day06.apiTestIHRM import app


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
    def test01_login_success(self):
        # 调用方法 获取response对象
        response = self.login_api.login("13800000002", "123456")
        logging.info("1登录接口返回的json数据是: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功！")

        # 获取json数据
        jsonData = response.json()
        # 拼接 token 组成全局变量
        token = "Bearer " + jsonData.get('data')
        # 把token保存到全局变量app.py中
        # 先要在app.py中创建 HEADERS 变量才能保存
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        logging.info("保存登录的token和Content-Type: {}".format(app.HEADERS))

    # 账户名错误
    def test02_mobile_is_error(self):
        response = self.login_api.login("13900000002", "123456")
        logging.info("2登录接口返回的json数据是: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码错误
    def test03_password_is_error(self):
        response = self.login_api.login("13800000002", "000000")
        logging.info("3登录接口返回的json数据是: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    # 参数为空
    def test04_none_params(self):
        response = self.login_api.login_none_params()
        logging.info("4登录接口返回的json数据是: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")

    # 账号为空
    def test05_mobile_is_null(self):
        response = self.login_api.login("", "000000")
        logging.info("5登录接口返回的json数据是: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test06_password_is_null(self):
        # 发送登陆请求
        response = self.login_api.login("13800000002", "")
        # 打印日志
        logging.info("6登录接口返回的json数据是: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参
    def test07_extra_params(self):
        # 调用方法 获取response对象
        response = self.login_api.login_extra_params()
        logging.info("7登录接口返回的json数据是: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功！")

    # 少参
    def test08_less_params(self):
        # 调用方法 获取response对象
        response = self.login_api.login_less_params()
        logging.info("8登录接口返回的json数据是: {}".format(response.json()))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")
