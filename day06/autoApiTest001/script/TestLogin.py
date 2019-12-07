import unittest
import requests
from day06.autoApiTest001.api.login_api import LoginApi
from day06.autoApiTest001.utils import assert_common


class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        # 实例化LoginApi
        cls.login_api = LoginApi()
        cls.session = requests.Session()

    def tearDown(self):
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        pass

    # 登录成功
    def test01_login_success(self):
        # 调用获取验证码接口
        response_verify = self.login_api.get_login_verify(self.session)
        # 断言验证码是否正确
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 调用获取登录接口
        response_login = self.login_api.login(self.session, "15627672674", "123456", "8888")
        result = response_login.json()
        print(result)
        # 断言
        assert_common(self,response_login, 200, 1, "登陆成功")

    # 账号不存在
    def test02_account_exist(self):
        # 调用获取验证码接口
        response_verify = self.login_api.get_login_verify(self.session)
        # 断言验证码是否正确
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 调用获取登录接口
        response_login = self.login_api.login(self.session, "15600093333", "123456", "8888")
        result = response_login.json()
        print(result)
        # 断言
        assert_common(self, response_login, 200, -1, "账号不存在!")

    # 密码错误
    def test03_password_error(self):
        # 调用获取验证码接口
        response_verify = self.login_api.get_login_verify(self.session)
        # 断言验证码是否正确
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 调用获取登录接口
        response_login = self.login_api.login(self.session, "15627672674", "222222", "8888")
        result = response_login.json()
        print(result)
        # 断言
        assert_common(self, response_login, 200, -2, "密码错误!")
