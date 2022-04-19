from urllib import request
url='https://www.biedoul.com/'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
rq=request.Request(url,headers=header)
resp=request.urlopen(rq)
print(resp.read().decode('utf-8'))