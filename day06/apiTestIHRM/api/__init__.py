from day06.apiTestIHRM.app import init_logger
import logging

# 调用自己封装的日志初始化
init_logger()

logging.debug("日志等级低于设置的info, 不可以打印出来")
logging.info("日志等级相同, 可以 打印出来")
logging.warning("日志等级高于设置的info, 可以打印出来")


