from collections import namedtuple,deque,defaultdict,Counter
def nametuplee():
    point = namedtuple("point", ['x', 'y'])
    p = point(1, 2)
    print(p.x, p.y)

    # 定义一个圆 想，y r
    round = namedtuple('Round', ['x', 'y', 'r'])
    r = round(2, 3, 3.14159)
    print(r.x, r.y, r.r)


#双端队列  两边进行操作
def dequee():
    d = deque(['a','b','s','d','d'])
    print(d)
    d.append('yy')
    d.appendleft('aaa')
    print(d)

    d.pop()
    d.popleft()
    print(d)



def defaultdictt(): #没有键 返回默认值
    dd = defaultdict(lambda :'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'],'----',dd['kk'])

defaultdictt()

#遍历有序的dict：orderdict



#Counter  统计次数
c = Counter()
for ch in 'cjsjslkjajfkldjfafpoewowo我的等待你的点点滴滴':
    c[ch] = c[ch] +1
print(c)