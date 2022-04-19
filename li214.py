import requests
'''
resp=requests.get('https://www.baidu.com/')
print(resp.cookies)
print(resp.cookies.get_dict())
'''

#case1
'''
url='https://www.zhihu.com/hot'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'cookie':'_zap=a02ac108-85c0-4aa5-b5e2-1044791de388; _xsrf=dA926aKRkVOSZ9hUAZYylKDC2qTpajB0; d_c0="AGCfRoZnshSPTgAX61KcyAqyRgLGgX6vrrM=|1648349899"; __snaker__id=0gTWEUuDdmCjAnrz; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=GHk8CzO%2FJ6ZBQBBREEZqr6GSMa8rxTGa; l_cap_id="NTk0YzdhYThhMGIzNDI3YmJhMzUzZWEwNjQyMTJkMzA=|1648349975|430aa863dbaefb3a71c65b1029a3d60cb4709beb"; r_cap_id="MDkxYzY3NTQ5ODdmNGQwNTkwYTdjNzk0NDZhMzM1YTk=|1648349975|8edeab91c9c1be331d4b010fee68c6ddab39739e"; cap_id="MDRkMWY0NGUzYTAwNGJkYmEyYjQ0MGQ2M2FkZTQ0MGM=|1648349975|930af50e870a12ff15011529906e6930aa833983"; q_c1=7bca3a7e04074cd389e530d5dec406cf|1648349995000|1648349995000; gdxidpyhxdE=qxiVSmLznO1wv2E768Shz4hvMdXPuDCmq1VOo5NscTOPk%5CCN7nLJjmPzlL3Iijz3TvEs2d8mSKhHy1Jl0CMJXp5EAD0EVewpE2guPQXEx84B7LjWyBzLgXx7k3Eppkzu%2BZHj%2B1ym2JH%2Bx%2BSS6j4yl6jRi%2FWa69SsZgCZ8Yp%2FpVXgwdPO%3A1648524860703; YD00517437729195%3AWM_NI=%2BvjuWh8ovIdwAQDc9gI7f9dkezjGqCpwLeqZEdXQU%2BysjUdXfcb1Wg3KHq4v4nqWJSTIs2NUSblCnbOCQ%2FobJbj0fBSifDtFXtfjIDS2zgkvrg7CEtHycxzAeHHBWYb9cUY%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea4b133b6a78391b545f6bc8bb7d44a879a8fbbaa7bf596818ae479afeea598c12af0fea7c3b92ae9aaa696d664fcb1baaae77d838f8c84bc6d8be9aadae761a7a6a6a8f449b4a98486f45287bc98b2d821bbada6b6e754a6bdaed2d66df1958892b77ef8b2bfb8c9599897bdd3cd5f91bea4a4ed6a8d9d9fd0ee6a8abea6d1e54a91b7aaa5f74e9cacaa8bcc5091eeb688ea7eb2b9f9a4c8808ca7ad99f94ba79888a3d653a2e7adb6dc37e2a3; captcha_session_v2=2|1:0|10:1648523960|18:captcha_session_v2|88:Q2ZWWEQ3eTc0VXFEaFgzUDFXa20rZXExUTB5bzZzaXAyMCsrSkY1REd3ajBId082dEYxUERuRXNCRHdEQ2l2OQ==|9ae35771eb4cf6864ba9e0e443d8541ed1c3d5f77314bca166aac7c2859a51a0; captcha_ticket_v2=2|1:0|10:1648523972|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfMFZDZThtNm5Mb2RhNFpOT2V3RnhvUVVNQXBYWS5DRkxoS0l1RVpEZWVyVmZjOXlfYXdXWWp6b05TSEtnVzdpekRzbEdIVjZoQlo1aThwZ0Q1SGdnY2Z0bHpkc0V6NHc2Y3lZdWFRTlM1bXM5bHUxeDFQU1hQSDJzYjlST3F3OVhtWTZjUDd5MWZ3YWttMEZzdU9EQ1lmeGRiNnJkS1puamtmcUJQdmJtaUR6bkZ4S3JDdHRwT0FqVWI3bDVxck1SOFhKOTVzc1RNR1BpNUhHN0lwYXdzWVhEclFCdGRCRkdHSWhyRTloUERHSEVsZDF2bXgyQVIuRVpVay43alpydGdCZVI4R3VmOFNhdlJSQmZ2SXo0elZjSFMuTTBaYUFnU1lZeUVXcHlOa1RWbHJ0b3hvMkNydjRadlYwS3pCaGktT3AueGpLaklrOTl0LnliUFU5QndZQmhEUHppUnhKNHZ3RF8xLlVJemZzeXpSQnFmWVRLUi1wUi1MMW9UcmQ5THZlQkM3NmhkamNmb3QwLjlZQ1FWUTZTUVFYZDdmTWVvT0tqWllCWC1GWi1QR2JuWkJlZDRyQlI0WG5pXzB6akU3TTB5OHRUT0hOdHF5MmpVWDFVT1FfOU9wNnFuZ2FneXBpcUxQQXJFSk9nbjZycDJkYXcyNEVfSVpJMyJ9|bea1fce202d1ffebc8233c91e15b2968a01c8d66395430bb918e62cc2460aa87; z_c0=2|1:0|10:1648523972|4:z_c0|92:Mi4xdHJ6dE53QUFBQUFBWUo5R2htZXlGQ1lBQUFCZ0FsVk54TWd2WXdEN0MtS096YzQ1enBheVRmLVk2M2J0TGNpUjBR|85a59700c27a880c76f62cc255516de1fc3287a7f4ca4f78fea83505b754bdd4; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1648453622,1648474252,1648521635,1648542700; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1648542700; tst=h; NOT_UNREGISTER_WAITING=1; SESSIONID=DDoRtTUt1ACo9dP3BmuEjpPSbp04qlK2aT2pTr9ljzU; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1648542701|1648542698; JOID=W10TA0iJkS2Rdr7rAIC38lv10F8bwdZEwAjmvXKy3G34TNC3MGtXavpwse4FW2z19j0V7Kt3xpKixlF6a5ZKC94=; osd=Ul0RC02AkS-Zc7frAoiy-1v32FoSwdRMxQHmv3q31W36RNW-MGlfb_Nws-YAUmz3_jgc7Kl_w5uixFl_YpZIA9s='
}
resp=requests.get(url,headers=header)
print(resp.text)
'''

#case2
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
post_url='https://i.meishi.cc/login_t.php?redirect=https%3A%2F%2Fwww.meishij.net%2F%3Fsession_id%3D23221efc82d454145c4dcbf7ad04da78'
post_data={
    'username':'15754519404',
    'password':'lnxmol22.4'
}

#共享cookie

#登陆
session=requests.session()#会话对象
session.post(post_url,headers=header,data=post_data)
#访问个人网页
url='https://i.meishi.cc/cook.php?id=15116714'
resp=session.get(url)
print(resp.text)