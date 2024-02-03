# -*- coding: utf-8 -*-
# Time:2024/2/3 14:21
# Author:张柘
# File:log.py
# Desc:

import logging
from config.config import log_path

# 先创建日志器
logger = logging.getLogger()
# 定义日志器级别
logger.setLevel(logging.INFO)

# 定义处理器的格式参数
format = logging.Formatter("%(asctime)s %(filename)s [line:%(lineno)d]%(levelname)s %(message)s")

logfile = log_path
# 创建处理器
fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
fh.setFormatter(format)
fh.setLevel(logging.INFO)

# 将处理器添加到日志器中
logger.addHandler(fh)
