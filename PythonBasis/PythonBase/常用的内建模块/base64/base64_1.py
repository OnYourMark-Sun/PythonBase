import random,base64
lis = []
def array64(num):
    for i in range(num):
        if i%3 ==0:
            y = random.random() * 10
            lis.append(str(int(y)))
        else:
            w = random.randint(97,122)
            c = chr(w)
            lis.append(str(c))

array64(64)
print(lis)

#直接base64 编码
bb =base64.b64encode(b'yurongkeijh==')
print(bb)
# jiem,ma
print(base64.b64decode(bb))
#base64多层编码

def base64Multilayer(num,string):
    string = base64.b64encode(b'xsysxm')
    print('times',num,'-----','string:',string)
    if num==0:
        return string
    else:
        num = num-1
        base64Multilayer(num,string)

base64Multilayer(5,'xsysxm')


#由于标准的base64 后出现的+和／，在URL中就不能直接作为参数 ，所以又有一种'url safe'd的base64编码
print(base64.b64decode(b'sjkdsakj'))
print(base64.urlsafe_b64encode(b'sd\s\d\s\d\edsd\df\d'))
