#处理不信任的SSL证书
import requests
url='https://inv-veri.chinatax.gov.cn/'
resp=requests.get(url,verify=False)
print(resp.content.decode('utf-8'))