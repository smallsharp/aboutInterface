import os
import unittest
import mParser
from common import mUtils
from common.mLog import MyLog
from common.mRequests import MyRequests
import requests
import urllib3

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyBaseCase(unittest.TestCase):
    """
    接收并处理数据，给子类调用
    """
    print('MyBaseCase in')

    mRequest = MyRequests()  # request instance
    logger = MyLog.getLog().getLogger()

    def __init__(self, methodName='runTest', dconfig=None):
        super(MyBaseCase, self).__init__(methodName)
        self.hasSession = False

    # 1 接受请求参数，进行处理，使用参数化时，这个方法必须写
    def setParameters(self, *data):
        print("origin data:", data)
        # self.case, self.method, self.url,*args, self.headers,self.cookies,self.codeExp, self.msgExp = data
        # # self.params = None
        # self.checkedArgs = self.checkNum(args)
        self.case, self.method, self.url, self.headers, self.params, self.codeExp, self.msgExp = data

    def initSession(self):

        if not self.hasSession:
            print('init session ~')

            login_url = "https://m.taidu.com/memberSite/sso/loginJson"
            login_params = {'loginAccount': '18521035133', 'password': '111111', 'code': '', 'rememberMe': '1',
                            'clientType': 'H5', 'abbr': 'CN', 'clientVersion': '',
                            'sign': '87823FC7334C13955C8B451B48027954'}
            session = requests.Session()
            urllib3.disable_warnings()
            session.get(url=login_url, params=login_params, verify=False)  # verify=False 关闭证书验证，但是仍然会报出证书警告
            self.hasSession = True
        return session

    def init(self):
        data = None
        self.case, self.method, self.url, *args, self.headers, self.cookies, self.codeExp, self.msgExp = data
        # self.params = None
        self.checkedArgs = self.checkNum(args)

    # 2
    def setUp(self):
        print("{} is running".format(self.case))

    def getParams(self, xlsPath, sheetName):
        self.params = self.zipParams(self.getParamsTitle(xlsPath, sheetName), self.getParamsValue())

    def getSheets(self):
        return ['login', 'categoryProductList']

    def getParamsTitle(self, xlsxName, sheetName):
        """
        :param xlsxName: xlsx file name
        :param sheetName: sheet name
        :return: params(not common params,like method,code) like loginAccount,password etc...
        """
        titles = mUtils.get_xls_title(xlsxName, sheetName)
        paramsTitle = []
        for t in titles:
            if t not in ('case', 'method', 'url', 'headers', 'cookies', 'code', 'msg'):
                paramsTitle.append(t)
        return paramsTitle

    def getParamsValue(self):
        return self.checkedArgs

    def checkNum(self, numTurple):
        new = list()
        for num in numTurple:
            if isinstance(num, float):
                num = int(num)
            new.append(num)
        return tuple(new)

    def zipParams(self, paramsTitle, paramsValue):
        """
        zip(paramsTitle,paramsValue)
        :param paramsTitle: request title
        :param paramsValue: title ==> value
        :return: {'title': value}
        """
        paramDict = dict()
        for k, v in zip(paramsTitle, paramsValue):
            paramDict[k] = v
        return paramDict

    # 4
    def tearDown(self):
        # print("{} is over ".format(self.case))
        pass

    def checkResult(self, result=None):
        print('result:', result)
        if result:
            import json
            result = json.loads(result)
            self.assertEqual(result['code'], str(int(self.codeExp)))
            self.assertEqual(result['message'], self.msgExp)
            print("success")
