import mechanize
import time
from bs4 import BeautifulSoup
import re
import urllib
import string
import os

def downloadProcess (html, base,filetype,linkList):
    "This does the actual file downloading."
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        linkText = str(link.get('href'))

        if filetype in linkList:
            slashList = [i for i, ind in enumerate(linkText) if ind =='/']
            directoryName = linkText[(slashList[0]+1):slashList]
            if not os.path.exists(directoryName):
                os.makedirs(directoryName)

            image = urllib.URLopener()
            linkGet = base + linkText
            filesave = string.lstrip(linkText,"/")
            image.retrieve (linkGet,filesave)
        elif "htm" in linkText: #covers both "html" and "htm"
            linkList.append(link)





start = "http://" + input ("where would you like to start searching? \n")
filetype = input ("what file type are you looking for?\n")

numSlash = start.count('/')
slashLish = [i for i, ind in enumerate(start) if ind =='/']

if (len(slashLish) >=3):
    third = slashLish[2]
    base = start[:third]
else:
    base = start

br = mechanize.Browser()
r = br.open(start)
html = r.read()
linkList = []
print("Parsing" +start)
downloadProcess(html,base,filetype,linkList)

for leftover in linkList:
    time.sleep(0.1)
    linkText = str(leftover.get('href'))
    print("Parsing"+ base + linkText)
    br = mechanize.Browser()
    r = br.open(base + linkText)
    html = r.read()
    linkList = []
    downloadProcess(html,base,filetype,linkList)