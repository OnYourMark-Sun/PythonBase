from datetime import datetime
#时间《=》时间戳的转换
# class timeconversion():
#     now = datetime.now()
#     print(now.timestamp())
#     print(type(now))
#
#     dt = datetime(1991, 1, 23, 20, 39)  # 参数构造时间
#
#     print(dt.timestamp())  # 转换为时间戳
#
#     # 时间戳 变为时间
#     print(datetime.fromtimestamp(78965465625.23))

# timeconversion()

from datetime import datetime
    # cday = datetime.strptime('2011-5-5 18:23:23','Y -m -d H:M:S')
    # print(cday)
    #时间的计算
    noo= datetime.now()
    thistime = datetime.fromtimestamp('63545646464')
    print(thistime,noo)


