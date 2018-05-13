import paramunittest
from common import mUtils
from common.mBaseCase import MyBaseCase
import requests
from common import HTMLTestReportCN

banner = mUtils.get_xls("goodsCase.xls", "HBanner2")  # lists contains many list

@paramunittest.parametrized(*banner)
class HomeBanner(MyBaseCase):

    session=None

    def getSession(self):
        global session

        login_url = "https://m.taidu.com/memberSite/sso/loginJson"
        login_params = {'loginAccount': '18521035133', 'password': '111111', 'code': '', 'rememberMe': '1', 'clientType': 'H5', 'abbr': 'CN', 'clientVersion': '', 'sign': '87823FC7334C13955C8B451B48027954'}
        session = requests.Session()
        # session.keep_alive=False
        requests.adapters.DEFAULT_RETRIES = 5
        session.get(url=login_url, params=login_params, verify=False)  # verify=False 关闭证书验证，但是仍然会报出证书警告
        # cookies = session.cookies
        # for c, v in cookies.items():
        #     print(c, v)
        return session

    #3
    def testBanner(self):
        session = requests.Session()
        self.res = None
        if self.method.lower()=='post':
            self.res = session.post(self.url,self.params)
            print('res:',self.res.text)
        elif self.method.lower()=='get':
            self.res= session.get(self.url,params=self.params)
            print('res:',self.res.text)

        print(self.res.headers)
        self.checkResult(self.res.text)


if __name__ == '__main__':
    import unittest
    # suite = unittest.defaultTestLoader.discover('./', pattern='testHomeBanner.py',top_level_dir=None)
    # print('suite:', suite)
    # if suite is not None:
    #     with open('report.html', 'wb') as oFile:
    #         runner = HTMLTestReportCN.HTMLTestRunner(stream=oFile, title='Test Report',description='Test Description')
    #         runner.run(suite)
    unittest.main()
