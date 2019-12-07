# 访问TPshop接口 获取登陆接口
# 导包
import requests

# 发送post请求
data01 = {"username": "15627672674", "password": "123456", "verify_code": "1234"}
response2 = requests.post("http://localhost/index.php?m=Home&c=User&a=do_login", data=data01)
# 打印响应体数据
print("text = ", response2.text)
print("返回json数据: ", response2.json())
