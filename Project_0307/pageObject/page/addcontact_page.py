#!/usr/bin/env python
# encoding: utf-8
'''
@author: owen_zc
@file: addcontact_page.py
@time: 2021-03-29 15:05
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy

from Project_0307.pageObject.page.base_page import Page


class AddContactPage(Page):
    '''添加成员页'''

    inputAdd_loc = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    name_loc = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']")
    tel_loc = (MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']")
    sendMessage_loc = (MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']")
    saveButton_loc = (MobileBy.XPATH, "//*[@text='保存']")
    toast_loc = (MobileBy.XPATH, "//*[contains(@text,'成功')]")
    backButton_loc = (MobileBy.ID, "com.tencent.wework:id/ig0")

    def addContact_action(self,name,tel):
        '''添加成员'''
        self.click(self.inputAdd_loc)
        self.sendKeys(self.name_loc,name)
        self.sendKeys(self.tel_loc,tel)
        self.click(self.sendMessage_loc)
        self.click(self.saveButton_loc)
        self.click(self.backButton_loc)


    def get_toast(self):
        '''获取toast'''
        return self.getText(self.toast_loc)