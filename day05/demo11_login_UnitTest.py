# 导包
import unittest
import requests


# 定义一个登陆的类
class TestTPshopLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 创建会话对象
        cls.session = requests.Session()
        # 验证码网址
        cls.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        # 登录网址
        cls.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self):
        # 关闭session
        self.session.close()

    # 登录成功
    def test01_login_succeed(self):
        # 调用验证码接口,获取验证码
        response_verify = self.session.get(self.verify_url)
        # 打印获取到的验证码信息
        print("登陆成功的text = ", response_verify.headers.get("Content-Type"))
        # 断言验证码是否包含 image
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 登录
        data = {"username": "15627672674", "password": "123456", "verify_code": "8888"}
        response_login = self.session.post(self.login_url,data=data)
        # 打印登录返回的数据
        json_result = response_login.json()
        print("登录成功返回的json数据:", json_result)
        # 断言
        self.assertEqual("登陆成功", json_result.get("msg"))
        self.assertEqual(1, json_result.get("status"))
        self.assertEqual(200, response_login.status_code)

    # 账号不存在
    def test02_account_not_exist(self):
        # 调用验证码接口  获取验证码
        response_verify = self.session.get(self.verify_url)
        # 打印获取的验证码信息
        print("账号不存在中的验证码text = : ", response_verify.headers.get("Content-Type"))
        # 断言
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 登录
        data = {"username": "15600002222", "password": "123456", "verify_code": "8888"}
        response_login = self.session.post(self.login_url,data=data)
        # 打印登陆后是json数据
        json_result = response_login.json()
        print("账号不存在返回的json数据: ", json_result)
        # 断言
        self.assertEqual(-1, json_result.get("status"))
        self.assertIn('账号不存在', json_result.get("msg"))
        self.assertEqual(200, response_login.status_code)

    # 密码错误
    def test03_password_error(self):
        # 获取验证码
        response_verify = self.session.get(self.verify_url)
        # 打印验证码信息
        print("密码错误的验证码信息: ", response_verify.headers.get("Content-Type"))
        # 断言
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 登录
        data = {"username": "15627672674", "password": "000000", "verify_code": "8888"}
        response_login = self.session.post(self.login_url,data=data)
        # 打印登录返回的json信息
        json_result = response_login.json()
        print("密码错误的json信息: ", json_result)
        # 断言
        self.assertIn("密码错误", json_result.get("msg"))
        self.assertEqual(-2, json_result.get("status"))
        self.assertEqual(200, response_login.status_code)












