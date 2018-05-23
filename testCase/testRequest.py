import os
import json
import requests
import re
from common.mExcel import MyExcel

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test():

    def __init__(self):
        self.steps = MyExcel(PATH('../testFile/my.xls'), 'yunche').getAllSteps()

    def run(self):
        for step in self.steps:
            print(step)
            case, method, url, params, type, code, msg = step
            if type == 'W' and method == 'post':
                print('url:',url)
                print('params:',params)
                # requests.adapters.DEFAULT_RETRIES = 5
                headers = {'Content-Type':'application/x-www-form-urlencoded; charset=utf-8'}
                res = requests.post(url, json=params)
                print(res.text)
                # resJson = json.loads(res.text)
                # token = resJson['retData']['token']
                # uid = resJson['retData']['uid']
                # return token, uid
            elif method=='get':
                print('get')
                print(self.extract_variables(params))

                # requests.get(url,params)
                print('else')
        print('over')

    # 从内容中提取所有变量名, 变量格式为$variable,返回变量名list
    def extract_variables(self, content):
        variable_regexp = r"\$([\w_]+)"
        if not isinstance(content, str):
            content = str(content)
        try:
            return re.findall(variable_regexp, content)
        except TypeError:
            return []

    # 替换内容中的变量, 返回字符串型
    def replace_var(self, content, var_name, var_value):
        if not isinstance(content, str):
            content = json.dumps(content)
        var_name = "$" + var_name
        content = content.replace(str(var_name), str(var_value))
        return content

    def login(self):
        url = 'https://api.yunchehome.com/app/user/login'
        params = {"mobile": 18521035133, "password": "96e79218965eb72c92a549dd5a330112"}
        res = requests.post(url, json=params)
        print(res.text)
        resJson = json.loads(res.text)
        token = resJson['retData']['token']
        uid = resJson['retData']['uid']
        return token, uid





if __name__ == '__main__':
    test = Test()

    test.run()
    # test.request()
