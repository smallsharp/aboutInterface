import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
iniPath = os.path.join(proDir, "config.ini")


class ReadConfig:

    def __init__(self):
        fd = open(iniPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(iniPath, "w")
            file.write(data)
            file.close()
        fd.close()

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


if __name__ == '__main__':

    print(proDir)
    read = ReadConfig()
    print(read.get_email('mail_host'))