# URL地址解析
from urllib import parse

url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91&oq=%25E7%2599%25BE%25E5%25BA%25A6&rsv_pq=e90159c00001fd4e&rsv_t=d170%2FaNkEHoLuCiiuHfS5N8%2BTkkB8r%2F3UKZJ%2FDbZGs9A1Tn1ePHYJjhYHgg&rqlang=cn&rsv_enter=1&rsv_dl=ts_1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_sug2=1&rsv_btype=t&prefixsug=%25E7%2599%25BE%25E5%25BA%25A6&rsp=1&rsv_sug4=3945'
# result=parse.urlparse(url)
result = parse.urlsplit(url)  # urlsplit没有属性(params)
print(result)
print(result.scheme)
