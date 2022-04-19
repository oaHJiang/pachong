import re

#1.验证手机号码：手机号码以1开头，第二位可以是34587，后面9位随意
text='18711223344'
res=re.match('1[34587]\d{9}',text)
print(res.group())

#2.验证邮箱：邮箱名是由数字，英文，下划线组成，然后是@，后面是域名
text='123a_@qq.com'
res=re.match('\w+@[a-z0-9]+\.[a-z]+',text) #\.的\表示转义
print(res.group())

#3.验证URL：前面是http或https或ftp加上：，再加斜杠/，后面是任意非空白字符
text='https://www.kuaidaili.com/free/inha/3/'
res=re.match('(http|https|ftp)://\S+',text)
print(res.group())

#4.验证身份证：前十七位是数字，最后一位为数字或X,x
text='55414719961205551x'
res=re.match('\d{17}[\dxX]',text)
print(res.group())
