#css选择器
#select返回列表型
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
#1.通过标签名查找
# print(soup.select('a'))#查找所有的
#2.通过类名查找
#print(soup.select('.sister'))
#print(soup.select('a[class="sister"]'))
#3.通过id查找
#print(soup.select('#link1'))
#4.组合查找
print(soup.select('p #link1'))#空格表示p标签下子标签
#print(soup.select('head>title'))
#5.通过属性查找
#print(soup.select('a[href="http://example.com/elsie"]'))
#6.获取内容
#print(soup.select('title')[0].get_text())