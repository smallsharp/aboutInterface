import paramunittest
from common import mUtils
from common.mBaseCase import MyBaseCase
from common import HTMLTestReportCN


# login = mUtils.get_xls("userCase.xls", "login")  # lists contains many list


def getSheets():
    return ['login', 'categoryProductList']

cases = []
for sheet in getSheets():
    case = mUtils.get_xls('userCase.xls',sheet)
    cases.append(cases)

# [['login', 'get', 18521035133.0, 123456.0, '0', '220119', 'account or password error!']]
@paramunittest.parametrized(*cases)
class Login(MyBaseCase):

    # 3
    def testCase(self):
        # uri = self.iniParser.getItem('memberSite', 'login')  # '/memberSite/sso/loginJson'
        # params = self.zipParams(self.getParamsTitle("userCase.xls", "login"), self.getParamsValue())
        self.mRequest.setRequest(self.url, self.params, self.method)
        res = self.mRequest.send()
        print(res.json())
        self.checkResult(res.json())


if __name__ == '__main__':
    import unittest
    suite = unittest.defaultTestLoader.discover('./', pattern='test*.py', top_level_dir=None)
    print('suite:', suite)
    if suite is not None:
        with open('report.html', 'wb') as oFile:
            runner = HTMLTestReportCN.HTMLTestRunner(stream=oFile, title='Test Report',
                                                     description='Test Description')
            runner.run(suite)
