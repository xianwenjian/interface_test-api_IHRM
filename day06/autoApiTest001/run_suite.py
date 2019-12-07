# 导包
import os
import time
import unittest
from day06.autoApiTest001.script.TestLogin import TestLogin
from day06.autoApiTest001.tools.HTMLTestRunner import HTMLTestRunner
from day06.autoApiTest001.utils import BASE_DIR

# 初始化测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
# 初始化测试报告和名称
report_path = BASE_DIR + "/report/report{}.html".format(
    time.strftime("%Y%m%d-%H%M%S"))
with open(report_path, mode='wb') as f:
    # 初始化HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=1, description="tpshop的测试报告", title="TPshop")
    # 使用runner运行测试用例
    runner.run(suite)
