title = ['loginAccount', 'password']
value = ['18521035133', '11111']
# params = {"loginAccount": self.loginAccount, "password": self.password}


dict1 = dict()
for k, v in zip(title, value):
    print(k,v)
    dict1[k] = v

print(dict1)
