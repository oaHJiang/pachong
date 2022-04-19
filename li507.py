#多线程下载王者荣耀高清壁纸
from urllib import parse
# result=parse.unquote('https%3A%2F%2Fshp.qpic.cn%2Fishow%2F2735041514%2F1650002839_1265602313_2614_sProdImgNo_8.jpg%2F200')
# print(result)
# 可以获取到高清壁纸的url，获取到url后通过parse.unquote解码，然后将最后的200变为0
# https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=4&totalpage=0&page=0&iOrder=0&iSortNumClose=1&jsoncallback=jQuery1710017807851079442605_1650101403644&iAMSActivityId=51991&_everyRead=true&iTypeId=1&iFlowId=267733&iActId=2735&iModuleId=2735&_=1650101403740
#page参数range(0,29)