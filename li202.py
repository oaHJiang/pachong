#url编解码
from urllib import parse
data={'name':'老王','age':18,'greet':'hello world'}
qs=parse.urlencode(data)#只能编码字典
print(qs)
print(parse.parse_qs(qs))#编码后的url参数解码
#字符串编码
#parse.quote()