#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08 11:10
# @Author  : zc
# @File    : app.py
from appium import webdriver

from pageObject.page.main_page import MainPage
from pageObject.utils.functions import Functions as Fun


class APP(object):

    appData = Fun().getYamlData('app')
    caps = appData['caps']
    server = appData['server']
    ip = server['ip']
    port = server['port']


    def startApp(self):

        self.driver = webdriver.Remote(f"http://{self.ip}:{self.port}/wd/hub", self.caps)
        self.driver.implicitly_wait(15)

        return self


    def stopApp(self):
        self.driver.quit()


    def goto_main(self):
        return MainPage(self.driver)