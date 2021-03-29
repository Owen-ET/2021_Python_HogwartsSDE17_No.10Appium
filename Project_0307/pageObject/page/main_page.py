#!/usr/bin/env python
# encoding: utf-8
'''
@author: owen_zc
@file: main_page.py
@time: 2021-03-29 14:43
@desc:
'''

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from Project_0307.pageObject.page.addresslist_page import AddressListPage
from Project_0307.pageObject.page.base_page import Page


class MainPage(Page):
    '''主页'''
    address_loc = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addressList(self):
        '''点击通讯录，进入通讯录列表'''
        self.click(self.address_loc)
        return AddressListPage(self.driver)