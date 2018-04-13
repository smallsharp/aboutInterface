
import os
import mParser

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
iniParser = mParser.MyIniParser(PATH('../../interface.ini'))
# iniParser = mParser.MyIniParser(PATH('interface.ini'))

print(os.path.dirname(__file__))
print(PATH('../../interface.ini'))


print(iniParser.getItem('memberSite','login'))