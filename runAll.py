#encoding=utf-8
import os
import unittest
from common.Log import MyLog as Log
import mParseIni
# import HTMLTestRunner
from common import HTMLTestReportCN
from common.configEmail import MyEmail

localReadConfig = mParseIni.ReadConfig()


class AllTest:
    def __init__(self):
        global log, logger, resultPath, on_off
        log = Log.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_path()
        on_off = localReadConfig.get_email("on_off")
        self.caseListFile = os.path.join(mParseIni.proDir, "caselist.txt") # D:\workspace\PythonStation\interfaceTest\caselist.txt
        self.caseFile = os.path.join(mParseIni.proDir, "testCase") # D:\workspace\PythonStation\interfaceTest\testCase
        # self.caseFile = None
        self.caseList = [] # ['user/testLogin', 'user/testRegister']
        self.email = MyEmail.get_email()

    def set_case_list(self):
        """
        set case list
        :return:
        """
        print("self.caseListFile:",self.caseListFile)
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            # print("data:",data)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        print("第一步：准备testSuite")
        self.set_case_list()
        test_suite = unittest.TestSuite()

        suite_module = []
        print("self.caseList:%s" % self.caseList) # ['user/testLogin', 'user/testRegister']
        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name + ".py")
            print("self.caseFile:",self.caseFile)
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            # print('discover:',discover)
            suite_module.append(discover)
        # print("suite_module:",suite_module)

        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                    print("tests_name",test_name)
                    test_suite.addTest(test_name)
        else:
            return None

        print("test_suite:",test_suite)
        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suite = self.set_case_suite()
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
