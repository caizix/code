"""
登录开心网
利用coolie
免除ssl
"""
"""
1.寻找入口，通过搜查
login_url="https://security.kaixin001.com/login/login_post.php"
相对应的用户名和密码 email password
2.构造opener3
3.构造login函数
"""
from http import cookiejar
from urllib import request,parse
import ssl
#忽略安全问题
ssl._create_default_https_context = ssl._create_unverified_context

cookie = cookiejar.CookieJar()
cook_headler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPHandler()

opener = request.build_opener(http_handler,https_handler,cook_headler)
def login():
    login_url = "https://security.kaixin001.com/login/login_post.php"
    data = {
        "email":"15981095894",
        "password":"123456"
    }
    data = parse.urlencode(data)
    #http请求头
    headers = {
        "Content-Length":len(data),
        "User-Agemt":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    req = request.Request(login_url,data=data.encode(),headers=headers)
    rsp = opener.open(req)
    html= rsp.read()
    html= html.decode()
    #print(html)

def getHomePage():
    base_url = "http://www.kaixin001.com/home/?_profileuid=181843594"
    rsp = opener.open(base_url)
    html = rsp.read()
    html.decode()
    print(html)


if __name__ == '__main__':
    login()
    getHomePage()