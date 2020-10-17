import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }#请求头
    Url="http://top.baidu.com/buzz?b=1&fr=topindex"
    req=requests.get(Url)
    print(req.apparent_encoding)
    data=req.content.decode("GB18030")#编码为GB18030
    soup=BeautifulSoup(data,"lxml")
    X=soup.find_all("a",class_="list-title")#热搜标题
    Y=soup.find_all("td",class_="last")#热搜指数
    L=soup.find_all("td",class_="tc")#热搜相关资源
    n=len(X)
    i=0
    while i < n:
        print(X[i].string,Y[i].span.string)
        print(L[i].find_all("a")[0].attrs["href"])#新闻
        print(L[i].find_all("a")[1].attrs["href"])#视频
        print(L[i].find_all("a")[2].attrs["href"])#图片
        i = i + 1
