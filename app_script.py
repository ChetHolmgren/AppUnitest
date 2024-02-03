# -*- coding: utf-8 -*-
# Time:2024/1/30 16:09
# Author:张柘
# File:app_script.py
# Desc:
from time import sleep
from config.config import caps
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=caps)
# 首次进入需要点击登录按钮，后面进去就直接是账号面膜页面
# driver.implicitly_wait(10)
# driver.find_element(By.ID, 'com.tencent.mobileqq:id/btn_login').click()
# driver.implicitly_wait(10)
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, '请输入QQ号码或手机或邮箱').clear()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "密码 安全").clear()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, '请输入QQ号码或手机或邮箱').send_keys('2224540751')
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "密码 安全").send_keys('216971@zhangzhe')
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, '登 录').click()


sleep(5)
# 退出登录
# 向右滑动进入个人设置页面
driver.swipe(11, 144, 873, 144, 1000)
driver.implicitly_wait(10)
driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="设置"]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.TextView').click()
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ID, 'com.tencent.mobileqq:id/account_switch').click()
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, '退出当前帐号按钮').click()
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ID, 'com.tencent.mobileqq:id/action_sheet_button').click()
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ID, 'com.tencent.mobileqq:id/dialogRightBtn').click()

