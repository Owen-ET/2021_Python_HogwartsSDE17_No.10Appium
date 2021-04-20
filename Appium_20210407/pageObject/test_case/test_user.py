#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08 11:27
# @Author  : zc
# @File    : test_user.py
from Appium_20210407.pageObject.page.app import APP


class TestUser:

    def setup(self):
        self.app = APP().startApp()
        self.main = self.app.goto_main()


    def teardown(self):
        self.app.stopApp()


    def test_addUser(self):
        self.main.goto_addressList().goto_addUser().addUser_action()