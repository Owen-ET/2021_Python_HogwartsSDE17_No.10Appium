#!/usr/bin/env python
# encoding: utf-8
'''
@author: owen_zc
@file: base_page.py
@time: 2021-03-29 15:35
@desc:
'''
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class Page(object):
    '''基类'''

    logging.basicConfig(level=logging.INFO)

    def __init__(self,driver:WebDriver = None):
        self.driver = driver


    def find_element(self,*loc):
        logging.info("find")
        logging.info(loc)
        return self.driver.find_element(*loc)


    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)


    def click(self,loc):
        self.find_element(*loc).click()


    def sendKeys(self,loc,text):
        self.find_element(*loc).send_keys(text)


    def getText(self,loc):
        return self.find_element(*loc).text


    def swipeUp(self):
        '''向上滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width*1/2,height*3/5,width*1/2,height*1/5,500)


    def findEle(self,loc,num=0):
        '''找到元素后点击元素退出循环，未找到元素继续滑动'''
        while(num<3):
            try:
                element = self.find_element(*loc)
                return element
            except:
                print("继续滑")
                self.swipeUp()
                num = num + 1
                if num == 3:
                    raise NoSuchElementException(f"找了{num}次，元素没找到！")