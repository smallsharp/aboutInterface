# encoding=utf-8
import os
import unittest
import mParser
from common.mLog import MyLog
from common.mEmail import MyEmail
from common import HTMLTestReportCN

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AllTest:

    def __init__(self):
        log = MyLog.getLog()
        self.logger = MyLog.getLog().getLogger()
        self.reportPath = log.get_report_path()  # D:\workspace\mInterface\result\20180414213218\report.html
        self.on_off = mParser.MyIniParser(mParser.configIni).getItem('EMAIL', 'on_off')
        self.caseList = self.initCaseList(os.path.join(PATH('caselist.txt')))  # ['user/testLogin2', 'user/testRegister']
        print('caseList:',self.caseList)
        self.email = MyEmail.get_email()

    def initCaseList(self, filePath):
        caseList = []
        with open(filePath, 'r') as f:
            for value in f.readlines():
                data = str(value)
                if data != '' and not data.startswith('#'):
                    caseList.append(data.replace('\n', ''))
        return caseList

    def initTestSuite(self):
        for case in self.caseList:
            caseName = case.split("/")[-1]
            print('caseName:',caseName)
            suite = unittest.defaultTestLoader.discover(os.path.join(PATH('testCase')), pattern=caseName + '.py', top_level_dir=None)
        return suite

    def run(self):
        print('run')
        suite = self.initTestSuite()
        print('suite:',suite)
        if suite is not None:
            self.logger.info("********TEST START********")
            with open(self.reportPath, 'wb') as oFile:
                runner = HTMLTestReportCN.HTMLTestRunner(stream=oFile, title='Test Report',
                                                         description='Test Description')
                runner.run(suite)
        else:
            self.logger.info("Have no case to test.")
        if self.on_off == 'on':
            self.logger.info("sending email..")
            # self.email.send_email()
        elif self.on_off == 'off':
            self.logger.info("Doesn't send report email to developer.")
        else:
            self.logger.info("Unknow state.")
        self.logger.info("*********TEST END*********")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()
