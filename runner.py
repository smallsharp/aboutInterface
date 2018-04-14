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

        log = MyLog.get_log()
        self.logger = MyLog.get_log().get_logger()
        self.reportPath = log.get_report_path()  # D:\workspace\mInterface\result\20180414213218\report.html
        self.on_off = mParser.MyIniParser(mParser.configIni).getItem('EMAIL', 'on_off')
        # D:\workspace\python\mInterface\caselist.txt
        self.caseList = self.getCaseList(os.path.join(PATH('caselist.txt')))  # ['user/testLogin2', 'user/testRegister']
        self.caseDir = os.path.join(PATH('testCase'))  # D:\workspace\PythonStation\interfaceTest\testCase
        self.email = MyEmail.get_email()

    def getCaseList(self, filePath):
        caseList = []
        with open(filePath, 'r') as f:
            for value in f.readlines():
                data = str(value)
                if data != '' and not data.startswith('#'):
                    caseList.append(data.replace('\n', ''))
        return caseList

    def getTestSuite(self):
        testsuite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            caseName = case.split("/")[-1]
            discover = unittest.defaultTestLoader.discover(self.caseDir, pattern=caseName + '.py', top_level_dir=None)
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for testName in suite:
                    testsuite.addTest(testName)
        else:
            return None
        return testsuite

    def run(self):
        print('run')
        suite = self.getTestSuite()
        if suite is not None:
            self.logger.info("********TEST START********")
            with open(self.reportPath, 'wb') as oFile:
                runner = HTMLTestReportCN.HTMLTestRunner(stream=oFile, title='Test Report',
                                                         description='Test Description')
                runner.run(suite)
        else:
            self.logger.info("Have no case to test.")
        # send report email
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
