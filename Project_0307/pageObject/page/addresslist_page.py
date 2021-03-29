#!/usr/bin/env python
# encoding: utf-8
'''
@author: owen_zc
@file: addresslist_page.py
@time: 2021-03-29 14:50
@desc:
'''
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from Project_0307.pageObject.page.addcontact_page import AddContactPage
from Project_0307.pageObject.page.base_page import Page
from Project_0307.pageObject.page.contactinfo_page import ContactInfo


class AddressListPage(Page):
    '''通讯录列表页'''

    addContact_loc = (MobileBy.XPATH, "//*[@text='添加成员']")
    searchButton_loc = (MobileBy.ID, "com.tencent.wework:id/igk")
    search_loc = (MobileBy.XPATH, "//*[@text='搜索']")
    searchContact_loc = (MobileBy.ID, "com.tencent.wework:id/ebs")




    def click_addContact(self):
        '''点击添加成员'''
        self.findEle(self.addContact_loc).click()
        return AddContactPage(self.driver)


    def searchContact(self,name):
        '''查询成员，进入个人信息页面'''
        self.click(self.searchButton_loc)
        self.sendKeys(self.search_loc,name)
        sleep(2)
        self.click(self.searchContact_loc)
        return ContactInfo(self.driver)