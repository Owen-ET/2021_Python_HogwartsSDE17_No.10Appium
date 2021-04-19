#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/04/08 14:55
# @Author  : zc
# @File    : functions.py
import os

import yaml


class Functions:

    def pathUp(self):
        path = os.path.dirname(os.path.dirname(__file__))
        return path


    def getYaml(self,path):
        with open(path,encoding='utf-8') as file:
            data = yaml.load(file)
            return data


    def getCommonYaml(self):
        commonPath = self.pathUp()+ "/data/common.yaml"
        return self.getYaml(commonPath)



    def getYamlData(self,data):
        yamlPath = self.pathUp() + self.getCommonYaml()[data]
        return self.getYaml(yamlPath)

