from turtle import title
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
soup=BeautifulSoup(html,'lxml')
'''
print(soup.p)#Tag对象,查找第一个符合要求的标签
print(soup.p.name)#标签名
print(soup.p.attrs)#属性字典
print(soup.p['class'])#属性值
print(soup.p.get('class'))#属性值 

soup.p['class']='new'#更改属性
print(soup.p)
'''
print(soup.p.string)#navigable.string类型

print(soup.b.string)#comment类型，特殊的navigable.string对象