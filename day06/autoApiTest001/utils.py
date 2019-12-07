# 导包
import os

# 相对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def assert_common(self, respon, status_code, status,msg):
    self.assertEqual(status_code, respon.status_code)
    self.assertEqual(status, respon.json().get("status"))
    self.assertEqual(msg, respon.json().get("msg"))