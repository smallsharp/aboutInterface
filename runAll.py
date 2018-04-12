# encoding=utf-8
import os
import unittest
from common.Log import MyLog as Log
import mParseIni
from common import HTMLTestReportCN
from common.configEmail import MyEmail

iniParser = mParseIni.ReadConfig()

class AllTest:

    def __init__(self):
        global log, logger, resultPath, on_off
        log = Log.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_path()
        on_off = iniParser.get_email("on_off")
        # D:\workspace\PythonStation\interfaceTest\caselist.txt
        self.caseFile = os.path.join(mParseIni.proDir,"caselist.txt")
        self.caseList = self.getCaseList()  # ['user/testLogin', 'user/testRegister']
        self.caseDir = os.path.join(mParseIni.proDir, "testCase")  # D:\workspace\PythonStation\interfaceTest\testCase
        self.email = MyEmail.get_email()

    def getCaseList(self):
        caseList = []
        with open(self.caseFile, 'r') as f:
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
            print(caseName + ".py")
            discover = unittest.defaultTestLoader.discover(self.caseDir, pattern=caseName + '.py', top_level_dir=None)
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for testName in suite:
                    print("testName:", testName)
                    testsuite.addTest(testName)
        else:
            return None

        print("test_suite:", testsuite)
        return testsuite

    def run(self):
        try:
            suite = self.getTestSuite()
            if suite is not None:
                logger.info("********TEST START********")
                fp = open(resultPath, 'wb')
                runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suite)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            fp.close()
            # send test report by email
            if on_off == 'on':
                logger.info("sending email..")
                pass
                # self.email.send_email()
            elif on_off == 'off':
                logger.info("Doesn't send report email to developer.")
            else:
                logger.info("Unknow state.")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()
