# request库--代理
import requests

proxy = {
    'http': '120.220.220.95:8085'
}  # 代理ip
url = 'http://httpbin.org/ip'
resp = requests.get(url, proxies=proxy)
print(resp)
print(resp.text)
