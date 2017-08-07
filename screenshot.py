# -*- coding: utf-8 -*-

import os

def screenshot(driver,file_name):
    directory = '%s/' % os.getcwd()
    screenshot = driver.save_screenshot(directory + '_' + file_name)
