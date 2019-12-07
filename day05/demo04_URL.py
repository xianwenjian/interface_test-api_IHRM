# 传递URL参数
# 导包
import requests

# 发送get请求
response_code = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
# response = requests.get("http://www.baidu.com/s?wd=python")
# response = requests.get("http://www.baidu.com/s", params="wd=python")
# response = requests.get("https://www.baidu.com/s", params={"wd": "python"})
# 打印数据
print("text = ", response_code.text)
# print("url = ", response.url)
# print("encoding = ", response.encoding)
# print("headers = ", response.headers)
# print("cookies = ", response.cookies)
# print("content = ", response.content)
# print("json = ", response.json())



