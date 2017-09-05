#dict


#set

def setmothods():
    s = [1, 9, 3, 3, 4, 2, 1, 6, 7, 8]
    t = [1, 4, 67, 9, 5, 3]
    ss = set(s)  # 消除重复并排序
    print(ss)
    print(set(t).remove(67))
    # print(set(s)-set(t))#相当于集合运算 s中减去包含t的，s+t 合并


    ss = set(['aa', 'b', 'cc', 'sd'])
    tt = set(['v', 'f', 's', 'aa', 'b'])

    print(ss & tt)
    print(ss | tt)  # 全部出现过的的字母

def set2methods():
    a = ['c','f','s','b']
    a.sort() #排序
    print(a)

    ss = 'avbsd'
    st = ss.replace('a','AA') # 创建一个新的字符串
    print(st) #取代字符串


set2methods()

