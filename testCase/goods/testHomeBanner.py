import paramunittest
from common import mUtils
from common.mBaseCase import MyBaseCase
from common import HTMLTestReportCN

banner = mUtils.get_xls("goodsCase.xls", "HBanner")  # lists contains many list

@paramunittest.parametrized(*banner)
class HomeBanner(MyBaseCase):

    # 3
    def testBanner(self):
        url = self.iniParser.getItem('goodsSite', 'homeBanner')  # '/memberSite/sso/loginJson'
        params = self.zipParams(self.getParamsTitle("goodsCase.xls", "HBanner"), self.getParamsValue())
        self.mRequest.setRequest(url, params, self.method)
        self.res = self.mRequest.send()
        self.checkResult(self.res)

if __name__ == '__main__':
    import unittest
    suite = unittest.defaultTestLoader.discover('./', pattern='testHomeBanner.py',top_level_dir=None)
    print('suite:', suite)
    if suite is not None:
        with open('report.html', 'wb') as oFile:
            runner = HTMLTestReportCN.HTMLTestRunner(stream=oFile, title='Test Report',description='Test Description')
            runner.run(suite)
