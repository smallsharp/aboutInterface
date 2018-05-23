import os
import configparser

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
# config.ini文件路径
configIni = PATH('config.ini')

# interface.ini文件路径
interfaceIni = PATH('interface.ini')


class MyIniParser:
    """
    解析.ini 文件
    """

    def __init__(self, filePath):
        with open(filePath, 'r'):
            self.parser = configparser.ConfigParser()
            self.parser.read(filePath)


    def getItem(self,section,key):
        return self.parser.get(section,key)


if __name__ == '__main__':

    p = MyIniParser(PATH('config.ini'))
    v = p.getItem('EMAIL', 'mail_host')
    print(v)