# -*- coding: utf-8 -*-
# @Time    : 2017/2/7 下午2:10
# @Author  : Yuhsuan
# @File    : main.py
# @Software: PyCharm Community Edition

from appium import webdriver
import unittest
import os
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from action import *
import action
import deepblu_tool as common



if __name__ == '__main__':
    try:
        action.driver_init()
        common.remove_terms_conditions('laura@deepblu.com')
        action.login('laura@deepblu.com','12345678')
        action.agree_terms_conditions()

    except Exception as e:
        print(e)