import os
import logging
from datetime import datetime
import threading

# https://segmentfault.com/a/1190000007581128


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class Log:

    def __init__(self):
        self.reportDir = os.path.join(PATH('../report')) # 测试报告的目录
        if not os.path.exists(self.reportDir):
            os.mkdir(self.reportDir)

        # 日志文件的目录
        # self.logDir = os.path.join(self.reportDir, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        self.logDir = os.path.join(self.reportDir, str(datetime.now().strftime("%Y%m%d")))
        if not os.path.exists(self.logDir):
            os.mkdir(self.logDir)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG) # 将日志的输出级别调整为DEBUG
        handler = logging.FileHandler(os.path.join(self.logDir, "report.log"))

        # 设置日志的打印格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def getLogger(self):
        return self.logger

    def build_start_line(self, case_no):
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)

    def get_report_path(self):
        return os.path.join(self.logDir, "report.html")

    def get_report_dir(self):
        return self.logDir

    def write_result(self, result):
        result_path = os.path.join(self.logDir, "report.txt")
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
    def getLog():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log() # new log instance
            MyLog.mutex.release()
        return MyLog.log

if __name__ == "__main__":
    log = MyLog.getLog()
    logger = log.getLogger()
    logger.debug("test debug")
    logger.info("test info")
    print('ok')

