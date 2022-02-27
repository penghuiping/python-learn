# encoding=utf8
import requests

data = {
    "appId": "jintianli_123",
    "appSecret": "123456"
}

try:
    res = requests.post(url="http://localhost:8080/rcs/basic/login",
                        json=data, headers={"Content-Type": "application/json;charset=UTF-8"})
    print(res.text)
finally:
    res.close()



