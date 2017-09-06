'''切片slice'''
L = ['xsy','sxm','xtt','ss','ssd','ttgs','fagf','agag','agag','ayjj']

def slicex(n):
    ll = []
    for i in range(n):
        ll.append(L[i])

    print(ll)

slicex(2)

def slicexx(n):
    ll = L[0:n]
    print('Slice:',ll)
#slicexx(3) # 获取前边的三个

def slicexxx():
    print('获取后边的两个', L[-2:])  # 获取后边的两个
    print('前边8个数，每3个获取一个', L[:8:3])
    print('全部的数，每5个获取一个', L[::5])
    print('复制一个L', L[:])

    # tuple 元组也是一种list 也可以做切片 知识操作后的结果仍然是元组
    tp = (1, 3, 5, 6, 7, 8, 9, 0, 9)
    print(tp[:5])

    # 字符串''我是一个字符串'也可以看成一个list进行切片

    st = '我是一个字符串'
    print(st[:6:3])

"""迭代 Iterration"""
def iteration():
    for i,value in enumerate(L):
        print(i,value)

#iteration()


"""列表生成式"""
def Listss():
    li = list(range(1, 12))
    print(li)

    print([m + n for m in 'abcd' for n in '1234'])  # a1 a2 a3 a4  b1 b2 b3 ...

    d = {'a': 'xst', 'x': 'ser'}
    for x, y in d.items():
        print(x, y)  # 遍历key：value

    d_list = [x + ':' + y for x, y in d.items()]  # ['a:xst', 'x:ser']
    print(d_list)

    max_min = ['XSY', 'WOMEN D ', 'YIBKF']
    print([ma.lower() for ma in max_min])


"""生成器  二者区别 g列表全部创建，gg会根据使用情况创建满足需求个数的值  

     g 可以直接全部打印，，
     gg 使用next（gg） 一次智能打印一个"""
def generators():
    g = [n for n in range(10)]
    gg = (n for n in range(10))
    print(g, '_____', next(gg))
    print(next(gg))

    # 正确的迭代 generator
    for n in gg:
        print(n)

"""迭代器"""
from  collections import Iterator

print(isinstance(88,Iterator))