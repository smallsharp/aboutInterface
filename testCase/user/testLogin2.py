import unittest
import paramunittest
import mParseIni
from common import Log as Log
from common import utils
from common import mHttp as ConfigHttp

login_xls = utils.get_xls("userCase.xlsx", "login")
config = mParseIni.ReadConfig()
mhttp = ConfigHttp.MyHttp()


@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):

    def setParameters(self, case_name, method, loginAccount, password, result, code, msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.loginAccount = self.checkNum(loginAccount)
        self.password = self.checkNum(password)
        self.result = str(result)
        self.codeExp = self.checkNum(code)
        self.msgExp = str(msg)
        self.res = None
        self.resJson = None

    def checkNum(self,num):
        """
        防止数值类型转换
        :param num:
        :return:
        """
        if num == int(num):
            return  int(num)
        return num

    def setUp(self):
        print(self.case_name + "准备进入测试")
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testLogin(self):
        # self.url = utils.get_url_from_xml('login')
        self.url = '/memberSite/sso/loginJson'
        mhttp.set_url(self.url)
        print("第一步：设置url  " + self.url)

        print("第二步：设置header(token等)")

        # set params
        params = {"loginAccount": self.loginAccount, "password": self.password}
        mhttp.set_params(params)
        print("第三步：设置发送请求的参数:",params)

        # test interface
        self.res = mhttp.get()
        print("第四步：发送请求,请求方法：" + self.method)

        # check result
        print("第五步：检查结果")
        self.checkResult()

    def tearDown(self):
        info = self.resJson
        if info['code'] == 0:
            # get uer token
            token_u = utils.get_value_from_return_json(info, 'member', 'token')
            # set user token to config file
            config.set_headers("TOKEN_U", token_u)
        else:
            pass
        self.log.build_case_line(self.case_name, self.resJson['code'], self.resJson['message'])
        print("测试结束，输出log完结")

    def checkResult(self):
        print('result:',self.result)
        self.resJson = self.res.json()
        # show return message
        utils.show_return_msg(self.res)

        if self.result == '0':
            # email = utils.get_value_from_return_json(self.resJson, 'member', 'email')
            print('resJson:',self.resJson)
            print("codeReal:",self.resJson['code'],type(self.resJson['code']))
            print("codeExp:",self.codeExp,type(self.codeExp))
            self.assertEqual(self.resJson['code'], str(int(self.codeExp)))
            self.assertEqual(self.resJson['message'], self.msgExp)
            # self.assertEqual(email, self.email)

        elif self.result == '1':
            self.assertEqual(self.resJson['code'], self.codeExp)
            self.assertEqual(self.resJson['message'], self.msgExp)

        else:
            print('result:',self.result)


if __name__ == '__main__':
    unittest.main()
