# -*- coding: utf-8 -*-
# Time:2024/2/3 19:29
# Author:张柘
# File:test1_login_out.py
# Desc:手机qq登录
import unittest
from time import sleep

from obeject_page.App_login import Login
from config.config import caps
from appium import webdriver
from log.log import logger

class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('开始测试')
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=caps)
        cls.login_suite = Login(driver)

    @classmethod
    def tearDownClass(cls):
        print("退出测试")

    def test_1(self):
        """
        进行一次完整的登录退出操作
        :return:
        """
        self.login_suite.loginbtn()
        sleep(4)
        self.login_suite.loginout()
        logger.info('手机qq登录退出流程成功')
