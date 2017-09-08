print("线程Thread-进程Process")

'''from multiprocessing import Process
import os

def run_proce(name):
    print(name,os.getpid())
if __name__ == '__main__':
    print(os.getpid())
    p = Process(target=run_proce,args=('text',))
    print('child star')
    p.start()
    p.join()
    print('child process end')
'''

"""进程间的通信"""
from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print(os.getpid())
    for value in ['a','b','c']:
        print(value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    print(os.getpid())
    while True:
        value = q.get(True)
        print(value)
