import re
import requests
import time

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
}


def parse_page(page_url, f):
    resp = requests.get(page_url, headers=header)
    text = resp.text
    res = re.search(r"""
    <div.+?bookname.+?<h1>(.+?)</h1>.+?content.+?>(.+?)</div>
    """, text, re.VERBOSE | re.DOTALL)
    title = res.group(1).encode('iso-8859-1').decode('gbk')
    chapter = res.group(2).encode('iso-8859-1').decode('gbk')
    chapter = re.sub(r'&nbsp;&nbsp;&nbsp;&nbsp;', '    ', chapter)
    chapter = re.sub(r'<br />', '', chapter)
    chapter = re.sub('\n', '', chapter)
    article = title + '\n' + chapter + '\n'
    f.write(article)


def main():
    source_url = 'https://www.qbiqu.com/0_1/'
    resp = requests.get(source_url, headers=header)
    text = resp.text
    res = re.search(r"""
    <div.+?list.+?<dt>.+?</dt>.+?<dt>.+?</dt>(.+?)</dl>
    """, text, re.VERBOSE | re.DOTALL)
    res = res.group(1)
    res = re.findall(r'/0_1/.+?html', res)
    head_url = 'https://www.qbiqu.com'
    with open('大主宰.txt', mode='a+', encoding='utf-8') as f:
        base_url = 'https://www.qbiqu.com{}'
        for x in res[0:50]:
            page_url = base_url.format(x)
            parse_page(page_url, f)
            time.sleep(5)
    f.close


if __name__ == '__main__':
    main()
