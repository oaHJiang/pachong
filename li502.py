import threading
import time


# threading.current_thread()可以看到当前线程的信息
# threading.enumerate()可以看到当前的线程
# 为了让线程代码更好地封装，可以使用threading模块下的Thread类，继承自这个类，然后实现run方法，线程会自动运行run方法中的代码
class CodingThread(threading.Thread):
    def run(self):
        the_thread = threading.current_thread()
        for x in range(3):
            print('%s正在写代码' % the_thread.name)
            time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        the_thread = threading.current_thread()
        for y in range(3):
            print('%s正在画画' % the_thread.name)
            time.sleep(1)


def multi_thread():
    th1 = CodingThread()
    th2 = DrawingThread()

    th1.start()
    th2.start()


if __name__ == '__main__':
    multi_thread()
