# cookie
"""
相关接口：
获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
登录：http://localhost/index.php?m=Home&c=User&a=do_login
我的订单：http://localhost/Home/Order/order_list.html
获取cookie数据：
response.cookies
添加cookie数据：
requests.post(url, cookies={"c1": "v1"})
"""
# 导包
import requests

# 请求 获取验证码
response_code = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
# 获取cookie数据
cookies = response_code.cookies
print("cookie :", cookies)

# 调用登录接口
data01 = {"username": "15627672674", "password": "123456", "verify_code": "8888"}
response_login = requests.post("http://localhost/index.php?m=Home&c=User&a=do_login", data=data01, cookies=cookies)

# 调用我的订单页面
response_order = requests.get("http://localhost/Home/Order/order_list.html", cookies=cookies)

# 打印结果
print("验证码: ", response_code.content)
print("登陆结果:", response_login.json())
print('登陆页面:', response_order.text)
