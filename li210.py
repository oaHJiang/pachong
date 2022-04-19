from urllib import request
from http.cookiejar import MozillaCookieJar
'''
#保存
cookiejar=MozillaCookieJar('cookie.txt')#保存cookie
handler=request.HTTPCookieProcessor(cookiejar)
opener=request.build_opener(handler)
resp=opener.open('http://httpbin.org/cookies/set/course/abc')

cookiejar.save(ignore_discard=True,ignore_expires=True)
#按ctrl点击save进入源码,dsicard保存要被丢弃的,expire保存过期的
'''
#加载
cookiejar=MozillaCookieJar('cookie.txt')#保存cookie
cookiejar.load()
handler=request.HTTPCookieProcessor(cookiejar)
opener=request.build_opener(handler)
resp=opener.open('http://httpbin.org/cookies/set/course/abc')
for cookie in cookiejar:
    print(cookie)
