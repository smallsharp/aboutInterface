import paramunittest
from common import mUtils
import requests
import unittest

banner = mUtils.get_xls("goodsCase.xls", "HBanner2")  # lists contains many list

@paramunittest.parametrized(*banner)
class HomeBanner(unittest.TestCase):


    # 1 接受请求参数，进行处理，使用参数化时，这个方法必须写
    def setParameters(self, *data):
        print("origin data:", data)
        self.case, self.method, self.url, self.headers, self.params, self.codeExp, self.msgExp = data

    #3
    def testBanner(self):
        print('start test')
        self.res = None
        if self.method.lower()=='post':
            # self.res = session.post(self.url,self.params)
            self.res = requests.post(self.url,json=self.params)
        elif self.method.lower()=='get':
            # self.res= session.get(self.url,params=self.params)
            self.res = requests.get(self.url,params=self.params)

        print(self.res.text)


if __name__ == '__main__':
    import unittest
    # suite = unittest.defaultTestLoader.discover('./', pattern='testHomeBanner.py',top_level_dir=None)
    # print('suite:', suite)
    # if suite is not None:
    #     with open('report.html', 'wb') as oFile:
    #         runner = HTMLTestReportCN.HTMLTestRunner(stream=oFile, title='Test Report',description='Test Description')
    #         runner.run(suite)
    unittest.main()
