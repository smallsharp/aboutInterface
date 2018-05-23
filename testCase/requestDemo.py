import requests
import json


def writeCookies():

    url = 'https://m.taidu.com/memberSite/sso/loginJson?loginAccount=18521035133&password=111111&code=&rememberMe=1&clientType=H5&abbr=CN&clientVersion=&sign=87823FC7334C13955C8B451B48027954'
    res = requests.get(url)

    with open('cookies.txt', 'w') as file:
        file.write(json.dumps(requests.utils.dict_from_cookiejar(res.cookies)))



def readCookies():

    with open('cookies.txt','r') as readFile:
        content = json.load(readFile)


    print(type(content))

    url = 'https://m.taidu.com/memberSite/members/homeIndex?memberId=2199587&clientType=H5&abbr=CN&clientVersion=&sign=BFF9453ADCA0A76D371322C3C98DD27C'
    res = requests.get(url,headers=content)
    print(res.text)


    url2 = 'https://m.taidu.com/orderPaySite/tude/cart/cartList'
    params = {'abbr': 'CN', 'pageNo': '1', 'clientType': 'H5', 'pageSize': '200', 'clientVersion': '', 'sign': 'FF1AEE6E87BF3B9132FE9621A1E1A941'}
    res2 = requests.post(url2,data=params,cookies = content)
    print(res2.text)


    


writeCookies()
readCookies()


