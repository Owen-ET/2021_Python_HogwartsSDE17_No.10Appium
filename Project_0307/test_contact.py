#!/usr/bin/env python
# encoding: utf-8
'''
@author: owen_zc
@file: test_contact.py
@time: 2021-03-09 20:45
@desc:
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class TestContact(object):

    def swipeUp(self):
        '''向上滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width*1/2,height*3/5,width*1/2,height*1/5,500)


    def findEle(self,text,num=0):
        '''找到元素后点击元素退出循环，未找到元素继续滑动'''
        while(num<3):
            try:
                element = self.driver.find_element(By.XPATH, f"//*[@text='{text}']")
                return element
            except:
                print("继续滑")
                self.swipeUp()
                num = num + 1
                if num == 3:
                    raise NoSuchElementException(f"找了{num}次，元素没找到！")


    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True,
            "waitForIdleTimeout": 1,
            "skipServerInstallation": True,     # 跳过UIautomator2 server安装
            "skipDeviceInitialization": True,   # 跳过设备的初始化
            "dontStopAppOnReset": True,       # 测试之前不停止app运行
            "automationName": "UiAutomator2"        # Toast内容
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)


    def teardown(self):
        pass


    def test(self):
        '''完成企业添加联系人'''
        name = "zc4"
        tel = "13600000004"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.findEle("添加成员").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(tel)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        toast = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'成功')]").text
        print(toast)
        assert toast == "添加成功","toast不对"
        # self.driver.page_source
        # self.driver.find_element(By.ID, "com.tencent.wework:id/ig0").click()
        # self.driver.find_element(By.XPATH, "//*[@text='" + name + "']").click()
        # self.driver.find_element(By.XPATH, "//*[@text='设置部门']").click()
        # els = self.driver.find_elements(By.ID, "com.tencent.wework:id/h1g")
        # print("数量为：" + str(len(els)) + "个")
        # list = [3]
        # for i in list:
        #     els[i].click()
        # self.driver.find_element(By.XPATH, "//*[@text='确定(" + str(len(list)) + ")']").click()
        # self.driver.find_element(By.XPATH, "//*[@text='保存']").click()