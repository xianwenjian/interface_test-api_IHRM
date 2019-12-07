# 1.导包
import logging
from logging import handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {}
EMPID = ""


def init_logger():
    # 2.初始化日志器 并设置日志等级
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # logging.INFO  : 20
    # 3.初始化处理器
    # 初始化控制台处理器
    sh = logging.StreamHandler()
    # 初始化文件处理器
    log_path = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path, when="s", interval=1, backupCount=7,
                                                   encoding="UTF-8")

    # 4.初始化格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # 5.将格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 6.将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
