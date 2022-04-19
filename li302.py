#在html中使用xpath语法
from cgitb import html
from lxml import etree
html=etree.parse('hello.html')
#获取所有li标签
'''
result=html.xpath('//li')
for i in result:
    print(etree.tostring(i))
'''
#获取li标签下所有class的属性value(值)
'''
result=html.xpath('//li/@class')
print(result)
'''
#获取li标签下href为www.baidu.com的a标签

result=html.xpath('//li/a[@href="link4.htm1"]')
for i in result:
    print(etree.tostring(i))

#获取li标签下所有span标签
'''
result=html.xpath('//li//span')#若使用/span,找li标签的子标签/span,找不到
print(result)
'''
#获取li标签下的a标签里所有的class的属性值
'''
result=html.xpath('//li/a//@class')
print(result)
'''
#获取最后一个li的a的href属性对应值
'''
result=html.xpath('//li[last()]/a/@href')
print(result)
'''
#获取倒数第二个li元素的内容
'''
result=html.xpath('//li[last()-1]/a')
print(result[0].text)
'''
#获取倒数第二个li元素的内容的第二种方式
'''
result=html.xpath('//li[last()-1]/a/text()')
print(result)
'''