"""
这是登录模块
"""

import requests


class LoginApi:
    def __init__(self):
        self.login_url = "http://182.92.81.159" + "/api/sys/login"

    # 登录模块
    def login(self, mobile, password):
        login_data = {"mobile": mobile, "password": password}
        return requests.post(self.login_url, json=login_data, headers={"Content-Type": "application/json"})

    # 没有参数
    def login_none_params(self):
        return requests.post(self.login_url, headers={"Content-Type": "application/json"})

    # 多参
    def login_extra_params(self):
        login_data = {"mobile": "13800000002", "password": "123456", "extra_params": "测试_多参"}
        return requests.post(self.login_url, json=login_data, headers={"Content-Type": "application/json"})

        # 少参

    def login_less_params(self):
        login_data = {"password": "123456"}
        return requests.post(self.login_url, json=login_data, headers={"Content-Type": "application/json"})

