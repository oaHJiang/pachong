import requests
from lxml import etree
import time
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
domian = 'https://xiaohua.zol.com.cn'
joke_list = []


def parse_page(page_url):  # 解析列表页
    resp = requests.get(page_url, headers=header)
    text = resp.text
    parser = etree.HTML(text)
    detail_url_list = parser.xpath(
        "//ul[@class='article-list']/li[@class='article-summary']//a[@class='all-read']/@href")
    for detail_url in detail_url_list:
        detail_url = domian + detail_url
        parse_detail(detail_url)
        time.sleep(2)


def parse_detail(detail_url):  # 解析详情页
    resp = requests.get(detail_url, headers=header)
    text = resp.text
    parser = etree.HTML(text)
    joke_title = parser.xpath("//h1[@class='article-title']/text()")
    joke_content = ''.join(
        parser.xpath("//div[@class='article-text']//text()")).strip()  # 有的text可能在子标签下，所以用//,''.join可以将列表的字符串拼接在一起
    joke_list.append({
        'title': joke_title,
        'content': joke_content
    })
    print(f'{joke_title}笑话下载完毕')


def main():  # 循环解析列表页
    for page in range(1, 11):
        page_url = f'https://xiaohua.zol.com.cn/new/{page}.html'  # 在字符串中加入变量值，使用f字符串写法
        parse_page(page_url)
        time.sleep(2)
    with open('joke.json', 'w', encoding='utf-8') as fp:
        json.dump(joke_list, fp, ensure_ascii=False)  # 若不是False，保存到json文件的中文会是Unicode字符串
    print('=' * 30)
    print('笑话数据抓取完毕')


if __name__ == '__main__':
    main()
