from function import function2

#if

def ifmethods():
    na = input('name')
    if int(na) < 2000:  # 输入是str类型 需要做一个类型转换   str()   float() ,,,
        print('数字太小啦')
    else:
        print('haode', na)

#ifmethods()


#for

def forMedthods():
    m = 0
    for n in list(range(5)):
        m = m+n
    print(m)
    n = 0
    while n<10:
        m +=n
        n+=1
    print('m:',m)

#forMedthods()

'''break :结束循环
continue: 跳到下一次循环'''


# 调用函数

