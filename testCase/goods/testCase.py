import paramunittest
from common import mUtils
import requests
import unittest
import json


class HomeBanner(unittest.TestCase):

    session = None

    def setUp(self):
        print('setup')
        self.lines = mUtils.getLines("goodsCase.xls", "HBanner2")  # lists contains many list

        global session
        session = requests.session()



    def getCookies(self):
        with open('cookies.txt','r') as file:
            return json.load(file)

    def testMethod(self):
        for line in self.lines:
            # for v in line:
            #     print(v)
            print(line)
            url = line[2]
            headerType = line[3]
            params = line[4]
            print(headerType)
            if headerType.lower() == 'w':
                # res = requests.get(url, params)
                res = session.get(url,data = params)
                session.headers.update({'Cookie':session.cookies})
                print(res.text)

                # with open('cookies.txt', 'w') as file:
                #     file.write(json.dumps(requests.utils.dict_from_cookiejar(res.cookies)))

            elif headerType.lower() == 'y':
                # res = requests.post(url, params, cookies=self.getCookies())

                res = requests.post(url, data=params, headers=session.cookies)
                print('res:',res.text)

            elif headerType.lower() == 'n':
                res = requests.get(url, params)
                print(res.text)

            else:
                break


if __name__ == '__main__':
    import unittest

    unittest.main()
