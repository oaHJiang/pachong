# request库
import requests

# 添加headers查询参数
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
response = requests.get('https://www.baidu.com/', headers=header)
# 添加参数,params接收一个字典或字符串的查询参数，字典类自动转换url编码，不需要urlencode()
kw = {'wd': '中国'}
response = requests.get('https://www.baidu.com/', headers=header, params=kw)
# print(response)
# 查询响应内容
# print(response.text)#返回Unicode格式数据
# 或
# print(response.content)#返回字节流数据，可以添加解码 .decode('utf-8')
print(response.url)
print(response.encoding)
