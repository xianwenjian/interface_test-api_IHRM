"""
需求：
1. 使用requests库调用TPshop登录功能的相关接口，完成登录操作
2. 登录成功后获取‘我的订单’页面的数据
3. 要求：使用Session对象来实现
"""

# 获取验证码
# 导包
import requests
# 获取session对象
session = requests.Session()
# get请求  获取验证码
response = session.get("http://localhost/index.php?m=Home&c=User&a=verify")
print("验证码: ", response.cookies)
print("==============")

# 登陆
login_data = {"username": "15627672674", "password": "123456", "verify_code": "8888"}
response_login = session.post("http://localhost/index.php?m=Home&c=User&a=do_login", data=login_data)
print("获取登录返回的数据: ", response_login.json())
print("==============")

# 我的订单
response_my_order = session.get("http://localhost/Home/Order/order_list.html")
print("订单: ", response_my_order.text)

# 关闭会话对象
session.close()

