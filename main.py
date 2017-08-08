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



if __name__ == '__main__':
    try:
        action.driver_init()
        action.login()
        action.post_video()

    except Exception as e:
        print(e)
