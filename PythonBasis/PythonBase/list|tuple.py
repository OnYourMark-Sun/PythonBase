#list 列表

listt = [1,2,3,5,6,5]
print(len(listt))# 获取listt的长度
print(listt[4]) # 不可以越界 可以是负数 倒着数
listt.pop(2) #删除第几个元素，没有值 默认删除最后一个
print(listt)

list2 = ['s','s','gg',['ee','er','ewe',['tt',]]]
print(list2[3][3])


#tuple 元组 有序列表   不可改变没有append   insert
classmates = ('mical','bob','tracty')
classma = (1,)# 定义一个元素是后边加，