import unittest
import paramunittest
import mParser
from common import mLog
from common import utils
from common import mHttp
import os

login = utils.get_xls("userCase.xlsx", "login")
titles = utils.get_xls_title("userCase.xlsx", "login")
# ['case_name', 'method', 'loginAccount', 'password', 'result', 'code', 'msg']
# ['login', 'get', 18521035133.0, 123456.0, '0', '220119', 'account or password error!']
# ['login_PasswordError', 'get', 18521035133.0, 111111.0, '1', '200', 'success!']

mhttp = mHttp.MyHttp()
log = mLog.MyLog.get_log()
logger = log.get_logger()
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
iniParser = mParser.MyIniParser(PATH('../../interface.ini'))


@paramunittest.parametrized(*login)
class Login(unittest.TestCase):

    # def setParameters(self, case_name, method, loginAccount, password, result, code, msg):
    #     print("set Parameters")
    #     self.case_name = str(case_name)
    #     self.method = str(method)
    #     self.loginAccount = self.checkNum(loginAccount)
    #     self.password = self.checkNum(password)
    #     self.result = str(result)
    #     self.codeExp = self.checkNum(code)
    #     self.msgExp = str(msg)
    #     self.res = None
    #     self.resJson = None

    def setParameters(self, *params):
        # params:('login_PasswordError', 'get', 18521035133.0, 111111.0, '1', '200', 'success!')
        self.case_name, self.method, *args, self.result, self.codeExp, self.msgExp = params
        self.reqParams = args  # [18521035133.0, 111111.0]

    def checkNum(self, num):
        if num == int(num):
            return int(num)
        return num

    def setUp(self):
        print("{}准备进入测试".format(self.case_name))

    def testLogin(self):
        print('开始执行测试')
        self.uri = iniParser.getItem('memberSite', 'login') # '/memberSite/sso/loginJson'
        print("第一步：设置url  " + self.uri)
        mhttp.set_url(self.uri)

        print("第二步：设置header(token等)")

        # set params
        # ['case_name', 'method', 'loginAccount', 'password', 'result', 'code', 'msg']
        # ['login', 'get', 18521035133.0, 123456.0, '0', '220119', 'account or password error!']
        params = {"loginAccount": self.loginAccount, "password": self.password}
        mhttp.set_params(params)
        print("第三步：设置发送请求的参数:", params)

        # test interface
        self.res = mhttp.get()
        print("第四步：发送请求,请求方法：" + self.method)

        # check result
        print("第五步：检查结果")
        self.checkResult()

    def tearDown(self):
        print('teardown')
        if self.resJson['code'] == 200:
            # get uer token
            token_u = utils.get_value(self.resJson, 'member', 'token')
            # set user token to config file
            # config.set_headers("TOKEN_U", token_u)
        else:
            pass
        log.build_case_line(self.case_name, self.resJson['code'], self.resJson['message'])
        print("{}测试结束".format(self.case_name))

    def checkResult(self):
        print('check')
        print('result:', self.result)
        self.resJson = self.res.json()
        # show return message
        utils.show_return_msg(self.res)

        if self.result == '0':
            # email = utils.get_value(self.resJson, 'member', 'email')
            print('resJson:', self.resJson)
            print("codeReal:", self.resJson['code'], type(self.resJson['code']))
            print("codeExp:", self.codeExp, type(self.codeExp))
            self.assertEqual(self.resJson['code'], str(int(self.codeExp)))
            self.assertEqual(self.resJson['message'], self.msgExp)
            # self.assertEqual(email, self.email)

        elif self.result == '1':
            self.assertEqual(self.resJson['code'], self.codeExp)
            self.assertEqual(self.resJson['message'], self.msgExp)

        else:
            print('result:', self.result)


if __name__ == '__main__':
    unittest.main()
