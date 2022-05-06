# 搜索文档树
# find找到第一个满足要求的标签并返回，find_all返回所有满足要求的标签
from bs4 import BeautifulSoup

html = """
<table class="tablelist" celpadding="0" cel1spacing="0">
    <tbody>
        <tr class="h">
            <td class="1" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=33824&keyWords=python&amp;tid=87&amp;lid=2218">01工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&amp;tid=87&amp;lid=2218">02工程师</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=31236&keywords=python&amp;tid=87&amp;lid=2218">03工程师</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=31235&keyWords=python&amp;tid=87&amp;lid=2218">04工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=34531&keyWords=python&amp;tid=87&amp;lid=2218">05工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=34532&keywords=python&amp;tid=87&amp;lid=2218">06工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=31648&keyWords=python&amp;tid=87&amp;lid=2218">07工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=32218&keywords=python&amp;tid=87&amp;lid=2218">08工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="1 square"><a target="_blank" href="position_detail.php?id=32217&keywords=python&amp;tid=87&amp;lid=2218">09工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="1 square"><a id="test" class="test" target="_blank" href="position_detail.php?id=34511&keywords=python&amp;tid=87&amp;lid=2218">10工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
    </body>
</table>
"""
soup = BeautifulSoup(html, 'lxml')
# 1.获取第一个tr标签
'''
print(soup.tr)
print(soup.find('tr'))
'''
# 2.获取所有tr标签
'''
trs=soup.find_all('tr')#trs为列表
for i in trs:
    print(i)
'''
# 3.获取第二个tr标签
'''
tr=soup.find_all('tr',limit=2)[1]
print(tr)
'''
# 4.获取所有class等于even的tr标签
# trs=soup.find_all('tr',class_='even')#注意_,class为Python的关键词，要加下划线
'''
trs=soup.find_all('tr',attrs={'class':'even'})
for i in trs:
    print(i)
    print('='*10)
'''
# 5.将所有id等于test,class等于test的a标签提取出来
'''
list=soup.find_all('a',id='test',class_='test')
for i in list:
    print(i)
'''
# 6.获取所有a标签的href属性
# alist=soup.find_all('a')

# for i in alist:
# 1.
# href=i['href']
# print(type(i))#tag型
# print(href)
# 2.
# href=i.attrs['href']
# print(href)

# 7.获取所有职位信息(文本)
trs = soup.find_all('tr')[1:]  # 列表切片
'''
list=[]
'''

for tr in trs:
    infos = list(tr.stripped_strings)
    print(infos)
'''
    info={}
    tds=tr.find_all('td')
    name=tds[0].string
    category=tds[1].string
    print('名称为：',name,'类别为：',category)
    info['name']=name
    info['category']=category
    list.append(info)
print(list)
    '''
'''
    for string in tr.stripped_strings:
        print(string)
        print(type(string))
   '''
