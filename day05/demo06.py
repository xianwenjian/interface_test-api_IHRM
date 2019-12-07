# 导包
import requests
# get请求 天气
response = requests.get("http://www.weather.com.cn/data/sk/101010100.html")
# 打印数据
print("json数据:", response.json())
print("响应状态码:", response.status_code)
print("字符集:", response.encoding)

# 设置字符集为utf-8
# response.encoding = "utf-8"
# print("设置后的字符集:", response.encoding)
# print("设置后的json数据: ", response.json())

# 使用字节码自带的 decode 方法实现utf-8字符集的转并打印
print("使用字节码自带的 方法实现utf-8字符集的转并打印: ", response.content.decode(encoding='utf-8'))

