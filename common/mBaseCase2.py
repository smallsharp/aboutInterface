import os
import unittest
import mParser
from common import mUtils
from common.mLog import MyLog
from common.mRequests import MyRequests
import requests
import urllib3

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyBaseCase(unittest.TestCase):
    """
    接收并处理数据，给子类调用
    """


    pass