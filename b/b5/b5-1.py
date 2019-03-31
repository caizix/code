"""
爬取百度贴吧，张继科吧
1.主页
https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=0
https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=100
https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=150
https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=200
解决方法：
1.准备构建参数字典
    字典分为kw  ie  pn 
2.使用parse构建完整的url
3.使用for循环下载
"""

from urllib import request,parse

if  __name__ == '__main__':
    qs = {
        "kw":"张继科",
        "ie":"utf-8",
        "pn":0
    }

    urls = []
    baseurl = "https://tieba.baidu.com/f"
    for i in range(10):
        pn = (i)*50
        qs['pn'] = str(pn)
        urls.append(baseurl+parse.urlencode(qs))
    print(urls)
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode("utf-8")
        print(url)
        print(html)
