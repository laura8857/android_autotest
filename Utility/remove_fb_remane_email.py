# -*- coding: utf-8 -*-
# @Time    : 2017/3/10 下午3:16
# @Author  : Yuhsuan
# @File    : remove_facebook_connect.py
# @Software: PyCharm Community Edition

from pymongo import *
from datetime import datetime


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

    client.close()
if __name__=="__main__":
    rm_email("hi@deepblu.com")
    rm_fb("")


