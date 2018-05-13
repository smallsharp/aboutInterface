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
        # self.protocol = self.iniParser.getItem('HTTP', 'protocol')  # 协议
        # self.host = self.iniParser.getItem('HTTP', 'host')  # 域名
        # self.port = self.iniParser.getItem('HTTP', 'port')  # 端口
        self.url = None  # 请求地址
        self.method = 'get'
        self.headers = None  # 头信息
        self.params = None  # 请求参数
        self.data = None  # 请求参数
        self.cookies = None
        self.files = None
        self.state = 0
        self.timeout = self.iniParser.getItem('HTTP', 'timeout')  # 超时时间

    def setRequest(self, url, params, method='get', data=None, json=None, headers=None, cookies=None):
        # self.url = '{}://{}{}'.format(self.protocol, self.host, uri)
        self.url = url
        self.params = params  # get
        self.data = data # post
        self.json = json # post
        self.method = method
        self.headers = headers
        self.cookies = cookies

    def set_headers(self, header):
        self.headers = header


    def send(self):
        if self.method == 'get':
            return self.get(self.url, self.params, headers=self.headers, cookies=self.cookies,
                            timeout=float(self.timeout))
        elif self.method == 'post':
            return self.post(self.url, self.data,json=self.json,headers=self.headers, cookies=self.cookies,
                            timeout=float(self.timeout))
        else:
            raise Exception('unknown method {}'.format(self.method))

    def get(self, url, params=None, **kwargs):
        """
        get请求
        :param url:
        :param params:
        :param kwargs:
        :return:
        """
        return requests.get(url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        """
        :param url:
        :param data:
        :param json:
        :param kwargs:
        :return:
        """
        return requests.post(url, data=data, json=json, **kwargs)

    def set_files(self, filename):
        if filename != '':
            file_path = 'F:/AppTest/Test/interfaceTest/testFile/img/' + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    def postWithFile(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(self.timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def request(self, method, url,
                params=None, data=None, headers=None, cookies=None, files=None,
                auth=None, timeout=None, allow_redirects=True, proxies=None,
                hooks=None, stream=None, verify=None, cert=None, json=None):
        """Constructs a :class:`Request <Request>`, prepares it and sends it.
        Returns :class:`Response <Response>` object.

        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, bytes, or file-like object to send
            in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the
            :class:`Request`.
        :param files: (optional) Dictionary of ``'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to ``False``.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response
        """


if __name__ == "__main__":
    m = MyRequests()

    url = 'https://m.taidu.com/goodsSite/home/categoryProductList'
    params = {'abbr': 'CN', 'clientType': 'H5', 'clientVersion': ''}
    # res = m.get("https://m.taidu.com/goodsSite/home/categoryProductList?abbr=CN&clientType=H5&clientVersion=")
    res = m.get(url, params, timeout=0.5)
    print(res.text)
