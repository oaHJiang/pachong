# 什么是GIL锁？
# Python自带的解释器是CPython。CPython解释器的多线程实际上是一个假的多线程（在多核CPU中，只能利用一核，不能利用多核）。同一时刻只有一个线程在执行，为了保证同一时刻只有一个线程在执行，在CPython解释器中有一个东西叫做GIL (Global Intepreter Lock)，叫做全局解释器锁。这个解释器锁是有必要的。因为CPython解释器的内存管理不是线程安全的。当然除了CPython解释器，还有其他的解释器，有些解释器是没有GIL锁的，见下面：
# 1.Jython：用Java实现的Python解释器。不存在GIL锁。更多详情请见：https://zh.wikipedia.org/wiki/Jyhon
# 2.IronPython：用.net实现的Python解释器。不存在GIL锁。更多详情请见：https://zh.wikipedia.org/wiki/IronPython
# 3.PyPy：用Python实现的Python解释器。存在GIL锁。更多详情请见：https://zh.wikipedia.org/wiki/PyPy
# GIL虽然是一个假的多线程。但是在处理一些IO操作（比如文件读写和网络请求）还是可以在很大程度上提高效率的。在IO操作上建议使用多线程提高效率。在一些CPU计算操作上不建议使用多线程，而建议使用多进程。
# 有了GIL锁，为什么还需要Lock？
# GIL锁只是保证全局同一时刻只有一个线程在执行，但是他不能保证执行代码的原子性。也就是说一个操作可能分成几个部分完成，这样会导致数据有问题，所以需要Lock。

import requests
from lxml import etree
import time
import os
import threading
import queue

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'Referer': 'https://xiaohua.zol.com.cn'
}
domian = 'https://xiaohua.zol.com.cn'


class Producer(threading.Thread):
    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self) -> None:
        while not self.page_queue.empty():
            page_url = self.page_queue.get()
            resp = requests.get(page_url, headers=header)
            text = resp.text
            parser = etree.HTML(text)

            joke_list = parse_page(parser)
            for index, joke_inf in enumerate(joke_list):
                dir_path = os.path.join('joke', joke_inf['name'])
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)  # mkdir()创建路径下的文件夹，path.join连接路径
                detail_url = joke_inf['joke_url']
                joke_content = parse_detail(detail_url)
                joke_path = os.path.join(dir_path, '%s.txt' % joke_inf['name'])
                self.joke_queue.put(
                    {'joke_content': joke_content,
                     'joke_path': joke_path})


class Consumer(threading.Thread):
    def __init__(self, joke_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.joke_queue = joke_queue
    def run(self) -> None:
        while True:
            try:
                joke_obj = self.joke_queue.get(timeout=10)
                joke_content = joke_obj.get('joke_content')
                joke_path = joke_obj.get('joke_path')
                try:
                    with open(f'{joke_path}', 'w', encoding='utf-8') as fp:
                        fp.write(joke_content)
                        fp.close()
                except:
                    print('%s笑话数据下载失败' % joke_path)
            except:
                break


def parse_page(parser):  # 解析列表页
    joke_list = []
    detail_url_list = parser.xpath(
        "//ul[@class='article-list']/li[@class='article-summary']//a[@class='all-read']/@href")
    name_list = parser.xpath("//ul[@class='article-list']//span[@class='article-title']/a/text()")
    for index, detail_url in enumerate(detail_url_list):
        joke_url = domian + detail_url
        joke_list.append({
            'name': name_list[index].replace(':', ',').replace('?', ','),
            'joke_url': joke_url
        })
    return joke_list


def parse_detail(detail_url):  # 解析详情页
    resp = requests.get(detail_url, headers=header)
    text = resp.text
    parser = etree.HTML(text)
    oke_title = parser.xpath("//h1[@class='article-title']/text()")
    joke_content = ''.join(
        parser.xpath("//div[@class='article-text']//text()")).strip()  # 有的text可能在子标签下，所以用//,''.join可以将列表的字符串拼接在一起
    return joke_content


def main():
    page_queue = queue.Queue(5)
    joke_queue = queue.Queue(100)
    for page in range(1, 6):
        page_url = f'https://xiaohua.zol.com.cn/new/{page}.html'  # 在字符串中加入变量值，使用f字符串写法
        page_queue.put(page_url)

    for x in range(3):
        th = Producer(page_queue, joke_queue, name='生产者%d号' % x)
        th.start()

    for x in range(5):
        th = Consumer(joke_queue, name='消费者%d号' % x)
        th.start()


if __name__ == '__main__':
    main()
