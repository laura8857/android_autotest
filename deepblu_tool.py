# -*- coding: utf-8 -*-

import random
import json
import requests
import os
from pymongo import *
import deepblu_lib as deepblu
import action


#隨機字串
def randomword(size=10,chars=""):
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


#註冊驗證號碼
def getusercode(email):
    print('email:'+email)
    url = "http://test.tritondive.co:3000/1/api/users?access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79Wwr" \
          "QtOlgRC9sQmKmzYAfqqy&filter={\"where\":{\"email\":\""+email+"\"}}"
    result = requests.get(url)
    if result.status_code==200:
        if len(result.json()) == 1:
            user_code=""
            user_code=result.json()[0]['code']
            print("usercode:"+str(user_code))
            link = "https://test.tritondive.co/apis/user/v0/activeAccount?ownerId=" + result.json()[0]['id'] + "&code=" + user_code
            dict = {"code": user_code, "link": link}
            return dict
        else:
            return {}
#驗證 link
def verify_by_link(url):
    json = {"accept-language": "en"}
    res = requests.get(url,headers=json)


#使當前token過期
def token_expired(email):
    try:
        # connect to mongo
        client = MongoClient("52.197.14.177", 27017)
        client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
        db = client.deepblu

        if db.user.find_one({"email":email}):
            user = {}
            token =""
            user = db.user.find_one({"email": email})
            id = user['_id']
            print(str(id))

            for doc in db.AccessToken.find({"userId":id}).sort("created",-1).limit(1):
                token = doc['_id']
                print(token)

            #call api
            url = "http://test.tritondive.co:8000/apis/user/v0/tokenExpire"
            data = {}
            data['accessToken']=token
            headers = {"Accept-Language": "en"}
            result = requests.post(url, json=data, headers=headers)
            if result.status_code == 200:
                print(result.text)
                return True
        else:
            deepblu.log("The mail "+email+" can't be found.","w")
            #print("The mail "+email+" can't be found.")
            return False

        client.close()
    except Exception as e:
        deepblu.log(e)
        return False
