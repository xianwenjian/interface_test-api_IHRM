"""
使用unittest编写代码测试注册接口测试用例，并在注册成功后，根据服务器返回的user_id，查询数据库，
获取该用的 nickname 是否为注册时，输入的username
要求：
至少包括以下测试点：
1，电信，联通，移动3种手机号码（3个测试用例）
2，缺少图片验证码时进行注册（1个缺少必填参数的案例）
3，增加无效参数进行注册（多参测试）
4，手机号码已存在（数据异常测试）
断言数据参考：
1，包括http响应状态码，status，message
2，注册成功的正向案例，必须还根据响应数据的user_id，断言数据库中的nickname是否为注册时填写的username

注意：由于没有接口文档，就以实际各类注册用例的返回结果为预期结果进行断言，但是要有常识。

接口调用流程：先调用注册的获取验证码接口->再调用注册接口
注册用获取验证码接口参考：http://localhost/index.php?m=Home&c=User&a=verify&type=user_reg
注册接口参考：http://localhost/index.php/Home/User/reg.html
请求头：{"Content-Type":"application/x-www-form-urlencoed"}
请求体：参考postman，注意转换成字典的格式

使用到的技术：
requests
代码操作数据库
unittest断言
实战中，数据重复的处理（删数据库，小心点儿，别删错了）
"""

# 导包
import unittest
import requests


# 定义一个测试类  注册
class TestTPshonRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session = requests.Session()
        cls.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify&type=user_reg"
        cls.register_url = "http://localhost/index.php/Home/User/reg.html"

    def tearDown(self):
        # 关闭session
        self.session.close()

    # 手机号码正常注册
    def test01_verify(self):
        # 获取验证码的对象
        response_verify = self.session.get(self.verify_url)
        # 打印返回的验证码信息
        print("验证码信息: ", response_verify.headers.get("Content-Type"))
        # 断言
        self.assertIn("image", response_verify.headers.get("Content-Type"))
        # 注册
        data = {"scene": 1, "username": "13400000004", "verify_code": "8888", "password": "123456",
                "password2": "123456", "invite": "15627672674"}
        response_register = self.session.post(self.register_url, data=data)
        # 获取注册返回的信息
        result_json = response_register.json()
        print("注册返回的json信息: ", result_json)

        # 断言
        # 断言状态码
        self.assertEqual(200, response_register.status_code)
        # 断言 nickname
        self.assertEqual(data.get("username"), result_json.get("result").get("nickname"))







        # 缺少图片验证码时进行注册（1个缺少必填参数的案例）
        # def test02_lack_verify(self):
        #     # 注册
        #     data = {"username": "13511110009", "password": "123456", "password2": "123456"}
        #     response_register = self.session.get(self.register_url, data=data)
