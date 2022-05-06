# 生产和消费者模式
# 生产者的线程专门用来生产一些数据，然后存放到中间变量中。消费者再从中间变量取出数据进行消费。
# 通过生产者和消费者模式可以让代码达到高内聚低耦合的目标，程序分工更加明确，线程更加方便管理
# 生产者和消费者因为要使用中间变量，中间变量经常是一些全局变量，因此需要使用锁来保证数据完整性。
import threading
import random

gMoney = 0
gLock = threading.Lock()
gTimes = 0


class Producer(threading.Thread):
    def run(self) -> None:  # ->提示函数返回None
        global gMoney
        global gTimes
        while True:
            gLock.acquire()
            if gTimes >= 10:
                gLock.release()
                break
            money = random.randint(0, 100)
            gMoney += money
            gTimes += 1
            print('%s生产了%d元钱' % (threading.current_thread().name, money))
            gLock.release()


class Consumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        while True:
            gLock.acquire()
            money = random.randint(0, 100)
            if gMoney >= money:
                gMoney -= money
                print('%s消费了%d元钱' % (threading.current_thread().name, money))
            else:
                if gTimes >= 10:
                    gLock.release()
                    break
                print('%s消费者想消费%d元钱，但余额只有%d元钱' % (threading.current_thread().name, money, gMoney))
            gLock.release()


def main():
    for x in range(5):
        th = Producer(name='生产者%d号' % x)
        th.start()

    for x in range(5):
        th = Consumer(name='消费者%d号' % x)
        th.start()


if __name__ == '__main__':
    main()
