"""
1). 访问百度首页的接口`http://www.baidu.com`，获取以下响应数据
2). 获取响应状态码
3). 获取请求URL
4). 获取响应字符编码
5). 获取响应头数据
6). 获取响应的cookie数据
7). 获取文本形式的响应内容
8). 获取字节形式的响应内容
"""
# 导出
import requests
# 发送请求
response = requests.post("http://182.92.81.159/api/sys/login", json={"mobile": "13800000002", "password": "123456"})
# 打印数据  响应内容
print("响应状态码: ", response.status_code)
print("获取请求URL: ", response.url)
print("获取响应字符编码: ", response.encoding)
print("获取响应头数据: ", response.headers)
print("获取响应的cookie数据: ", response.cookies)
print("获取字节形式的响应内容: ", response.content)
print("获取文本形式的响应内容: ", response.text)
print("json数据 : ", response.json())