#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/07 13:40
# @Author  : zc
# @File    : test.py


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestDemo(object):

    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True


        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)

        self.driver.implicitly_wait(15)


    def teardown(self):
        self.driver.quit()


    # def reStart(self):
    #     self.driver.close_app()
    #     self.driver.launch_app()


    def swipeUp(self,loc):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        while(True):
            try:
                ele = self.driver.find_element(MobileBy.XPATH,loc)
                return ele
            except:
                print("继续上滑")
                self.driver.swipe(0.5 * width, 0.7 * height, 0.5 * width, 0.3 * height)




    def test1(self):
        print("启动成功")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.swipeUp("//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='姓名')]/../*[@text='必填']").send_keys("zc9")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys("zc8")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys("13600000008")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'自动发送')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
