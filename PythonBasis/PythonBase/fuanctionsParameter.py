#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000
'''Fanction Parameter函数参数'''
def fanctions(x,y):
    if x>y:
        print(x,'是最大的')
    elif x == y :
        print('x=y')
    else:print(y,'是最大的')

#fanctions(66,66)

# def fanctionParameter(x,y=8):'''y=8,当y没有复制的时候默认的值，  默认参数用于不变对象   若可变对象可以用 L= None'''
#     while x < y:
#         print('x什么时候大于y啊')
#         x +=1
#
# fanctionParameter(2)

'''不可变参数前边加* 就是可变的了'''

def person(name,age,**kw):   #当给kw传入 city= '北京' 时， **kw  会将kw  转换成 {''city':'beijng'}
    print(name,age,'kw:',kw)

#person('xsy',23,city = 'beijing')

"""Recursive递归函数"""

def recursiveFanction(num,product):
    if num == 1:
        return product
    return recursiveFanction(num-1,num * product)

print(recursiveFanction(3,4))


def oythonlist():
    L = []
    n = 1
    while n<99:
        L.append(n)
        n += 2
    print(L)
oythonlist()