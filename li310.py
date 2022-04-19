import re

# 正则表达式单字符匹配

# 匹配某个字符串

# text='abc'
# ret=re.match('ab',text)#match从第一个字符开始匹配
# print(ret.group())

# 点(.)匹配任意字符除了'\n'
text='abc'
ret=re.match('.',text)
print(ret.group())

# \d匹配任意数字[0-9]
text='10bc'
ret=re.match('\d',text)
print(ret.group())

# \D匹配任意非数字
# text='+bc'
# ret=re.match('\D',text)
# print(ret.group())

# \s匹配空白字符(包括\n,\t,\r和空格)\t为制表符
# text='\rbc'
# ret=re.match('\s',text)
# print('='*10)
# print(ret.group())
# print('='*10)

#\S匹配非空白字符
# text='+bc'
# ret=re.match('\D',text)
# print(ret.group())

# \w匹配a-z,A-Z,数字及下划线
# text='_Abc'
# ret=re.match('\w',text)
# print(ret.group())

# \W匹配和\w相反

#[]组合的方式，满足括号中某一项都可以匹配
# text='bc'
# ret=re.match('[1b]',text)
# print(ret.group())

# 组合方式实现\d
# text='2bc'
# ret=re.match('[0-9]',text)
# print(ret.group())

#组合方式实现\D
# text='bc'
# ret=re.match('[^0-9]',text) # ^:取反
# print(ret.group())

# 组合方式实现\w
# text='bc'
# ret=re.match('[a-zA-Z0-9_]',text)
# print(ret.group())

