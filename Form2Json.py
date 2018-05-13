# coding=utf-8
"""
@Time:2018-03-1019:19
@Author:lfl5207
"""
import requests


def str2dict(str_f):
    dictF = dict()
    list_one = str_f.split('&')
    for l in list_one:
        list_t = l.split("=")
        key, value = list_t[0], list_t[1]
        dictF[key] = value
    return dictF


def login():
    login_url = "https://app.cmall.com/memberSite/sso/loginJson"
    login_params = {"loginAccount": "18833330001", "password": "111111", "clientType": "ios", "abbr": "CN"}
    res = requests.post(url=login_url, data=login_params)
    return res


def add2Cart():
    """
    加入购物车
    :return:
    """
    url = "https://apimerch.cmall.com/restwsapis/open/order/saveShoppingCart?st=1522404883227&clientId=f03b23fe-c74c-4968-a73a-7567b363ba67&tepComInfo=%7B%22clientType%22%3A%2200%22%2C%22skuniCode%22%3A%2280001_80001128_0%22%2C%22productId%22%3A%2280001%22%2C%22imgUri%22%3A%22%5B%7B%5C%22height%5C%22%3A369%2C%5C%22href%5C%22%3A%5C%22stag%2Fmodel%2F2D%2FgoodsSvgTemplate%2F20180205060254%2F3823%2F1%2F910EF0FC.png%5C%22%2C%5C%22imgFlag%5C%22%3A1%2C%5C%22isMaterial%5C%22%3A0%2C%5C%22isSuit%5C%22%3A%5C%22N%5C%22%2C%5C%22locked%5C%22%3Afalse%2C%5C%22maskX%5C%22%3A124.99997%2C%5C%22maskY%5C%22%3A627.537%2C%5C%22matrix%5C%22%3A%5C%22matrix%281.0+0.0+-0.0+1.0+124.99997+627.537%29%5C%22%2C%5C%22url%5C%22%3A%5C%22stag%2Fmodel%2F2D%2FgoodsSvgTemplate%2F20180205060254%2F3823%2F1%2F910EF0FC.png%5C%22%2C%5C%22width%5C%22%3A750%7D%5D%22%2C%22productDesignType%22%3A%222%22%2C%22opusUri%22%3A%22nospc%2Fandroid%2F2018%2F3%2F30%2Fthumbl_15224048808252018033042539.png%22%2C%22goodsId%22%3A%223823%22%2C%22words%22%3A%22%5B%5D%22%2C%22clientVersion%22%3A%222.0.0%22%2C%22abbr%22%3A%22CN%22%2C%22userId%22%3A%22wuta-1%22%2C%22tckd%22%3A%22F809347B3FC1593F89BBB6600EF8C5F4%22%7D&clientVersion=1.0&userId=wuta-1&dModel=MHA-AL00&skuJson=%5B%7B%22skuValue%22%3A%22%E7%A1%AC%E5%A3%B3%E9%BB%91%22%2C%22skuName%22%3A%22%E9%A2%9C%E8%89%B2%22%7D%2C%7B%22skuValue%22%3A%22iPhone+X%22%2C%22skuName%22%3A%22%E5%B0%BA%E7%A0%81%22%7D%5D&goodsCount=1&clientType=android&osVersion=26&partner=&goodsPrice=69.0&dBrand=HUAWEI&client=android&clientSecret=ba1962c4-0e90-4fa0-bfa2-3f7096a9dcbb&imagePixels=1080&rememberMe=1&abbr=CN&udid=F809347B3FC1593F89BBB6600EF8C5F4&imagePHeight=1808&networkType=WIFI&goodsName=iPhone%E6%89%8B%E6%9C%BA%E5%A3%B3&sign=EBD9B5A4CDE99698D10AA0F1CA323014"
    res = requests.get(url)
    return res


if __name__ == '__main__':

    # for i in range(100):
    #     try:
    #         add2Cart()
    #         print("添加第%d条成功" % i)
    #     except Exception:
    #         print("第%d条,添加失败" % i)

    str2 = 'pageSize=100&currPage=1&status=0%2C21%2C22&clientType=H5&abbr=CN&clientVersion=&sign=2E269FE54CF9E1C08396EA94F056DEE9'

    d = str2dict(str2)
    print(d)