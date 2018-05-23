# coding=utf-8
import xlrd
import os



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class MyExcel():

    def __init__(self, excel, sheetName):

        self.excel = excel
        self.sheetName = sheetName

        try:
            self.workbook = xlrd.open_workbook(self.excel)
            self.sheet = self.workbook.sheet_by_name(self.sheetName)
        except Exception:
            print("请检查Excel文件是否存在，文件格式是否正确,提供的路径：", self.excel)

    # 获取所有用例信息，每一行为一个用例
    def getAllSteps(self):
        rows = self.sheet.nrows  # 获取sheet的行数
        cases = []
        for r in range(rows):
            if r == 0: continue  # 去掉第一行标题
            case = self.sheet.row_values(r)  # 获取该行的内容[]
            cases.append(case)
        return cases


if __name__ == '__main__':
    excel = MyExcel(PATH('../testFile/my.xls'),'yunche')

    print(excel.getAllSteps())