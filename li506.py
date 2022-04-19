# Queue 线程安全队列
# 在线程中，访问一些全局变量，加锁是一个经常的过程。如果你是想把一些数据存储到某个队列中，
# 那么 Python 内置了一个线程安全的模块叫做 queue 模块。 Python 中的 queue 模块中提供了同步的、线程安全的队列类，
# 包括 FIFO（先进先出）队列 Queue , LIFO（后入先出）队列 LifoQueue 。
# 这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么都做完），能
# 够在多线程中直接使用。可以使用队列来实现线程间的同步。相关的函数如下：
# 初始化 Queue(maxsize)：创建一个先进先出的队列。
# 1.qsize()：返回队列的大小。
# 2.empty()：判断队列是否为空。
# 3.full()：判断队列是否满了。
# 4.get()：从队列中取最后一个数据。
# 5.put()：将一个数据放到队列中。

import random
from queue import Queue
import time
import threading
# q=Queue(4)
# for x in range(5):
#     try:
#         q.put(x,block=False) #非阻塞
#     except:
#         break
    
# # print(q.qsize())

# if q.full:
#     print('full')

# for x in range(5):
#     try:
#         value=q.get(block=False) #非阻塞
#         print(value)
#     except:
#         break

# if q.empty:
#     print('empty')

# print('complete')

def add_value(q):
    while True:
        q.put(random.randint(0,10))
        time.sleep(1)

def get_value(q):
    while True:
        print('获取到的值:%d'%q.get())

def main():
    q=Queue(10)
    th1=threading.Thread(target=add_value,args=[q])
    th2=threading.Thread(target=get_value,args=[q])

    th1.start()
    th2.start()

if __name__=='__main__':
    main()