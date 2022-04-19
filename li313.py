from cgitb import text
import re

# 开始，结束和非贪婪

# ^:以...开头
text='hello world'
# res=re.match('hello',text)
res=re.search('^hello',text)
print(res.group())

# $:以...结尾
text='hello world'
res=re.search('world$',text)
print(res.group())

text=''
res=re.search('^$',text)
print(res.group())

# |:匹配多个字符串或表达式

# 贪婪和非贪婪
text='12345'
res=re.search('\d+?',text) #这里+?代表非贪婪模式
print(res.group())

# case1:提取html标签名称
text='<h1>这是标题</h1>'
res=re.search('<.+?>',text)
print(res.group())

# case2:验证一个数字是否在0-100间
text='100'
res=re.match('0$|[1-9]\d?$|100$',text)
print(res.group())