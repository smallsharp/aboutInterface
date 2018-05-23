import hashlib



str = '111111'


h1 = hashlib.md5()
h1.update(str.encode(encoding='utf-8'))

print(str)
print(h1.hexdigest())




# 生成MD5
def genearteMD5(str):
    # 创建md5对象
    hl = hashlib.md5()

    # Tips
    # 此处必须声明encode
    # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
    hl.update(str.encode(encoding='utf-8'))

    print('MD5加密前为 ：' + str)
    print('MD5加密后为 ：' + hl.hexdigest())


genearteMD5('111111')