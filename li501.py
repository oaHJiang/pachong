# 多线程
import threading
import time


def coding():
    for x in range(3):
        print('%d正在写代码' % x)
        time.sleep(1)


def drawing():
    for y in range(3):
        print('%d正在画画' % y)
        time.sleep(1)


def single_thread():
    coding()
    drawing()


def multi_thread():
    th1 = threading.Thread(target=coding)  # 不能用coding()
    th2 = threading.Thread(target=drawing)

    th1.start()
    th2.start()


if __name__ == '__main__':
    # single_thread()
    multi_thread()
