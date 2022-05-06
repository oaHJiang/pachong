from urllib import request

# 无代理
'''
url='http://httpbin.org/ip'
resp=request.urlopen(url)
print(resp.read())
'''
# 使用代理
url = 'http://httpbin.org/ip'
# 使用proxyhandler，传入代理构建一个handler
handler = request.ProxyHandler({'http': '120.220.220.95:8085'})
# 使用handler构建opener
opener = request.build_opener(handler)
# 使用opener发送请求
resp = opener.open(url)
print(resp.read())
