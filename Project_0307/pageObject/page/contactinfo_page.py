#!/usr/bin/env python
# encoding: utf-8
'''
@author: owen_zc
@file: contactinfo_page.py
@time: 2021-03-29 19:24
@desc:
'''
from Project_0307.pageObject.page.addcontact_page import AddContactPage
from Project_0307.pageObject.page.base_page import Page
from appium.webdriver.common.mobileby import MobileBy


class ContactInfo(Page):
    '''个人信息页'''

    contactInfo_loc = (MobileBy.ID, "com.tencent.wework:id/iga")
    editContact_loc = (MobileBy.XPATH, "//*[@text='编辑成员']")
    delContact_loc = (MobileBy.XPATH, "//*[contains(@text,'删除成员')]")
    sureButton_loc = (MobileBy.XPATH, "//*[contains(@text,'确定')]")

    def delContact_action(self):
        '''删除成员操作'''
        self.click(self.contactInfo_loc)
        self.click(self.editContact_loc)
        self.click(self.delContact_loc)
        self.click(self.sureButton_loc)
        self.click(AddContactPage(self.driver).backButton_loc)