# 多线程下载王者荣耀高清壁纸--v1
from urllib import parse
from urllib import request
import requests
import os

# https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=4&totalpage=0&page=0&iOrder=0&iSortNumClose=1&jsoncallback=jQuery1710017807851079442605_1650101403644&iAMSActivityId=51991&_everyRead=true&iTypeId=1&iFlowId=267733&iActId=2735&iModuleId=2735&_=1650101403740
# 可以获取到高清壁纸的url，
# 获取到url后通过parse.unquote解码，
# result=parse.unquote('https%3A%2F%2Fshp.qpic.cn%2Fishow%2F2735041514%2F1650002839_1265602313_2614_sProdImgNo_8.jpg%2F200')
# print(result)
# 然后将最后的200变为0
# page参数range(0,29)
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'Referer': 'https://pvp.qq.com/web201605/wallpaper.shtml'
}


def extract_images(data):
    image_urls = []
    for x in range(1, 9):
        image_url = parse.unquote(data['sProdImgNo_%d' % x]).replace('200', '0')
        image_urls.append(image_url)
    return image_urls


def main():
    page_url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=0&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=1&iFlowId=267733&iActId=2735&iModuleId=2735&_=1650509482242'
    resp = requests.get(page_url, headers=header)
    result = resp.json()  # 可得到python对象--字典
    print(result)
    datas = result['List']
    for data in datas:
        # sProdImgNo_1 = parse.unquote(data['sProdImgNo_1']).replace('200','0')
        image_urls = extract_images(data)
        # print(sProdImgNo_1)
        name = parse.unquote(data['sProdName'])
        dirpath = os.path.join('image', name)
        print(dirpath)
        # image/name/n.jpg
        os.mkdir(dirpath)  # mkdir创建路径下的文件夹，path.join连接路径
        for index, image_url in enumerate(image_urls):
            request.urlretrieve(image_url, os.path.join(dirpath, '%d.jpg' % (index + 1)))

        # print('=' * 20)
        # print(name)
        # print(image_urls)
        # print('=' * 20)


if __name__ == '__main__':
    main()
