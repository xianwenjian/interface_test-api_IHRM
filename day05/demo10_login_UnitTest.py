# 导包
import requests
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        # 创建会话对象
        self.session = requests.Session()
        # 验证码网址
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        # 登录网址
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self):
        # 关闭会话对象
        self.session.close()

    # 成功登录
    def test_login_success(self):
        # 获取验证码
        response_verify = self.session.get(self.verify_url)
        print("01--type=", response_verify.headers.get("Content-Type"))
        # 断言返回的是否是验证码图片
        self.assertIn("image", response_verify.headers.get("Content-Type"))

        # 登录
        data = {"username": "15627672674", "password": "123456", "verify_code": "8888"}
        response_login = self.session.post(self.login_url, data=data)
        result = response_login.json()
        print("01--login response data=", result)
        # 断言
        self.assertEqual(200, response_login.status_code)
        self.assertEqual(1, result.get("status"))
        self.assertEqual("登陆成功", result.get("msg"))

    # 账号不存在
    def test_login_username_is_not_exist(self):
        # 获取验证码
        response = self.session.get(self.verify_url)
        print("_02--type=", response.headers.get("Content-Type"))
        self.assertIn("image", response.headers.get("Content-Type"))
        # 登录
        data = {"username": "13377771111", "password": "123456", "verify_code": "8888"}
        response = self.session.post(self.login_url, data=data)
        result = response.json()
        print("02--login response data=", result)

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, result.get("status"))
        self.assertIn("账号不存在", result.get("msg"))

    # 密码错误
    def test_login_pwd_is_error(self):
        # 获取验证码
        response = self.session.get(self.verify_url)
        print("03--type=", response.headers.get("Content-Type"))
        self.assertIn("image", response.headers.get("Content-Type"))
        # 登录
        data = {"username": "15627672674", "password": "error", "verify_code": "8888"}
        response = self.session.post(self.login_url, data=data)
        result = response.json()
        print("03--login response data=", result)
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, result.get("status"))
        self.assertIn("密码错误", result.get("msg"))
