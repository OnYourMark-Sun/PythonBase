#操作迭代对象
import itertools
#natuals = itertools.count(1) #无限制的输出 自然数字
#natuals = itertools.cycle('ABC')#无限输出abcabc....
natuals = itertools.repeat('abcd',7)
for n in natuals:
    print(n)


#chain 把迭代数组 串联起来

for c in itertools.chain('abc','xyz'):
    print(c)

#迭代器中相邻的重复元素跳出来 放在一个数组中
for key,group in itertools.groupby('aaaajddddfjjjjdddkkkklannnn'):
    print(key,list(group))