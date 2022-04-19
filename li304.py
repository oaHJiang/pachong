from bs4 import BeautifulSoup

html=""" 
<html><head><title>The Dormouse's story </title ></head >
<body>
<p class="title" name ="dromouse"><b>The Dormouse's story</b></p>
<p class="story">0nce upon a time there were three 1ittle sisters; and their names were 
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/ti11ie" class="sister" id="link3">Tillie </a>;
and they lived at the bottom of a well.</p>
<p class ="story">...</p>
"""
soup=BeautifulSoup(html,'lxml')
print(soup.prettify())