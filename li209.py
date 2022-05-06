from urllib import request
from http.cookiejar import CookieJar
from urllib import parse

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}

# 1.登陆
# 1.1创建cookiejar对象
cookiejar = CookieJar()
# 1.2使用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3使用handler创建opener
opener = request.build_opener(handler)
# 1.4使用opener发送登陆请求(账号和密码)
post_url = 'https://i.meishi.cc/login_t.php?redirect=https%3A%2F%2Fwww.meishij.net%2F%3Fsession_id%3D23221efc82d454145c4dcbf7ad04da78'

post_data = parse.urlencode({
    'username': '15754519404',
    'password': 'lnxmol22.4'
})
req = request.Request(post_url, data=post_data.encode('utf-8'))
opener.open(req)

# 2访问网页
url = 'https://i.meishi.cc/cook.php?id=15116714'
rq = request.Request(url, headers=header)
resp = opener.open(rq)
print(resp.read().decode('utf-8'))
