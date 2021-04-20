#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08 11:20
# @Author  : zc
# @File    : addUser_page.py
from appium.webdriver.common.mobileby import MobileBy

from Appium_20210407.pageObject.page.base_page import Page
from Appium_20210407.pageObject.utils.functions import Functions as Fun

class AddUserPage(Page):

    addUserData = Fun().getYamlData('addUser')

    name_loc = (MobileBy.XPATH, addUserData['name'])
    name = addUserData['name_value']
    tel_loc = (MobileBy.XPATH, addUserData['tel'])
    tel = addUserData['tel_value']
    send_loc = (MobileBy.XPATH, addUserData['send'])
    saveButton_loc = (MobileBy.XPATH, addUserData['saveButton'])



    def addUser_action(self):
        self.el_sendKeys(self.name_loc,self.name)
        self.el_sendKeys(self.tel_loc,self.tel)
        self.el_click(self.send_loc)
        self.el_click(self.saveButton_loc)
