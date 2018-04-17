import requests
import mParser
from common.mLog import MyLog
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyRequests:
    # config.ini配置文件的路径
    iniParser = mParser.MyIniParser(PATH('../config.ini'))

    def __init__(self):

        self.logger = MyLog.getLog().getLogger()
        self.protocol = self.iniParser.getItem('HTTP', 'protocol')  # 协议
        self.host = self.iniParser.getItem('HTTP', 'host')  # 域名
        self.port = self.iniParser.getItem('HTTP', 'port')  # 端口
        self.timeout = self.iniParser.getItem('HTTP', 'timeout')  # 超时时间
        self.url = None  # 请求地址
        self.method = 'get'
        self.headers = {}  # 头信息
        self.params = {}  # 请求参数
        self.data = {}  # 请求参数
        self.files = {}
        self.state = 0

    def setAll(self, uri, params, method='get'):
        self.url = '{}://{}{}'.format(self.protocol, self.host, uri)
        self.params = params
        self.method = method

    def set_url(self, uri):
        # self.url = self.protocol + '://' + self.host + uri
        self.url = '{}://{}{}'.format(self.protocol, self.host, uri)
        print('url:', self.url)

    def set_method(self, method):
        self.method = method

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

    def send(self):
        print(self.url)
        if self.method == 'get':
            return self.get()
        elif self.method == 'post':
            return self.post()
        else:
            raise Exception('unknown method {}'.format(self.method))

    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(self.timeout))
            print(response.url)
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data,
                                     timeout=float(self.timeout))
            print(response.url)
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def postWithFile(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(self.timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def postWithJson(self):
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(self.timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


if __name__ == "__main__":
    print("ConfigHTTP")
    m = MyRequests()
