import requests
from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/1/"

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    "Accept":'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    "Accept-Language":'zh-CN,zh;q=0.9'
}
# 下载页面
rsp = requests.get(url, headers=headers)
html = rsp.text

# 把页面解析成html
html = etree.HTML(html)
print(html.text)
rst = html.xpath('//div[contains(@id, "qiushi_tag")]')

for r in rst:
    # print(type(r))
    # print(r.tag)
    # print(r)
    #print(r.text)
    item = {}
    #print(r)

    # content = r.xpath('//div[@class="content"]/span')[0].text.strip()
    # print(content)