import hashlib
#摘要算法应用
md5 = hashlib.md5()
md5.update('how to user md5 inpython'.encode('utf-8'))
print(md5.hexdigest())