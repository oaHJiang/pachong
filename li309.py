# --coding:utf-8--
import random
import requests
from bs4 import BeautifulSoup
import time

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
}
detail_urls = []

proxy = [
    '106.55.15.244:8889', '202.109.157.61:9000', '14.215.212.37:9168', '106.15.197.250:8001', '103.37.141.69:80',
    '47.113.90.161:83'
]  # 代理ip


def main():
    with open('movie.csv', 'a', encoding='utf-8') as fp:
        for page in range(0, 50, 25):
            url = f'https://movie.douban.com/top250?start={page}&filter='
            detail_urls = get_detail_urls(url)
            get_url_content(detail_urls, fp)
            time.sleep(random.uniform(1.0, 2.5))
    print('=' * 30)
    print('电影数据抓取完毕')


def get_detail_urls(url):  # 解析列表页
    resp = requests.get(url, headers=header, proxies={'http': random.choice(proxy)})
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
    lis = soup.find('ol', class_='grid_view').find_all('li')
    for li in lis:
        detail_url = li.find('a')['href']
        # print(detail_url)
        detail_urls.append(detail_url)
        time.sleep(random.uniform(0.5, 1.5))
    return detail_urls


def get_url_content(detail_urls, fp):
    for detail_url in detail_urls:
        resp = requests.get(detail_url, headers=header, proxies={'http': random.choice(proxy)})
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        print(soup)
        name = ''.join(soup.find('span', property="v:itemreviewed").strings)
        directors = []
        sreenwriters = []
        actors = []
        types = []
        dires = soup.find_all('span', class_='attrs')[0].strings
        for i in dires:
            directors.append(i)
        directors = ''.join(directors)
        screens = soup.find_all('span', class_='attrs')[1].strings
        for i in screens:
            sreenwriters.append(i)
        sreenwriters = ''.join(sreenwriters)
        acts = soup.find_all('span', class_='attrs')[2].strings
        for i in acts:
            actors.append(i)
        actors = ''.join(actors)
        type = soup.find_all('span', property="v:genre")
        for i in type:
            types.append(i.string)
        types = '/'.join(types)
        fp.write('{},{},{},{},{}\n'.format(name, directors, sreenwriters, actors, types))
        print(f'{name}信息爬取完毕')
        time.sleep(random.uniform(5, 10))


if __name__ == '__main__':
    main()
