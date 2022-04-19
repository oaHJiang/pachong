#下载
from urllib import request
'''
resp=request.urlopen('http://www.sogou.com/')#打开网站
print(resp.read())#读取对象
'''
request.urlretrieve('https://pic.baike.soso.com/ugc/baikepic2/8261/cut-20211218073221-1449301508_jpg_945_1179_1780605.jpg/300','shiyuanlimei.jpg')