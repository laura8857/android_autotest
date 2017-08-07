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
from Utility.remove_fb_remane_email import rm_email


if __name__ == '__main__':
    try:
        action.driver_init()
        action.login_skip()

    except Exception as e:
        print(e)
