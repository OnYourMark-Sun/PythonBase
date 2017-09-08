"""Input  Output"""
#文件读取
'''class text_txt1():
    def tex(self):
      with open('text.txt') as f:
        for line in f.readlines():
            print(line.strip())

    def write(self):
        with open('text.txt','w') as f:
            f.write('xsuxsssxsxsxsx')

# ff = text_txt1()
# ff.tex()
# ff.write()

#内存读取
class strngio():
    from io import StringIO
    f = StringIO('fsafa!\nffe!\nsef')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s)'''


"""二进制 处理"""

'''from  io import BytesIO
f = BytesIO
f.write('中国那我呢'.encode('utf-8'))
print(f.getvalue())'''

"""操作文件 以及类型"""
import os
'''def base():
    os.name
    print(os.name)
    print(os.uname())
# base()

def wenjianq():
    print('当前文件绝对路径：',os.path.abspath('.'))
    print('在某个目录下创建新目录：',os.path.join('/Users/yurong/Documents/GitHub/PythonBase/PythonBasis/PythonBase','xsy'))
    try:
       os.rename('text.txt', 'teeet.txt')
# wenjianq()'''


print('序列化：把变量从内存中变成可存储或者传输的过程称之为序列化')

'''import  pickle
# d = dict(name = 'bao',age = 23,score = 98)
# # print(pickle.dumps(d))
# f = open('teeet.txt','wb')
# pickle.dump(d,f)
# print(d)

f = open('teeet.txt','rb')
d = pickle.load(f)
f.close()
print(d)'''

"""python 转 JSON"""
import pickle
import json
'''d = dict(name ='xswxm',age = 23,person = 'kakakeke')
dd = json.dumps(d)
print(dd)
f = open('teeet.txt','rb')
pickle.dump(dd,f)
f.close()'''

class student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age


def student2(student):
    return {
        'name' : student.name,
        'age' : student.age
    }
ss = student('xssxsxs',233)
print(json.dumps(ss,default=student2))


