#contents和children
#contents返回所有子节点的列表
#children返回所有子节点的迭代器
from bs4 import BeautifulSoup
html=""" 
<html><head><title>The Dormouse's story </title ></head>
<body>
<p class="title" name ="dromouse">The Dormouse's story</p>
<p class="story">0nce upon a time there were three 1ittle sisters; and their names were 
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/ti11ie" class="sister" id="link3">Tillie </a>;
and they lived at the bottom of a well.</p>
<p class ="story">...</p>
<b><!--Hey, buddy. Want to buy a used parser?--></b>
"""
soup=BeautifulSoup(html,'lxml')#beautifulsoup可当做tag对象
'''
head_tag=soup.head
print(head_tag.contents)
print(head_tag.children)
for i in head_tag.children:
    print(i)
'''
#strings:如果tag包含多个非标签字符串，可以使用.strings来循环获取
#stripped_strings:输出的非标签字符串可能包含很多空格或空行，stripped_strings可去除多余空白内容
'''
for string in soup.strings:
    print(repr(string))#repr可打印出换行符
'''
'''
for string in soup.stripped_strings:
    print(repr(string))
'''
print(soup.b.string)
#string不能获取多行字符