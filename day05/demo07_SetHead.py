"""
需求：
1. 请求IHRM项目的登录接口，URL： http://182.92.81.159/api/sys/login
2. 请求头： Content-Type: application/json
3. 请求体： {"mobile":"13800000002", "password":"123456"}
"""

# 导包
import requests

# post请求
data01 = {"mobile": "13800000002", "password": "123456"}
response = requests.post("http://182.92.81.159/api/sys/login", json=data01, headers={"Content-Type": "application/json"}
                         )
# 打印数据
print("json: ", response.json())
print("head :", response.headers)