import pandas as pd
import os
from xlrd import open_workbook


data = pd.read_excel('../testFile/userCase.xls')

# print(data.head())

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def get_xls_title(xlsPath, sheet_name):
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    return sheet.row_values(0)

# 获取所有用例信息，每一行为一个用例

def get_all_steps(xlsPath,sheetName):
    excel = open_workbook(xlsPath)
    sheet = excel.sheet_by_name(sheetName)
    rows = sheet.nrows  # 获取sheet的行数
    cases = []
    for r in range(rows):
        if r == 0: continue  # 去掉第一行标题
        case = sheet.row_values(r)  # 获取该行的内容[]
        cases.append(case)
    return cases


# print(get_xls_title(PATH('../testFile/userCase.xls'), 'index'))
# print(get_all_steps(PATH('../testFile/userCase.xls'), 'index'))

for step in get_all_steps(PATH('../testFile/userCase.xls'), 'index'):
    print(step[0],step[1])
