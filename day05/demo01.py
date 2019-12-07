# 导包
import requests

# 发送get请求
response = requests.get("https://www.baidu.com/?tn=sitehao123&H123Tmp=nunew11")
# 打印响应体
print(response.text)
