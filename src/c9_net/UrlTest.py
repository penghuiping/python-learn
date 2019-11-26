# encoding=utf8
import urllib.request as req

# 这个with..as 类似于 java7 中 try..with..resources
request = req.Request(url="https://www.baidu.com", method="POST")
with req.urlopen(request) as res:
    html = res.read()
    print(html)
