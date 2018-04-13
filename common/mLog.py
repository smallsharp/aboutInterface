import os
import mParser
import logging
from datetime import datetime
import threading

# https://segmentfault.com/a/1190000007581128


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class Log:

    def __init__(self):
        global logPath, resultPath, proDir
        # resultPath = os.path.join(proDir, "result")
        resultPath = os.path.join(PATH('../result'))
        # 如果没有result目录，测创建一个
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()
        # 将日志的输出级别调整为DEBUG
        self.logger.setLevel(logging.DEBUG)

        # defined handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # 输出格式 如：2018-04-12 16:32:56,934 - root - INFO - test info
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)

    def get_report_path(self):
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_result_path(self):
        return logPath

    def write_result(self, result):
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            logger.error(str(ex))


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")
    print('ok')

