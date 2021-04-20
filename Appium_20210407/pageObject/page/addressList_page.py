#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08 11:16
# @Author  : zc
# @File    : addressList_page.py
from appium.webdriver.common.mobileby import MobileBy

from Appium_20210407.pageObject.page.addUser_page import AddUserPage
from Appium_20210407.pageObject.page.base_page import Page
from Appium_20210407.pageObject.utils.functions import Functions as Fun

class AddressListPage(Page):

    addressListData = Fun().getYamlData('addressList')

    inputAdd_loc = (MobileBy.XPATH, addressListData['inputAdd'])
    addUser_loc = (MobileBy.XPATH, addressListData['addUser'])

    def goto_addUser(self):
        self.swipeUp(self.addUser_loc).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.el_click(self.inputAdd_loc)
        return AddUserPage(self.driver)