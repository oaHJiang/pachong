# 多线程共享全局变量的问题
# 多线程是在一个进程中执行的，因此在进程中的全局变量所有线程都是可共享的。这就造成一个问题，因为线程执行的顺序是无序的，有可能造成数据错误。
# 为解决共享全局变量的问题，threading提供了一个Lock类
# 这个类可以在某个线程访问某个变量的时候加锁，其他线程就不能进来，直到当前线程处理完后，把锁释放了，其他线程才能进来处理
from multiprocessing import Lock
import threading

value=0
gLock=threading.Lock() #把尽量少和不耗时的代码放到锁中执行

def add_value():
    #如果在函数中修改全局变量，需要使用global关键字进行声明
    global value
    gLock.acquire() #上锁
    for x in range(1000000):
        value+=1
    gLock.release()
    print('value的值是：%d'%value)

def main():
    for x in range(2):
        th=threading.Thread(target=add_value)
        th.start()

if __name__=='__main__':
    main()
