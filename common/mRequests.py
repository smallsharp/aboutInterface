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
        self.cookies = None
        self.files = {}
        self.state = 0

    def setRequest(self, uri, params, method='get'):
        self.url = '{}://{}{}'.format(self.protocol, self.host, uri)
        self.params = params
        self.method = method

    def set_headers(self, header):
        self.headers = header

    def set_files(self, filename):
        if filename != '':
            file_path = 'F:/AppTest/Test/interfaceTest/testFile/img/' + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    def send(self):
        if self.method == 'get':
            return self.get(self.url,params,headers=self.headers,cookies=self.cookies,timeout=self.timeout)
        elif self.method == 'post':
            return self.post()
        else:
            raise Exception('unknown method {}'.format(self.method))

    def get(self,url, params=None, **kwargs):
        return requests.get(url, params=params, **kwargs)


    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data,
                                     timeout=float(self.timeout))
            print("request url:", response.url)
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


if __name__ == "__main__":
    m = MyRequests()

    url = 'https://m.taidu.com/goodsSite/home/categoryProductList'
    params={'abbr':'CN','clientType':'H5','clientVersion':''}
    # res = m.get("https://m.taidu.com/goodsSite/home/categoryProductList?abbr=CN&clientType=H5&clientVersion=")
    res = m.get(url,params,timeout=0.5)
    print(res.text)