# -*- coding: utf-8 -*-
# Time:2024/2/3 14:11
# Author:张柘
# File:config.py
# Desc:
import os

root = os.path.dirname(os.path.dirname(__file__))

report_path = root + '/report'
suite_case = root + '/testcase'
log_path = root + '/log/log.txt'
caps = {
    'platformName': 'Android',  # 设置操作系统
    'platformVersion': '7.1.2',  # 设置操作系统的版本号
    'deviceName': 'samsung',  # 设备的名称，通过命令adb shell getprop中查看设备的所有信息
    'appPackage': 'com.tencent.mobileqq',  # 加载的app的包名
    'appActivity': 'com.tencent.mobileqq.activity.SplashActivity',  # 启动app的activity
    'noReset': True,
    'resetKeyboard': True}