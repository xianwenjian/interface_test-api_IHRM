# 导包
import unittest
import time
from day06.apiTestIHRM.app import BASE_DIR
from day06.apiTestIHRM.script.test_ihrm_login import TestIHRMLogin
from day06.apiTestIHRM.script.test_irhm_emp_parameterized import TestIHRMEmp2
from day06.apiTestIHRM.tools.HTMLTestRunner import HTMLTestRunner
from day06.apiTestIHRM.script.test_ihrm_emp import TestIHRMEmp


# 实例化测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmp2))
# 初始化测试报告和名称
report_path = BASE_DIR + "/report/report{}.html".format(
    time.strftime("%Y%m%d-%H%M%S"))
with open(report_path, mode='wb') as f:
    # 初始化HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=1, description="IHRM人力资源管理系统接口测试报告",
                            title="测试登陆接口和员工管理模块")
    # 使用runner运行测试用例
    runner.run(suite)
