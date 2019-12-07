# 其他请求
# 导包
import requests
# 发送请求
response_put = requests.put("https://www.baidu.com", data={"key":"value"})
response_delete = requests.put("https://www.baidu.com")
response_head = requests.head("https://www.baidu.com")

#打印返回数据
print("response_delete:  ", response_delete.text)
print("headers = ", response_delete.headers)
print("response_head是否有响应体:", response_head.text)





