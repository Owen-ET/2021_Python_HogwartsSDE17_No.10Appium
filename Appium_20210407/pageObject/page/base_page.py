#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08 13:19
# @Author  : zc
# @File    : base_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from appium import webdriver


class Page:

    def __init__(self,driver:WebDriver):
        self.driver = driver


    def find_element(self,loc):
        return self.driver.find_element(*loc)


    def find_elements(self,loc):
        return self.driver.find_elements(*loc)


    def el_sendKeys(self,loc,text):
        self.find_element(loc).send_keys(text)


    def el_click(self,loc):
        self.find_element(loc).click()


    def swipeUp(self,loc):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        while(True):
            try:
                # ele = self.driver.find_element(MobileBy.XPATH,loc)
                ele = self.find_element(loc)
                return ele
            except:
                print("继续上滑")
                self.driver.swipe(0.5 * width, 0.7 * height, 0.5 * width, 0.3 * height)