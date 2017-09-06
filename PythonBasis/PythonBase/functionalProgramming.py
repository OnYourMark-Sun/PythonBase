'''from  functools import reduce
def fn(x,y):
    return x*10+y
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3}[s]

print(reduce(fn,map(char2num,'123579')))

#高阶函数 Higher-order function
def Higherorder():
    f = abs
    print(f(-55))

    """传入函数"""

def inputFunction(x, y, f):  # f参数 可以是一个函数
        return f(x) + f(y)

print(inputFunction(-123, 23, abs))

def f(x):
    return x*x

def map_reduce(L):
    return map(f,L)

l = map_reduce([1,2,2])
#print(list(l))
'''

'''from functools import reduce
def str2int(s):
    def fn(x,y):
        return x * 10 +y
    def char2num(s):
        return {'1':1,'2':2,'3':3}[s]

    return  reduce(fn,map(char2num,s))


"""filter()过滤器  filter(function,[])  方法返回true保留，flase 删除"""
def is_odd(i):
    return i%2 ==0
ii = list(filter(is_odd,[1,2,3,4,5,6,7]))
print(ii)

def notdivis(n):
    return lambda x:x%n>0

def prinmes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield  n
        it = filter(notdivis(n),it)
    print(it)




def sortedd():

    lis = [1,2,3,5,8,-98,-6,4,-34,-2]
    print(sorted(lis)) #从小到大进行排序
    print(sorted(lis,key=abs)) #绝对值进行排序
    strr = ['afdfd','bdfdd','SDFD','DFRG','DACVDCD','BDFD','bdfa']
    print(sorted(strr))
    print(sorted(strr,key=str.lower))
    print(sorted(strr,reverse=True))


#sortedd()


def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return  fs

f1,f2,f3 = count()



"""匿名函数 Lambda"""

print(list(map(lambda x:x*x,[1,2,3,4,5])))


def buile(x,y):
    return lambda:x*x +y*y

d = buile(2,3)
print(d)'''

"""装饰器"""
#t听过调用变量调用函数

def now(*x):
    print(x)
f = now
#print(f([4,5,5]),f.__name__)

"""p偏函数：代码创建新函数"""



import functools
int2 = functools.partial(int)

kw = {'base',2}
print(int('1222',**kw))