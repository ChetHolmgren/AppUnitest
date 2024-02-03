# -*- coding: utf-8 -*-
# Time:2024/2/3 14:08
# Author:张柘
# File:apprunner.py
# Desc:
import unittest
from BeautifulReport import BeautifulReport
from config.config import suite_case, report_path

suite = unittest.defaultTestLoader.discover(start_dir=suite_case, pattern='test*.py')

# 将测试结果存入
result = BeautifulReport(suite)
result.report(description='手机QQ测试报告', filename='SIT测试报告', report_dir=report_path)
