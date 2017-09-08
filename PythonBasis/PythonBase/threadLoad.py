import threading

local_school = threading.local()'''thread_school 是threadlocal的一个对象，每个thread都可以读取studen对象，
thread_school相当于全局对象，但每个属性如local_school.student都是线程但局部变量，可以任意但读写互不干扰，也不用给考虑锁的问题
但是每个线程智能读取自己独立的线程副本
 '''

def process_student():
    std = local_school.student #属性转换2次
    print('Hello',std,threading.current_thread().name)

def process_thread(name):
    local_school.student = name #属性转换1次
    process_student()

t1 = threading.Thread(target=process_thread,args=('shanxue',),name='threadAA')
t2 = threading.Thread(target=process_thread,args=('xushi',),name='threadNBB')

t1.start()
t2.start()
t1.join()
t2.join()
