import requests
import mParser
import os
from xlrd import open_workbook
from xml.etree import ElementTree
from common.mRequests import MyRequests
from common.mLog import MyLog as Log
import json

mhttp = MyRequests()
log = Log.getLog()
logger = log.getLogger()
caseNo = 0

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def show_return_msg(response):
    """
    show msg detail
    :param response:
    :return:
    """
    url = response.url
    msg = response.text
    print("\n请求地址："+url)
    # 可以显示中文
    print("\n请求返回值："+'\n'+json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))
# ****************************** read testCase excel ********************************


def getLines(xls_name: object, sheet_name: object) -> object:
    lines = []
    # get xls file's path
    xlsPath = os.path.join(PATH("../testFile"), xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case':
            lines.append(sheet.row_values(i))
    return lines

def get_xls_title(xls_name, sheet_name):
    # get xls file's path
    xlsPath = os.path.join(PATH("../testFile"), xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    return sheet.row_values(0)

# ****************************** read SQL xml ********************************
database = {}
def set_xml():
    """
    set sql xml
    :return:
    """
    if len(database) == 0:
        sql_path = os.path.join(PATH('../testFile/SQL.xml'))
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table


def get_xml_dict(database_name, table_name):
    """
    get db dict by given name
    :param database_name:
    :param table_name:
    :return:
    """
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict


def get_sql(database_name, table_name, sql_id):
    """
    get sql by given name and sql_id
    :param database_name:
    :param table_name:
    :param sql_id:
    :return:
    """
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql


if __name__ == "__main__":
    print(getLines("userCase.xlsx", "login"))
    # set_visitor_token_to_config()
