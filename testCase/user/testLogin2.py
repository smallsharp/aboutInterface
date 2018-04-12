import unittest
import paramunittest
import mParser
from common import Log as Log
from common import utils
from common import mHttp as ConfigHttp

login_xls = utils.get_xls("userCase.xlsx", "login")
# ['login', 'get', 18521035133.0, 123456.0, '0', '220119', 'account or password error!']
# ['login_PasswordError', 'get', 18521035133.0, 111111.0, '1', '200', 'success!']
mhttp = ConfigHttp.MyHttp()
log = Log.MyLog.get_log()
logger = log.get_logger()
iniParser = mParser.MyIniParser('../../interface.ini')

@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):

    def setParameters(self, case_name, method, loginAccount, password, result, code, msg):
        print("set Parameters")
        self.case_name = str(case_name)
        self.method = str(method)
        self.loginAccount = self.checkNum(loginAccount)
        self.password = self.checkNum(password)
        self.result = str(result)
        self.codeExp = self.checkNum(code)
        self.msgExp = str(msg)
        self.res = None
        self.resJson = None

    def checkNum(self, num):
        """
        防止数值类型转换
        :param num:
        :return:
        """
        if num == int(num):
            return int(num)
        return num

    def setUp(self):
        print('setup')
        print(self.case_name + "准备进入测试")


    def testLogin(self):
        print('test')
        # self.url = utils.get_url_from_xml('login')
        # self.uri = '/memberSite/sso/loginJson'
        self.uri =iniParser.getItem('memberSite','login')
        print("第一步：设置url  " + self.uri)
        mhttp.set_url(self.uri)

        print("第二步：设置header(token等)")

        # set params
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
    import os
    # project_dir = os.path.dirname(os.path.abspath(__file__))
    # print(project_dir)
    # iniParser = mParser.MyIniParser('../../interface.ini')
    # print(iniParser.getItem('memberSite', 'login'))