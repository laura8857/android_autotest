# -*- coding: utf-8 -*-

import random
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import os
from pymongo import *
from selenium.webdriver.common.by import By

from deepblu_lib import log
import action
import time
import datetime


# 隨機字串
def randomword(size=10, chars=""):
    return ''.join(random.choice(chars) for x in range(size))


def read_json(file_path):
    empty = {}
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print('[Error][read_json] %s' % (e))
            return empty
    else:
        print('[Error][read_json] The json file path is not exist, %s' % (file_path))
        return empty


def getuserId(email):
    url = 'http://test.tritondive.co:3000/1/api/users?filter=%7B%22where%22%3A%7B%22email%22%3A%22' + email + \
          '%22%7D%7D&access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy'
    result = requests.get(url)
    # list=result.json()
    dict = {}
    dict = result.json()[0]
    user_id = dict['id']
    # print("userid:"+str(user_id))
    return user_id


# 註冊驗證號碼
def getusercode(email):
    print('email:' + email)
    url = "http://test.tritondive.co:3000/1/api/users?access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79Wwr" \
          "QtOlgRC9sQmKmzYAfqqy&filter={\"where\":{\"email\":\"" + email + "\"}}"
    result = requests.get(url)
    if result.status_code == 200:
        if len(result.json()) == 1:
            user_code = ""
            user_code = result.json()[0]['code']
            print("usercode:" + str(user_code))
            link = "https://test.tritondive.co/apis/user/v0/activeAccount?ownerId=" + result.json()[0][
                'id'] + "&code=" + user_code
            dict = {"code": user_code, "link": link}
            return dict
        else:
            return {}


# 驗證 link
def verify_by_link(url):
    json = {"accept-language": "en"}
    res = requests.get(url, headers=json)


# 使當前token過期
def token_expired(email):
    try:
        # connect to mongo
        client = MongoClient("52.197.14.177", 27017)
        client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
        db = client.deepblu

        if db.user.find_one({"email": email}):
            user = {}
            token = ""
            user = db.user.find_one({"email": email})
            id = user['_id']
            print(str(id))

            for doc in db.AccessToken.find({"userId": id}).sort("created", -1).limit(1):
                token = doc['_id']
                print(token)

            # call api
            url = "http://test.tritondive.co:8000/apis/user/v0/tokenExpire"
            data = {}
            data['accessToken'] = token
            headers = {"Accept-Language": "en"}
            result = requests.post(url, json=data, headers=headers)
            if result.status_code == 200:
                print(result.text)
                return True
        else:
            log("The mail " + email + " can't be found.", "w")
            # print("The mail "+email+" can't be found.")
            return False

        client.close()
    except Exception as e:
        log(e)
        return False


# screenshot
def screenshot(file_name):
    directory = '%s/' % os.getcwd() + 'AndroidAppTest/' + time.strftime("%Y%m%d") + '/'
    if not os.path.exists(directory):  # 先確認資料夾是否存在
        os.makedirs(directory)
    # print(directory)
    screenshot = action.driver.save_screenshot(directory + time.strftime('%H%M%S') + '_' + file_name + ".png")


# 檢查是否抓元件
def wait(type=None, el=None, time=None):
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
        time = 10

    try:
        waite_element = WebDriverWait(action.driver, time).until(EC.presence_of_element_located((type, el)))
        return True
    except Exception as e:
        screenshot("Error")
        log("[Error] The element: %s can't be found. %s" % (el, e), 'w')
        return False


def kill_app():
    log('[kill app] start')
    action.driver.close_app()
    # os.popen("adb shell am force-stop com.deepblu.android.deepblu.internal")
    log('[kill app] end')


def open_app():
    log('[open app] start')
    os.popen('adb shell am start -n com.deepblu.android.deepblu.internal/'
             'com.deepblu.android.deepblu.screen.loading.LoadingActivity')
    log('[open app] end')


# clear cache and data
def clear_app():
    log('[clear app] start')
    os.popen("adb shell pm clear com.deepblu.android.deepblu.internal")
    log('[clear app] end')


def browser():
    os.popen("adb shell am start -a android.intent.action.VIEW -d 'http://stackoverflow.com/?uid=isme\&debug=true'")


def home_screen():
    back()
    home()
    home()
    back()


def home():
    action.driver.press_keycode(3)


def back():
    action.driver.press_keycode(4)


def enter():
    action.driver.press_keycode(66)


def sleep(x):
    time.sleep(x)


def size():
    dict = {}
    dict = action.driver.get_window_size()
    list = []
    list.append(dict['height'])
    list.append(dict['width'])
    # print("H: "+str(list[0]))
    # print("W: "+str(list[1]))

    return list


# 0.8滑到0.1 大滑動
def swipeup():
    try:
        # 絕對位置 起始點 結束點
        list = size()
        startx = list[1] * 0.2
        starty = list[0] * 0.8
        endy = list[0] / 10
        # print("x1:" + str(startx) + " y1:" + str(starty) + " x2:" + str(startx) + " y2:" + str(endy))
        action.driver.swipe(startx, starty, startx, endy, 500)
        # driver.swipe(640,2320,640,400,100)
    except Exception as e:
        log(e, 'w')


# 14/16滑到12/16  小滑動
def swipeup2():
    try:
        # 絕對位置 起始點 結束點
        list = size()
        startx = list[1] * 0.2
        starty = list[0] * 0.875
        endy = list[0] * 0.75
        # print("x1:" + str(startx) + " y1:" + str(starty) + " x2:" + str(startx) + " y2:" + str(endy))
        action.driver.swipe(startx, starty, startx, endy, 500)
        # driver.swipe(640,2320,640,400,100)
    except Exception as e:
        log(e, 'w')


def isElementPresent(by):
    try:
        action.driver.find_element_by_xpath(by)

        return 1

    except Exception as e:
        log(e, 'w')
        print("failed")
        return 0


def browser():
    os.popen("adb shell am start -a android.intent.action.VIEW -d 'http://stackoverflow.com/?uid=isme\&debug=true'")

# rename the email from AAA@AAA.com to AAAYYYYMMDDHHMMSS@AAA.com
def rm_email(email):
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    tmp = email.split("@")
    new_mail = tmp[0]+now+'@'+tmp[1]

    #update to mongodb
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email":email}):
        db.user.update_one({"email": email}, {"$set": {"email": new_mail}})
        if db.user.find_one({"email":email}):
            print("Please check DB, the email can't be changed")
        else:
            print("The email already modify to "+new_mail)
    else:
        print("The mail "+email+" can't be found.")
    client.close()

# remove Facebook connection
def rm_fb(email):
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.socialId.find_one({"email":email}):
        db.socialId.delete_one({"email":email})
        if db.socialId.find_one({"email":email}):
            print("Please check DB, the fb can't be changed")
        else:
            print("The facebook account is removed.")
    else:
        print("The facebook account "+email+" can't be found.")