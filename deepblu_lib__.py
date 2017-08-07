# -*- coding: utf-8 -*-
# @Time    : 2017/2/7 下午2:19
# @Author  : Yuhsuan
# @File    : deepblu_lib.py
# @Software: PyCharm Community Edition

import datetime

class deepblu_lib():
    def __init__(self):
        pass

    def log(self, output):
        now = datetime.datetime.now().strftime('%Y/%m/%d_%H:%M:%S')
        print(now, output)