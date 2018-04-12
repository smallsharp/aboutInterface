import unittest
import paramunittest
import mParser
from common import Log as Log
from common import utils
from common import mHttp as ConfigHttp

login_xls = utils.get_xls("userCase.xlsx", "login")
config = mParser.ReadConfig()
configHttp = ConfigHttp.MyHttp()
info = {}


@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):

    def setParameters(self, case_name, method, token, email, password, result, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param email:
        :param password:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.email = str(email)
        self.password = str(password)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.return_json = None
        self.info = None

    def description(self):
        self.case_name

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name + "测试开始前准备")

    def testLogin(self):

        # set url
        # self.url = utils.get_url_from_xml('login')
        # configHttp.set_url(self.url)
        self.url = '/memberSite/sso/loginJson'
        print("第一步：设置url  " + self.url)

        # get visitor token
        if self.token == '0':
            token = config.get_headers("token_v")
        elif self.token == '1':
            token = None

        # set headers
        header = {"token": str(token)}
        configHttp.set_headers(header)
        print("第二步：设置header(token等)")

        # set params
        data = {"email": self.email, "password": self.password}
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")

        # test interface
        self.return_json = configHttp.post()
        method = str(self.return_json.request)[
                 int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法：" + method)

        # check result
        self.checkResult()
        print("第五步：检查结果")

    def tearDown(self):
        info = self.info
        if info['code'] == 0:
            # get uer token
            token_u = utils.get_value(info, 'member', 'token')
            # set user token to config file
            config.set_headers("TOKEN_U", token_u)
        else:
            pass
        self.log.build_case_line(self.case_name, self.info['code'], self.info['msg'])
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        print('第五步：check result')
        # print(self.return_json)
        print('result:',self.result)
        # self.info = self.return_json.json()
        # show return message
        utils.show_return_msg(self.return_json)

        if self.result == '0':
            email = utils.get_value(self.info, 'member', 'email')
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)
            self.assertEqual(email, self.email)

        elif self.result == '1':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)

        else:
            print('result:',self.result)


if __name__ == '__main__':
    unittest.main()
