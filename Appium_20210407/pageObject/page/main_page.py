#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08 11:12
# @Author  : zc
# @File    : main_page.py
from appium.webdriver.common.mobileby import MobileBy

from pageObject.page.addressList_page import AddressListPage
from pageObject.page.base_page import Page
from pageObject.utils.functions import Functions as Fun


class MainPage(Page):

    mainData = Fun().getYamlData('main')
    address_loc = (MobileBy.XPATH, mainData['address'])

    def goto_addressList(self):

        self.el_click(self.address_loc)
        return AddressListPage(self.driver)