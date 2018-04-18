import paramunittest
from common import mUtils
from common.mBaseCase import MyBaseCase

login = mUtils.get_xls("userCase.xls", "login")  # lists contains many list
# [['login', 'get', 18521035133.0, 123456.0, '0', '220119', 'account or password error!']]
@paramunittest.parametrized(*login)
class Login(MyBaseCase):

    # 3
    def testLogin(self):
        uri = self.iniParser.getItem('memberSite', 'login')  # '/memberSite/sso/loginJson'
        params = self.zipParams(self.getParamsTitle("userCase.xls", "login"), self.getParamsValue())
        self.mRequest.setRequest(uri, params, self.method)
        self.res = self.mRequest.send()
        self.checkResult(self.res)

if __name__ == '__main__':
    import unittest
    unittest.main()
