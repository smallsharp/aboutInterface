import paramunittest
from common import mUtils
from common.mBaseCase import MyBaseCase
import requests
from common import HTMLTestReportCN

banner = mUtils.getLines("goodsCase.xls", "HBanner2")  # lists contains many list


# @paramunittest.parametrized(*banner)
class HomeBanner(MyBaseCase):

    # 3
    def testBanner(self):
        session = self.initSession()
        self.res = None
        if self.method.lower() == 'post':
            # self.res = session.post(self.url,self.params)
            self.res = requests.post(self.url, json=self.params,cookies = session.cookies)
        elif self.method.lower() == 'get':
            self.res = session.get(self.url, params=self.params)

        # print(self.res.headers)
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
