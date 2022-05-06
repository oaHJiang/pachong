from cgitb import text
import re

# 转义字符和原生字符:

# Python中的转义字符:
text = 'hello\nworld'
print(text)
# 转义：\\
text = 'hello\\nworld'
print(text)
# 原生字符串r''：
text = r'hello\nworld'
print(text)

# 正则表达式中的转义字符:加\
text = 'apple price is $99,orange price is $88'
res = re.findall('\$\d+', text)
print(res)

# 原生字符串和正则表达式
# 正则表达式的字符串解析规则
# 1.先把字符串放到Python语言层面解析
# 2.再把Python层面语言解析的结果放到正则表达式层面解析
'''
text='\cba c'
res=re.match('\\c',text)#Python语言层面解析结果:\c
print(res.group())
'''
text = '\cba c'
res = re.match('\\\\c', text)  # \\\\c -> Python语言层面解析结果:\\c -> 正则表达式结果:\c
print(res.group())
# 简化，使用原生字符串
text = '\cba c'
res = re.match(r'\\c', text)  # \\c -> 正则表达式结果:\c
print(res.group())
