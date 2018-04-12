import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
iniPath = os.path.join(proDir, "config.ini")

class ReadConfig:

    def __init__(self):
        fd = open(iniPath)
        self.parser = configparser.ConfigParser()
        self.parser.read(iniPath)

    def get_email(self, name):
        value = self.parser.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.parser.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.parser.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.parser.set("HEADERS", name, value)
        with open(iniPath, 'w+') as f:
            self.parser.write(f)

    def get_url(self, name):
        value = self.parser.get("URL", name)
        return value

    def get_db(self, name):
        value = self.parser.get("DATABASE", name)
        return value

class MyIniParser:

    def __init__(self,iniFilePath):

        with open(iniFilePath,'r'):
            self.parser = configparser.ConfigParser()
            self.parser.read(iniFilePath)

    def getItem(self,section,key):
        return self.parser.get(section,key)


if __name__ == '__main__':
    project_dir = os.path.dirname(os.path.abspath(__file__))
    print(project_dir)

    p = MyIniParser('config.ini')
    print(p.getItem('EMAIL', 'mail_host'))