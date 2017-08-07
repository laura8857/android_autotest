# -*- coding: utf-8 -*-
# @Time    : 2017/2/7 下午2:15
# @Author  : Yuhsuan
# @File    : TestCases.py
# @Software: PyCharm Community Edition
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import deepblu_lib as deepblu
import desired_capabilities
import os
import time
import GlobalString
import random
import deepblu_tool as Dtool


# desired_caps = desired_capabilities.get_desired_capabilities('appPackage', 'com.deepblu.android.deepblu.internal',
#                                                              'android')
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# init appium driver


def driver_init():
    global driver
    try:
        deepblu.log('[driver_init] start')
        desired_caps = desired_capabilities.get_desired_capabilities('appPackage', 'com.deepblu.android.deepblu.internal',
                                                                     'android')
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        deepblu.log('[driver_init] end')
    except Exception as e:
        deepblu.log(e, 'w')


def driver_close():
    try:
        deepblu.log('[driver_close] start')
        driver.close_app()
        driver.close
        deepblu.log('[driver_close] end')
    except Exception as e:
        deepblu.log(e, 'w')


def login(email=None, password=None):
    deepblu.log('[login] start')
    try:
        if email == None:
            email = desired_capabilities.account()
        if password == None:
            password = desired_capabilities.password()
        el = wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin')
        if el:
            driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/textLogin').click()
            sleep(3)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(email)
            sleep(3)
            back()
            sleep(3)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextPassword").send_keys(password)
            back()
            sleep(3)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUp").click()
        else:
            deepblu.log("Please check the screen shoot")
    except Exception as e:
        deepblu.log(e, 'w')
    screenshot("login")
    deepblu.log('[login] end')


def login_skip():
    deepblu.log('[login_skip] start')
    try:
        el = wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin')
        if el:
            driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/textLogin').click()
            sleep(2)
            back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSkip").click()

            checkel = wait(type='xpath', el=GlobalString.create_post)
            if checkel:
                screenshot('loginSkip')
            else:
                deepblu.log("Please see screenshot.")
        else:
            deepblu.log("Please check the screen shoot")
    except Exception as e:
        deepblu.log(e, 'w')

    deepblu.log('[login_skip] end')

def logout():
    deepblu.log('[logout] start')

    try:
        driver.find_element_by_xpath(GlobalString.tab + "[5]").click()
        sleep(3)
        swipeup()
        # logout xpath :note5 12 zenfone 10
        driver.find_element_by_xpath(GlobalString.list + "[12]").click()
        # driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[12]").click()
        sleep(3)
        el = wait(type='id', el="android:id/button1")
        if el:
            driver.find_element_by_id("android:id/button1").click()
        else:
            deepblu.log("Please check the screen shoot")
        sleep(3)
        # verify successful or not
        checkel = wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin')
        if checkel:
            screenshot("Logout")
        else:
            deepblu.log('Please check the screenshot')
    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log('[logout] end')


# about page
def about():
    deepblu.log('[about] start')
    try:
        # menu page
        driver.find_element_by_xpath(GlobalString.tab + "[5]").click()
        sleep(5)

        # about page
        driver.find_element_by_xpath(GlobalString.list + "[11]").click()
        sleep(3)

        screenshot("About")
    except Exception as e:
        deepblu.log(e, 'w')

    try:
        # app version
        deepblu.log('[appVersion] start')
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/about_version_secondary_text").click()
        time.sleep(3)
        screenshot("appVersion")
        back()
        deepblu.log('[appVersion] end')
    except Exception as e:
        deepblu.log(e, 'w')

    try:
        # Term&Conditoins
        deepblu.log('[Term&Condtions] start')
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/about_term_primary_text").click()
        sleep(3)
        screenshot("Term&CondtionsStart")

        i = 28
        while i > 0:
            swipeup()
            i -= 1
        screenshot("Term&ConditionsEnd")
        sleep(2)
        back()
        deepblu.log('[Term&Conditions] end')

    except Exception as e:
        deepblu.log(e ,'w')

    try:
        # Guidelines
        deepblu.log('[Guidelines] start')
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/about_guideline_primary_text").click()
        sleep(3)
        screenshot("Guidelines")
        sleep(2)
        back()
        deepblu.log('[Guidelines] end')

    except Exception as e:
        deepblu.log(e, 'w')

    # 返回menu page
    back()
    deepblu.log('[about] end')


# menu page的help
def help():
    deepblu.log("[Help] start")
    try:
        # menu page
        driver.find_element_by_xpath(GlobalString.tab + "[5]").click()
        sleep(5)
        # help page
        driver.find_element_by_xpath(GlobalString.list + "[9]").click()
        sleep(3)

        path = " //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]" \
               "/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/" \
               "android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android." \
               "webkit.WebView[1]/android.view.View[2]"
        el = wait(type='xpath', el=path)
        if el:
            deepblu.log("網頁正常出現")
        else:
            deepblu.log("\n 網頁沒有load出來")
        screenshot("Help")
    except Exception as e:
        deepblu.log(e, 'w')

    # 返回menu page
    back()
    deepblu.log("[Help] end")


# menu page的app feedback
def appfeedback():
    deepblu.log("[App feedback] start")
    try:
        # menu page
        driver.find_element_by_xpath(GlobalString.tab + "[5]").click()
        sleep(5)
        # appfeedback page
        driver.find_element_by_xpath(GlobalString.list + "[10]").click()
        sleep(3)

        optionel = wait(type='id', el="com.deepblu.android.deepblu.internal:id/textViewSpinner")
        if optionel:
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/textViewSpinner").click()
            sleep(2)
            option = driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.TextView[" + str(
                    random.randint(1, 4)) + "]")
            optionstring = option.text
            option.click()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/subject_edit").send_keys(
                "[Test Subject] " + optionstring)
            back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/content_edit").send_keys(
                optionstring + "\n" + time.strftime("%Y%m%d%H%M%S") + "\n" + Dtool.randomword(100, GlobalString.bio))
            back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/main_feedback_send_report").click()
            # sumit successful
            submit = wait(type='id', el="com.deepblu.android.deepblu.internal:id/feedback_submitted_button")
            if submit:
                screenshot("appfeedback")
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/feedback_submitted_button").click()
            else:
                deepblu.log("Report failed.Please check screenshot.")
                # 返回menu page
                back()
        else:
            deepblu.log("Please check the screen shoot")

    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[App feedback] end")


def events():
    deepblu.log("[Events] start")
    try:
        # menu page
        driver.find_element_by_xpath(GlobalString.tab + "[5]").click()
        sleep(5)
        # events page
        driver.find_element_by_xpath(GlobalString.list + "[8]").click()
        sleep(3)

        path = "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]" \
               "/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/andr" \
               "oid.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.webkit." \
               "WebView[1]/android.view.View[1]/android.widget.Image[1]"
        el = wait(type='xpath', el=path)
        if el:
            deepblu.log("網頁正常出現")
        else:
            deepblu.log("\n 網頁沒有load出來")
        screenshot("Events")
    except Exception as e:
        deepblu.log(e, 'w')
    # 返回menu page
    back()
    deepblu.log("[Events] end")


def userProfile():
    try:
        deepblu.log("[User Profile] start")

        # 一般方法進入user profile page
        # # menu page
        # driver.find_element_by_xpath(GlobalString.tab + "[5]").click()
        # sleep(5)
        # # user profile page
        # driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/item_menu_user_profile_icon").click()
        # sleep(3)

        # 用deepblink 進入user profile page
        os.popen("adb shell am start -W -a android.intent.action.VIEW -d 'deepblu://deepblu.link/Menu/Profile'")
        sleep(3)
        screenshot("UserProfile")

        # 返回menu page
        # back()
        deepblu.log("[User Profile] end")
    except Exception as e:
        deepblu.log(e, 'w')


def editUserProfile():
    deepblu.log("[Edit User Profile] start")
    # 一般方法進入Edit User Profile page
    # menu page
    # driver.find_element_by_xpath(GlobalString.tab + "[5]").click()
    # sleep(5)
    # # user profile page
    # driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/item_menu_user_profile_icon").click()
    # sleep(3)
    # driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/left_button").click()
    # sleep(3)

    # deeplink
    os.popen("adb shell am start -W -a android.intent.action.VIEW -d 'deepblu://deepblu.link/Menu/Profile/EditProfile'")
    sleep(3)

    screenshot("EditUserProfile")

    # 編輯user profile
    deepblu.log("[Avatar&Background] start")
    driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_avatar").click()
    sleep(2)

    # 要求權限
    elask = wait(type="id", el='com.android.packageinstaller:id/permission_allow_button')
    if elask:
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

    # # avatar
    # try:
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_avatar").click()
    #     sleep(3)
    #     # 第三個資料夾第二張照片
    #     changePhoto("3", "2")
    # except Exception as e:
    #     deepblu.log(e)
    # #background
    # try:
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_background").click()
    #     sleep(3)
    #     # 第二個資料夾第二張照片
    #     changePhoto("2", "2")
    # except Exception as e:
    #     deepblu.log(e)
    #
    # deepblu.log("[Avatar&Background] end")

    deepblu.log("[name] start")
    try:
        # name
        userel = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_text_user_name")
        Username = userel.text + "_" + time.strftime("%m%d")
        userel.clear()
        userel.send_keys(Username)
        back()
        swipeup2()
        firstel = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_text_first_name")
        Firstname = firstel.text + "_" + time.strftime("%m%d")
        firstel.clear()
        firstel.send_keys(Firstname)
        back()
        lastel = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edittext_last_name")
        Lastname = lastel.text + "_" + time.strftime("%m%d")
        lastel.clear()
        lastel.send_keys(Lastname)
        back()
    except Exception as e:
        deepblu.log(e)

    deepblu.log("[name] end")

    # 性別   男->女 女->其他 其他->男
    deepblu.log("[gender] start")
    try:
        gender1 = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/spinnerItem").text
        gender = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/spinnerItem").text
        print("gender:" + gender)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/spinnerItem").click()
        option1 = driver.find_element_by_xpath(
            "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout["
            "1]/android.widget.TextView[1]").text
        option2 = driver.find_element_by_xpath(
            "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]"
            "/android.widget.TextView[1]").text

        if gender == option1:
            driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout"
                "[2]/android.widget.TextView[1]").click()
        elif gender == option2:
            driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout"
                "[3]/android.widget.TextView[1]").click()
        else:
            driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout"
                "[1]/android.widget.TextView[1]").click()
    except Exception as e:
        deepblu.log(e)
    deepblu.log("[gender] end")
    sleep(2)

    swipeup2()
    # country
    deepblu.log("[country] start")
    try:
        elc = driver.find_element_by_id(
            "com.deepblu.android.deepblu.internal:id/user_profile_edit_region_auto_complete_text_view")
        country = elc.text
        elc.click()
        if country == "Taiwan":
            elc.send_keys("japan")
        else:
            elc.send_keys("taiwan")
        sleep(2)

        location = {}
        location = driver.find_element_by_id(
            "com.deepblu.android.deepblu.internal:id/user_profile_edit_region_auto_complete_text_view").location
        x = location['x']
        y = location['y']
        print("location x:" + str(x) + " y:" + str(y))

        list = size()
        x1 = list[1] * 0.5
        y1 = y + 260
        print("location x1:" + str(x1) + " y1:" + str(y1))
        TouchAction(driver).press(x=x1, y=y1).release().perform()
        sleep(2)
    except Exception as e:
        deepblu.log(e)

    deepblu.log("[country] end")

    sleep(2)
    swipeup2()
    # short bio
    deepblu.log("[short bio] start")
    try:
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_text_short_bio").clear()
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_text_short_bio").send_keys(
            Dtool.randomword(100, GlobalString.bio))
        sleep(3)
        back()
        screenshot("EditUserProfileAfter")
    except Exception as e:
        deepblu.log(e)
    deepblu.log("[Edit User Profile] end")

    # non deepblu dive
    deepblu.log("[Non-deepblu dive] start")
    swipeup2()
    swipeup2()
    try:
        diveel = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_text_total_dive")
        divenumber = int(diveel.text)
        if divenumber < 99990:
            divenumber = divenumber + 10
        else:
            divenumber = 0
        diveel.clear()
        diveel.send_keys(divenumber)
        back()
    except Exception as e:
        deepblu.log(e)
    deepblu.log("[Non-deepblu dive] end")

    # save
    try:
        swipeup()
        sleep(2)
        # swipeup()
        # sleep(2)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_done_button").click()
    except Exception as e:
        deepblu.log(e)

    deepblu.log("[Edit User Profile] end")


    # #將照片換回來
    # try:
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/left_button").click()
    #     sleep(3)
    #     #avatar
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_avatar").click()
    #     sleep(2)
    #     # 第三個資料夾第一張照片
    #     changePhoto("3", "1")
    #     sleep(2)
    #     #background
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_background").click()
    #     sleep(3)
    #     # 第二個資料夾第三張照片
    #     changePhoto("2", "3")
    #     sleep(2)
    #     swipeup()
    #     sleep(2)
    #     swipeup()
    #     sleep(2)
    #     # save
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_done_button").click()
    # except Exception as e:
    #     deepblu.log(e)


def post_text():
    deepblu.log("[Post Text] start")
    try:
        postIcon = GlobalString.create_post
        el = wait(type='xpath', el=postIcon)
        if el:
            driver.find_element_by_xpath(postIcon).click()
            sleep(2)
            el2 = wait(type='id', el="com.deepblu.android.deepblu.internal:id/text_post_group")
            if el2:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/text_post_group").click()
            else:
                deepblu.log("Please check the screen shoot")
            sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").click()
            content = ""
            content = "[AutoTest]\n" + Dtool.randomword(10, GlobalString.bio) + "\n" + time.strftime("%Y%m%d%H%M%S")
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").send_keys(content)
            # sleep(1)
            # hashtag()
            sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_post").click()
            sleep(2)
            el3 = wait(type='id', el="android:id/button1")
            if el3:
                driver.find_element_by_id("android:id/button1").click()
            else:
                deepblu.log("Please check the screen shoot")
            sleep(2)
            checkel = wait(type='xpath', el=postIcon)
            if checkel:
                screenshot("PostText")
            else:
                deepblu.log('Please check the screen shoot')
        else:
            deepblu.log("Please check the screen shoot")
    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Post Text] end")


def post_link():
    deepblu.log("[Post Link] start")
    try:
        postIcon = GlobalString.create_post
        el = wait(type='xpath', el=postIcon)
        if el:
            driver.find_element_by_xpath(postIcon).click()
            sleep(2)
            el2 = wait(type='id', el="com.deepblu.android.deepblu.internal:id/link_post_group")
            if el2:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/link_post_group").click()
            else:
                deepblu.log("Please check the screen shoot")
            sleep(2)
            link = "https://www.deepblu.com"
            # link = random.choice(GlobalString.link)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_body").send_keys(link)
            sleep(2)
            driver.find_element_by_id("android:id/button1").click()
            sleep(2)
            content = ""
            content = "[AutoTest]\n" + Dtool.randomword(10, GlobalString.bio) + "\n" + time.strftime(
                "%Y%m%d%H%M%S") + "\n" + link
            # 檢查有沒有抓到內容元件 才能輸入文字
            elcontent = wait(type='id', el="com.deepblu.android.deepblu.internal:id/post_caption")
            if elcontent:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").send_keys(content)
                # sleep(1)
                # hashtag()
                sleep(2)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_post").click()
                sleep(2)
                el3 = wait(type='id', el="android:id/button1")
                if el3:
                    driver.find_element_by_id("android:id/button1").click()
                else:
                    deepblu.log("Please check the screen shoot")
                sleep(2)
                checkel = wait(type='xpath', el=postIcon)
                if checkel:
                    screenshot("PostLink")
                else:
                    deepblu.log('Please check the screen shoot')
            else:
                deepblu.log("Please check the screen shoot")
        else:
            deepblu.log("Please check the screen shoot")

    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Post Link] end")


def post_photo():
    deepblu.log("[Post Photo] start")
    try:
        postIcon = GlobalString.create_post
        el = wait(type='xpath', el=postIcon)
        if el:
            driver.find_element_by_xpath(postIcon).click()
            sleep(2)
            el2 = wait(type="id", el="com.deepblu.android.deepblu.internal:id/photo_post_group")
            if el2:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/photo_post_group").click()
            else:
                deepblu.log("Please check the screen shoot")

            el3 = wait(type="id", el="com.android.packageinstaller:id/permission_allow_button")
            if el3:
                driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
                sleep(1)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_media").click()
                sleep(1)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/add_more_media").click()
                sleep(2)

                elphoto = driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]")
                # 選一張照片
                elphoto.click()

                # 選多張照片
                # TouchAction(driver).long_press(elphoto,None,None,5000).perform()
                # el4 = wait(type="xpath", el="//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]")
                # if el4:
                #     driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]").click()
                #     driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[3]").click()
                #     driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[4]").click()
                #
                # driver.find_element_by_id("com.android.documentsui:id/menu_sort").click()
                back()
            else:
                elphoto = driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]")
                TouchAction(driver).long_press(elphoto, None, None, 5000).perform()
                el4 = wait(type="xpath",
                           el="//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]")
                if el4:
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]").click()
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[3]").click()
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[4]").click()

                driver.find_element_by_id("com.android.documentsui:id/menu_sort").click()

            content = ""
            content = "[AutoTest]\n" + Dtool.randomword(10, GlobalString.bio) + "\n" + time.strftime("%Y%m%d%H%M%S")
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").send_keys(content)
            # sleep(1)
            # hashtag()
            sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_post").click()
            sleep(2)
            el3 = wait(type='id', el="android:id/button1")
            if el3:
                driver.find_element_by_id("android:id/button1").click()
            else:
                deepblu.log("Please check the screen shoot")
            sleep(2)
            checkel = wait(type='xpath', el=postIcon)
            if checkel:
                screenshot("PostPhoto")
            else:
                deepblu.log('Please check the screen shoot')
        else:
            deepblu.log("Please check the screen shoot")

    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Post Photo] end")


def post_video():
    deepblu.log("[Post Video] start")
    try:
        postIcon = GlobalString.create_post
        el = wait(type='xpath', el=postIcon)
        if el:
            driver.find_element_by_xpath(postIcon).click()
            sleep(2)

            el2 = wait(type="id", el="com.deepblu.android.deepblu.internal:id/video_post_group")
            if el2:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/video_post_group").click()
            else:
                deepblu.log("Please check the screen shoot")

            el3 = wait(type="id", el="com.android.packageinstaller:id/permission_allow_button")
            if el3:
                driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
                sleep(1)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_media").click()
                sleep(1)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/add_more_media").click()
                sleep(2)

                videoel = wait(type="xpath",
                               el="//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
                if videoel:
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                else:
                    deepblu.log("Please check the screen shoot")
                sleep(2)
                back()
            else:
                videoel = wait(type="xpath",
                               el="//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
                if videoel:
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
                else:
                    deepblu.log("Please check the screen shoot")
            sleep(5)
            content = ""
            content = "[AutoTest]\n" + Dtool.randomword(10, GlobalString.bio) + "\n" + time.strftime("%Y%m%d%H%M%S")
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").send_keys(content)
            # sleep(1)
            # hashtag()
            sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_post").click()
            sleep(2)
            el3 = wait(type='id', el="android:id/button1")
            if el3:
                driver.find_element_by_id("android:id/button1").click()
            else:
                deepblu.log("Please check the screen shoot")

            checkel = wait(type='xpath', el=postIcon)
            if checkel:
                screenshot("PostVideo")
            else:
                deepblu.log('Please check the screen shoot')
        else:
            deepblu.log("Please check the screen shoot")
    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Post Video] end")


# sign up with email
# should be samsung IME
def signup(username=None, email=None, password=None):
    deepblu.log("[Sign up] start")
    try:
        if username == None:
            username = "test" + time.strftime("%m%d%H%M")
        if email == None:
            email = username + "@deepblu.com"
        if password == None:
            password = 'a12345678'
        el = wait(type="id", el="com.deepblu.android.deepblu.internal:id/buttonSignUpWithEmail")
        if el:
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUpWithEmail").click()
            sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextUserName").send_keys(username)
            back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(email)
            back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextPassword").send_keys(password)
            back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUp").click()
            # check signup successful or not
            elcheck = wait(type='id', el="com.deepblu.android.deepblu.internal:id/activity_toolbar_title")
            if elcheck:
                screenshot('SignUp')
            else:
                deepblu.log('Please check the screen shoot')

            deepblu.log("[Sign up] end")
            return email

        else:
            deepblu.log("Please check the screen shoot")
    except Exception as e:
        deepblu.log(e, 'w')


# verify:code/url
def verify(verify='code', Useremail=None):
    deepblu.log("[Verify] start")
    try:
        # if way ==None:
        #     Useremail = signup()
        # else :
        #     Useremail =way
        # sleep(3)
        verifydict = {}
        verifydict = Dtool.getusercode(Useremail)
        if len(verifydict) == 0:
            deepblu.log("Cannot get verify code.Please check the screen")
        else:
            if verify == "code":
                code = verifydict["code"]
                driver.find_element_by_id(
                    "com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_1").send_keys(code[0:1])
                driver.find_element_by_id(
                    "com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_2").send_keys(code[1:2])
                driver.find_element_by_id(
                    "com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_3").send_keys(code[2:3])
                driver.find_element_by_id(
                    "com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_4").send_keys(code[3:4])
                screenshot("Verify_code")
            else:
                link = verifydict["link"]
                Dtool.verify_by_link(link)
                screenshot("Verify_link")
            sleep(3)
        success = wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right")
        if success:
            screenshot("Veirfy")
        else:
            screenshot("Veirfyfail")
            deepblu.log("Please check the screen shoot")

    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Verify] end")


def signup_skip():
    deepblu.log("[Sign up and skip] start")
    try:
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/fragment_signup_verify_skip_text").click()
        sleep(2)
        # check skip successful or not
        checkel = wait(type='xpath', el=GlobalString.create_post)
        if checkel:
            screenshot("SignUpSkip")
        else:
            deepblu.log("Please check the screen shoot", "w")

        deepblu.log("[Sign up and skip] end")
    except Exception as e:
        deepblu.log(e, 'w')


def signup_token_expire(Useremail):
    deepblu.log("[Sign up token expire] start")
    try:
        # token expired
        token = Dtool.token_expired(Useremail)
        if token:
            driver.find_element_by_xpath(GlobalString.tab + "[2]").click()
            sleep(2)
            # check token expired successfully or not(enter to email verify page)
            checkel = wait(type='id', el="com.deepblu.android.deepblu.internal:id/activity_toolbar_title")
            if checkel:
                screenshot("SignUpTokenExpire")
            else:
                deepblu.log("Please check the screenshot", 'w')
        else:
            screenshot("tokenExpireFailed")
            deepblu.log("Please check the screenshot.", 'w')
    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Sign up token expire] end")


def signup_change_email():
    deepblu.log("[Sign up change email] start")
    try:
        Useremail = signup()
        sleep(2)
        # 確認有成功換email 切換到驗證頁
        el2 = wait(type="id", el="com.deepblu.android.deepblu.internal:id/fragment_signup_verify_hint_msg")
        if el2:
            # change email
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/fragment_signup_verify_change").click()
            sleep(2)
            changeUseremail = "change" + Useremail
            # print('ChangeEmail:'+changeUseremail)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(
                changeUseremail)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUp").click()
            sleep(3)
            # verify code after change email
            verify(verify='code', Useremail=changeUseremail)
            success = wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right")
            if success:
                screenshot("SignUp_changeEmail")
            else:
                deepblu.log("Please check the screen shoot")
        else:
            deepblu.log("Please check the screen shoot")
    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Sign up change email] end")


def signup_resend_email():
    deepblu.log("[Sign up resend email] start")
    try:
        Useremail = signup()
        # resend
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/fragment_signup_verify_resend").click()
        sleep(0.5)
        screenshot('SignUp_resendEmail')
        sleep(2)

        # verify code after resend email
        verify(verify='code', Useremail=Useremail)
        success = wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right")
        if success:
            screenshot("SignUp_resendEamil_success")
        else:
            screenshot("SignUpfail")
            deepblu.log("Please check the screen shoot")

    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Sign up resend email] end")


def signup_with_existed_email():
    deepblu.log("[Sign up with existed email] start")
    try:
        el = wait(type="id", el="com.deepblu.android.deepblu.internal:id/buttonSignUpWithEmail")
        if el:
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUpWithEmail").click()
            sleep(2)
            Useremail = desired_capabilities.account()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextUserName").send_keys(
                "ExistedUser")
            back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(Useremail)
            back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextPassword").click()
            # check successful or not
            elcheck = wait(type='id', el="com.deepblu.android.deepblu.internal:id/editTextEmailError")
            if elcheck:
                screenshot('SignupExistedEmail')
            else:
                deepblu.log('Please check the screen shoot')
        else:
            deepblu.log("Please check the screen shoot")
    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Sign up with existed email] end")


# 要先verify過才能執行此function
def edit_profile_after_signup():
    deepblu.log("[Edit Profile after sign up] start")
    try:
        sleep(2)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right").click()
        sleep(2)
        checkel = wait(type='id', el='com.deepblu.android.deepblu.internal:id/edit_text_user_name')
        if checkel:
            screenshot('editProfileAfterSignup')
        else:
            deepblu.log('Please check the screenshot')
    except Exception as e:
        deepblu.log(e, 'w')
    deepblu.log("[Edit Profile after sign up] end")


def browser():
    os.popen("adb shell am start -a android.intent.action.VIEW -d 'http://stackoverflow.com/?uid=isme\&debug=true'")


def home_screen():
    back()
    home()
    home()
    back()


def home():
    driver.press_keycode(3)


def back():
    driver.press_keycode(4)


def enter():
    driver.press_keycode(66)


def sleep(x):
    time.sleep(x)


def kill_app():
    deepblu.log('[kill app] start')
    driver.close_app()
    # os.popen("adb shell am force-stop com.deepblu.android.deepblu.internal")
    deepblu.log('[kill app] end')


def open_app():
    deepblu.log('[open app] start')
    os.popen('adb shell am start -n com.deepblu.android.deepblu.internal/'
             'com.deepblu.android.deepblu.screen.loading.LoadingActivity')
    deepblu.log('[open app] end')


# clear cache and data
def clear_app():
    deepblu.log('[clear app] start')
    os.popen("adb shell pm clear com.deepblu.android.deepblu.internal")
    deepblu.log('[clear app] end')


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
        waite_element = WebDriverWait(driver, time).until(EC.presence_of_element_located((type, el)))
        return True
    except Exception as e:
        screenshot("Error")
        deepblu.log("[Error] The element: %s can't be found. %s" % (el, e), 'w')
        return False


def screenshot(file_name):
    directory = '%s/' % os.getcwd() + 'AndroidAppTest/' + time.strftime("%Y%m%d") + '/'
    if not os.path.exists(directory):  # 先確認資料夾是否存在
        os.makedirs(directory)
    # print(directory)
    screenshot = driver.save_screenshot(directory + time.strftime('%H%M%S') + '_' + file_name + ".png")


# 0.8滑到0.1 大滑動
def swipeup():
    try:
        # 絕對位置 起始點 結束點
        list = size()
        startx = list[1] * 0.2
        starty = list[0] * 0.8
        endy = list[0] / 10
        # print("x1:" + str(startx) + " y1:" + str(starty) + " x2:" + str(startx) + " y2:" + str(endy))
        driver.swipe(startx, starty, startx, endy, 500)
        # driver.swipe(640,2320,640,400,100)
    except Exception as e:
        deepblu.log(e, 'w')


# 14/16滑到12/16  小滑動
def swipeup2():
    try:
        # 絕對位置 起始點 結束點
        list = size()
        startx = list[1] * 0.2
        starty = list[0] * 0.875
        endy = list[0] * 0.75
        # print("x1:" + str(startx) + " y1:" + str(starty) + " x2:" + str(startx) + " y2:" + str(endy))
        driver.swipe(startx, starty, startx, endy, 500)
        # driver.swipe(640,2320,640,400,100)
    except Exception as e:
        deepblu.log(e, 'w')


def size():
    dict = {}
    dict = driver.get_window_size()
    list = []
    list.append(dict['height'])
    list.append(dict['width'])
    # print("H: "+str(list[0]))
    # print("W: "+str(list[1]))

    return list


def isElementPresent(by):
    try:
        driver.find_element_by_xpath(by)

        return 1

    except Exception as e:
        deepblu.log(e, 'w')
        print("failed")
        return 0


def changePhoto(file, photo):
    try:
        x1 = "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]" \
             "/android.view.View[1]/com.sec.samsung.gallery.glview.composeView.PositionControllerBase.ThumbObject[" + file + "]"
        x2 = "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/" \
             "android.view.View[1]/com.sec.samsung.gallery.glview.composeView.PositionControllerBase.ThumbObject[" + photo + "]"
        driver.find_element_by_xpath(x1).click()
        sleep(3)
        el = wait(type='xpath', el=x2)
        el.click()
        sleep(2)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/menu_crop").click()
        sleep(2)
    except Exception as e:
        deepblu.log(e, 'w')


def hashtag():
    try:
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_hashtag").click()
        sleep(1)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/new_hash_tag").send_keys("TestHashTag")
        enter()
    except Exception as e:
        deepblu.log(e, 'w')
