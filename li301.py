# 数据解析
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href ="link1.html">first item</a></li>
         <li class="item-1"><a href ="link2.htm1">second item</a></li>
         <li class="item-inactive "><a href ="link3.htm1">third item</a></li>
         <li class="item-1"><a href ="link4.htm1">fourth item</a></li>
         <li class="item-0"><a href ="link5.html">fifth item</a>
     </ul>
 </div>
'''

'''
#将字符串解析为html文件
html=etree.HTML(text)
print(html)
#将字符串序列化html
result=etree.tostring(html).decode('utf-8')
print(result)
'''
# 读取
html = etree.parse('hello.html')
result = etree.tostring(html).decode('utf-8')
print(result)
