#coding=utf-8
"""
@Time:2018-04-1111:58
@Author:lfl5207
"""

caseList=[]

def set_case_list():
    fb = open('caselist.txt')
    for value in fb.readlines():
        data = str(value)
        print("data:", data)
        if data != '' and not data.startswith("#"):
            # caseList.append(data.replace("\n", ""))
            caseList.append(data)
    fb.close()


set_case_list()
print(caseList)