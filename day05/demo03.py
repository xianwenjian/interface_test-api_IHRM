# 调用IHRM登陆接口
# 导包
import requests

# 发送post请求,调用IHRM登陆接口,获取返回数据
my_data = {"mobile": "13800000002", "password": "123456"}
response = requests.post("http://182.92.81.159/api/sys/login", json=my_data)
# 打印返回数据
print("text = ", response.text)
print("json = ", response.json())
