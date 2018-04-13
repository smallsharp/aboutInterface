import requests
import mParser
from common.mLog import MyLog as Log
import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
# config.ini配置文件的路径
configIni = PATH('../config.ini')

class MyHttp:

    def __init__(self):

        global scheme, host, port, timeout
        self.iniParser = mParser.MyIniParser(configIni)
        scheme = self.iniParser.getItem('HTTP','scheme')
        host = self.iniParser.getItem('HTTP','host')
        port = self.iniParser.getItem('HTTP','port')
        timeout = self.iniParser.getItem('HTTP','timeout')

        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url(self, uri):
        self.url = scheme + '://' + host + uri
        print('url:',self.url)

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, filename):
        if filename != '':
            file_path = 'F:/AppTest/Test/interfaceTest/testFile/img/' + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data,
                                     timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def postWithFile(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def postWithJson(self):
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


if __name__ == "__main__":
    print("ConfigHTTP")
    m = MyHttp()

