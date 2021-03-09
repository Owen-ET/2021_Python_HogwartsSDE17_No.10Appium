#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/03/05 10:14
# @Author  : zc
# @File    : testDemo.py


import pytest
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestDemo(object):


    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True,
            "waitForIdleTimeout": 1,
            "automationName": "UiAutomator2"        # Toast内容
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(25)
        # return self.driver


    def teardown(self):
        for i in range(10):
            sleep(1)
            print(i)
        self.driver.quit()


    def swipeUp(self):
        '''向上滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width*1/2,height*3/5,width*1/2,height*1/5)


    def findEle(self,loc):
        '''找到元素后点击元素退出循环，未找到元素继续滑动'''
        while(1<5):
            try:
                self.driver.find_element(By.XPATH, loc).click()
                return
            except:
                print("继续滑")
                self.swipeUp()


    def getExcept(self,loc,text):
        ''''''
        try:
            self.driver.find_element(By.XPATH,loc).click()
        except:
            print(text)


    @pytest.mark.skip(reason="不执行")
    def test1(self):
        '''
        前提条件: 已登录状态（ noReset=True）
        打卡用例：
        1、打开【企业微信】应用
        2、进入【工作台】
        3、点击【打卡】
        4、选择【外出打卡】tab
        5、点击【第N次打卡】
        6、验证【外出打卡成功】
        7、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(By.XPATH, "//*[@text='工作台']").click()
        # self.swipe()
        # self.driver.find_element(By.XPATH,"//*[@text='打卡']").click()
        self.findEle("//*[@text='打卡']")
        self.getExcept("//*[@text='立即使用']","没有找到按钮")
        self.driver.find_element(By.XPATH,"//*[@text='外出打卡']").click()
        self.getExcept("//*[@text='确定']", "没有定位失败弹框")
        self.driver.find_element(By.XPATH,"//*[contains(@text,'添加备注')]").click()
        self.driver.find_element(By.XPATH,"//*[@text='备注']").send_keys("Appium")
        self.driver.find_element(By.XPATH, "//*[@text='确定']").click()
        print(self.driver.page_source)
        self.getExcept("//*[@text='确定']", "没有定位失败弹框")
        po = self.driver.find_element(By.XPATH, "//*[contains(@text,'App')]").text
        print(po)
        assert po == "Appium1","不等于Appium1"


    def test2(self):
        '''完成企业添加联系人'''
        self.driver.find_element(By.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(By.ID,"com.tencent.wework:id/igf").click()
        self.driver.find_element(By.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(By.XPATH,"//*[@text='手动输入添加']").click()
        text = self.driver.find_elements(By.XPATH,"//*[@text='必填']")
        name = "zc3"
        text[0].send_keys(name)
        text[1].send_keys("13600000003")
        self.driver.find_element(By.XPATH,"//*[@text='保存后自动发送邀请通知']").click()
        self.driver.find_element(By.XPATH,"//*[@text='保存']").click()
        toast = self.driver.find_element(By.XPATH,"//*[contains(@text,'成功')]").text
        print(toast)
        self.driver.find_element(By.ID,"com.tencent.wework:id/ig0").click()
        self.driver.find_element(By.XPATH,"//*[@text='"+name+"']").click()
        self.driver.find_element(By.XPATH,"//*[@text='设置部门']").click()
        els = self.driver.find_elements(By.ID,"com.tencent.wework:id/h1g")
        print("数量为："+str(len(els))+"个")
        list = [3]
        for i in list:
            els[i].click()
        self.driver.find_element(By.XPATH,"//*[@text='确定("+str(len(list))+")']").click()
        self.driver.find_element(By.XPATH, "//*[@text='保存']").click()