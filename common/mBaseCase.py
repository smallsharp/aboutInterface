import os
import unittest
import mParser
from common import mUtils
from common.mLog import MyLog
from common.mRequests import MyRequests

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyBaseCase(unittest.TestCase):

    mRequest = MyRequests()  # request instance
    logger = MyLog.getLog().getLogger()
    # iniParser = mParser.MyIniParser(PATH('../interface.ini'))  # parser for interface

    # 1
    def setParameters(self, *params):
        print(params)
        self.case, self.method, self.url,*args, self.headers,self.cookies,self.codeExp, self.msgExp = params
        self.params = None
        self.cArgs = self.checkNum(args)

    def getParams(self,xlsPath,sheetName):
        self.params =  self.zipParams(self.getParamsTitle(xlsPath, sheetName), self.getParamsValue())

    def getSheets(self):
        return ['login','categoryProductList']

    # 2
    def setUp(self):
        print("{} is running".format(self.case))
        for sheetName in self.getSheets():
            self.getParams(PATH('../testFile/userCase.xls'),sheetName)

    def getParamsTitle(self, xlsxName, sheetName):
        """
        :param xlsxName: xlsx file name
        :param sheetName: sheet name
        :return: params(not common params,like method,code) like loginAccount,password etc...
        """
        titles = mUtils.get_xls_title(xlsxName, sheetName)
        paramsTitle = []
        for t in titles:
            if t not in ('case', 'method', 'url','headers','cookies', 'code', 'msg'):
                paramsTitle.append(t)
        return paramsTitle

    def checkNum(self, numTurple):
        new = list()
        for num in numTurple:
            if isinstance(num, float):
                num = int(num)
            new.append(num)
        return tuple(new)

    def getParamsValue(self):
        return self.cArgs

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
        print("{}测试结束".format(self.case))

    def checkResult(self, result=None):
        if result:
            self.assertEqual(result['code'], str(int(self.codeExp)))
            self.assertEqual(result['message'], self.msgExp)
        print('result of {} is {}'.format(self.case, self.result))
