import paramunittest
import unittest
from common import mUtils
from common.mBaseCase import MyBaseCase

# 0
cases = mUtils.getLines("userCase.xls", "login")  # lists contains many list

# [['login', 'get', 18521035133.0, 123456.0, '0', '220119', 'account or password error!']]
@paramunittest.parametrized(*cases)
class Login(MyBaseCase):

    # 3
    def testLogin(self):
        print("run testCase")
        print('url:%s, params:%s, method:%s'%(self.url,self.params,self.method))
        self.mRequest.setRequest(self.url, self.params, self.method)
        res = self.mRequest.send()
        print(res.json())
        self.checkResult(res.json())


if __name__ == '__main__':
    unittest.main()
