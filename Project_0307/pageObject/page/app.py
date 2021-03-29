#!/usr/bin/env python
# encoding: utf-8
'''
@author: owen_zc
@file: app.py
@time: 2021-03-29 14:32
@desc:
'''
import yaml
from appium import webdriver

from Project_0307.pageObject.page.base_page import Page
from Project_0307.pageObject.page.main_page import MainPage


class App(Page):

    with open("../data/app.yaml") as file:
        data = yaml.load(file)

    caps = data['desirecaps']
    ip = data['server']['ip']
    port = data['server']['port']


    def startApp(self):
        # 启动

        if self.driver == None:
            # 如果初始值为None
            # caps = {
            #     "platformName": "android",
            #     "deviceName": "emulator-5554",
            #     "appPackage": "com.tencent.wework",
            #     "appActivity": ".launch.LaunchSplashActivity",
            #     "noReset": True,
            #     "waitForIdleTimeout": 1,
            #     "skipServerInstallation": True,  # 跳过UIautomator2 server安装
            #     "skipDeviceInitialization": True,  # 跳过设备的初始化
            #     # "dontStopAppOnReset": True,  # 测试之前不停止app运行
            #     "automationName": "UiAutomator2"  # Toast内容
            # }

            self.driver = webdriver.Remote(f"http://{self.ip}:{self.port}/wd/hub", self.caps)
            self.driver.implicitly_wait(15)
        else:
            # 否则的话，启动app
            self.driver.launch_app()
        return self



    def restartApp(self):
        # 重启
        self.driver.close_app()
        self.driver.launch_app()


    def stopApp(self):
        # 停止
        self.driver.quit()


    def goto_main(self):
        '''进入主页'''
        return MainPage(self.driver)