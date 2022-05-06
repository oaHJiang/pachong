# 发送post请求
import requests

url = 'https://i.meishi.cc/cook.php?id=15116714'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
data = {
    'redirect': 'http://i.meishi.cc/',
    'username': '15754519404',
    'password': 'lnxmol22.4'
}
resp = requests.post(url, headers=header, data=data)
print(resp.text)
