from urllib import request

url = 'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=17fc54ed41bc8-016eed40db3183-9771a3f-144000-17fc54ed41bc8&timeStamp=1648287246462&User-Agent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk5LjAuNDg0NC44MiBTYWZhcmkvNTM3LjM2&index=502&channelId=40009&sVersion=2&signKey=27c4fbf34772d83c894ff6a05c9d6ea1'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
rq = request.Request(url, headers=header)
resp = request.urlopen(rq)
print(resp.read().decode('utf-8'))  # decode解码
