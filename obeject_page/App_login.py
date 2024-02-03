# -*- coding: utf-8 -*-
# Time:2024/2/3 14:34
# Author:张柘
# File:App_login.py
# Desc: QQ登录退出功能的封装
# from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.login_button = AppiumBy.ID, 'com.tencent.mobileqq:id/btn_login'
        self.username_page = AppiumBy.ACCESSIBILITY_ID, '请输入QQ号码或手机或邮箱'
        self.password_page = AppiumBy.ACCESSIBILITY_ID, '密码 安全'
        self.login = AppiumBy.ACCESSIBILITY_ID, '登 录'
        self.setting = AppiumBy.XPATH, '//android.widget.Button[@content-desc="设置"]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.TextView'
        self.account_switch = AppiumBy.ID, 'com.tencent.mobileqq:id/account_switch'
        self.login_out = AppiumBy.ACCESSIBILITY_ID, '退出当前帐号按钮'
        self.action_sheet_button = AppiumBy.ID, 'com.tencent.mobileqq:id/action_sheet_button'
        self.dialogRightBtn = AppiumBy.ID, 'com.tencent.mobileqq:id/dialogRightBtn'

    # 第一次登录需要点击登录按钮进入主页面
    def login_page_go(self):
        self.driver.find_element(*self.login_button).click()
        self.driver.implicitly_wait(10)

    # 输入用户名函数
    def input_username(self, username):
        self.driver.find_element(*self.username_page).clear()
        self.driver.find_element(*self.username_page).send_keys(username)

    # 输入密码函数
    def input_password(self, password):
        self.driver.find_element(*self.password_page).clear()
        self.driver.find_element(*self.password_page).send_keys(password)

    # 点击登录按钮
    def loginbtn(self):
        self.driver.find_element(*self.login).click()
        self.driver.implicitly_wait(10)

    # 向右滑动滑出个人设置页面
    # 退出登录
    def loginout(self):
        self.driver.swipe(11, 144, 873, 144, 1000)
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.setting).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.account_switch).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.login_out).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.action_sheet_button).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.dialogRightBtn).click()
