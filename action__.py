# -*- coding: utf-8 -*-
# @Time    : 2017/2/7 下午2:15
# @Author  : Yuhsuan
# @File    : TestCases.py
# @Software: PyCharm Community Edition
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import deepblu_lib as lib
import desired_capabilities

deepblu = lib()

class action:
    def __init__(self):
        pass

    #init appium driver
    def driver_init(self):
        deepblu.log('[driver_init] start')
        desired_caps = desired_capabilities.get_desired_capabilities('appPackage','com.deepblu.android.deepblu.internal','android')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        deepblu.log('[driver_init] end')

    def login(self):
        deepblu.log('[login] start')
        try:
            el = self.wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin')
            self.driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/textLogin').click()
            self.sleep(3)
            self.driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(desired_capabilities.acc)
            self.sleep(3)
            self.back()
            self.sleep(3)
            self.driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextPassword").send_keys(desired_capabilities.password())
            self.back()
            self.sleep(3)
            self.driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUp").click()

        except Exception as e:
            deepblu.log(e)
        deepblu.log('[login] end')

    def back(self):
        self.driver.press_keycode(4)

    def enter(self):
        self.driver.press_keycode(66)

    def sleep(self,x):
        self.driver.implicitly_wait(x)

    def wait(self,type=None,el=None,time=None):
        if type == 'id':
            type = By.ID
        elif type == 'class':
            type = By.CLASS_NAME
        elif type == 'name':
            type = By.NAME
        elif type == 'tag':
            type = By.TAG_NAME
        elif type == 'xpath':
            type = By.XPATH
        else:
            type = By.ID

        if time == None:
            time = 5

        waite_element = WebDriverWait(self.driver,time).until(EC.presence_of_element_located((type,el)))

        return waite_element
