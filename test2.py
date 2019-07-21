import hashlib
import hmac
import base64
import json
#test

secretKey = 'SwYNTwt5qPABx29Atyi0'
body='{"page":"1","pageSize":"20","app_key":"lemondream"}'
bo={"page": "1", "pageSize": "20", "app_key": "lemondream"}

co = json.dumps(bo).replace(" ", "")  #讲bo 变成 body

boo={'page':'1','pageSize':'20','app_key':'lemondream'}
booo =json.dumps(boo).replace(" ", "")

body1 = base64.b64encode(hmac.new(str.encode(secretKey), str.encode(str(body)), digestmod=hashlib.sha256).digest())
co1 = base64.b64encode(hmac.new(str.encode(secretKey), str.encode(str(co)), digestmod=hashlib.sha256).digest())
bo1 = base64.b64encode(hmac.new(str.encode(secretKey), str.encode(str(bo)), digestmod=hashlib.sha256).digest())
boo1 = base64.b64encode(hmac.new(str.encode(secretKey), str.encode(str(boo)), digestmod=hashlib.sha256).digest())
booo1 = base64.b64encode(hmac.new(str.encode(secretKey), str.encode(str(booo)), digestmod=hashlib.sha256).digest())


print(body,type(body),body1)
print(co,type(co),co1)

print(bo,type(bo),bo1)

print(boo,type(boo),boo1)
print(booo,type(booo),booo1)



