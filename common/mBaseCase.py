import os
import unittest
import mParser
from common import utils
from common import mLog
from common import mHttp

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyBaseCase(unittest.TestCase):
    mhttp = mHttp.MyHttp()
    log = mLog.MyLog.get_log()
    logger = log.get_logger()
    iniParser = mParser.MyIniParser(PATH('../interface.ini'))

    # 1
    def setParameters(self, *params):
        print('DATA:', params)
        self.case_name, self.method, *args, self.result, self.codeExp, self.msgExp = params
        self.reqParams = self.checkNum(args)

    # 2
    def setUp(self):
        print("{} is running".format(self.case_name))

    def getParamsTitle(self, xlsxName, sheetName):
        """
        :param xlsxName: xlsx file name
        :param sheetName: sheet name
        :return: params(not common params,like method,code) like loginAccount,password etc...
        """
        titles = utils.get_xls_title(xlsxName, sheetName)
        paramsTitle = []
        for t in titles:
            if t not in ('case_name', 'method', 'result', 'code', 'msg'):
                paramsTitle.append(t)
        return paramsTitle

    def checkNum(self, numTurple):
        new = list()
        for num in numTurple:
            if num == int(num):
                num = int(num)
            new.append(num)
        return tuple(new)

    def getParamsValue(self):
        return self.reqParams

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
        print("{}测试结束".format(self.case_name))

    def checkResult(self):
        self.resJson = self.res.json()
        if self.result == '0':
            self.assertEqual(self.resJson['code'], str(int(self.codeExp)))
            self.assertEqual(self.resJson['message'], self.msgExp)
            # self.assertEqual(email, self.email)
        elif self.result == '1':
            self.assertEqual(self.resJson['code'], self.codeExp)
            self.assertEqual(self.resJson['message'], self.msgExp)
        else:
            print('result:', self.result)
        print('result of {} is {}'.format(self.case_name, self.result))
