#!/usr/bin/env python
# encoding: utf-8
'''
@author: owen_zc
@file: test_contact.py
@time: 2021-03-29 15:45
@desc:
'''
from Project_0307.pageObject.page.app import App


class TestContact:

    def setup(self):
        self.app = App().startApp()
        self.main = self.app.goto_main()


    def teardown(self):
        pass


    def test_addContact(self):
        name = "zc7"
        tel = "13600000007"
        addContactPage = self.main.goto_addressList().click_addContact()
        addContactPage.addContact_action(name,tel)
        toast = addContactPage.get_toast()
        print(toast)


    def test_delContact(self):
        name = "zc5"
        self.main.goto_addressList().searchContact(name).delContact_action()