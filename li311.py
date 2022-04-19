import re
#多字符匹配

# *:匹配0个或多个字符
text='abc'
res=re.match('\w*',text)
print(res.group())

# +:匹配一个或多个字符
text='12c'
res=re.match('\d+',text)
print(res.group())

# ?:匹配前一个字符0个或1个
text='abc'
res=re.match('\w?',text)
print(res.group())

# {m}:匹配m个字符
text='1abc'
res=re.match('\w{2}',text)
print(res.group())

# {m,n}:匹配m-n个字符
text='1abc'
res=re.match('\w{1,3}',text) #返回满足条件最多的
print(res.group())

