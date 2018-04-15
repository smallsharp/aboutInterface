import paramunittest
from common import utils
from common.mBaseCase import MyBaseCase

login = utils.get_xls("userCase.xlsx", "login")  # lists contains many list
# [['login', 'get', 18521035133.0, 123456.0, '0', '220119', 'account or password error!']]
@paramunittest.parametrized(*login)
class Login(MyBaseCase):

    # 3
    def testLogin(self):
        self.uri = self.iniParser.getItem('memberSite', 'login')  # '/memberSite/sso/loginJson'
        self.mhttp.set_url(self.uri)

        params = self.zipParams(self.getParamsTitle("userCase.xlsx", "login"), self.getParamsValue())
        # params = {"loginAccount": self.loginAccount, "password": self.password}
        self.mhttp.set_params(params)
        self.res = self.mhttp.get()

        # check result
        self.checkResult()

if __name__ == '__main__':
    import unittest

    unittest.main()
