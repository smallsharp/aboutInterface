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
        self.on_off = mParser.MyIniParser(mParser.configIni).getItem('EMAIL', 'on_off')# send mail==>yes or no
        self.email = MyEmail.get_email()

    def initTestSuite(self):
        suite = unittest.defaultTestLoader.discover(os.path.join(PATH('testCase')), pattern='test*' + '.py', top_level_dir=None)
        return suite

    def run(self):
        suite = self.initTestSuite()
        if suite is not None:
            self.logger.info("Test Start")
            with open(self.reportPath, 'wb') as file:
                runner = HTMLTestReportCN.HTMLTestRunner(stream=file, title='Test Report',
                                                         description='interface test')
                runner.run(suite)
        else:
            self.logger.info("Have no case to test.")
        if self.on_off == 'on':
            self.logger.info("sending email..")
            # self.email.send_email()
        self.logger.info("Test End")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()
