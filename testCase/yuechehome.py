import requests
import json
import time
import datetime


def login():
    url = 'https://api.yunchehome.com/app/user/login'
    params = {"mobile": "18521035133", "password": "96e79218965eb72c92a549dd5a330112"}

    try:
        startTime = datetime.datetime.now()
        res = requests.post(url, json=params)
        if res.status_code == 200:
            endTime = datetime.datetime.now()
            print((endTime - startTime).total_seconds())
            print(res.text)
            resJson = json.loads(res.text)
            token = resJson['retData']['token']
            uid = resJson['retData']['uid']
            return token, uid
        else:
            print(res.status_code)

    except Exception as e:
        print('Error')


def userInfo(token, uid):
    url = 'https://api.yunchehome.com/app/LUser/UserCenter'
    params = {'token': token, 'uid': uid}
    res = requests.post(url, json=params)
    print(res.text)


token, uid = login()

userInfo(token, uid)
