# -*- coding: utf-8 -*-

"""
@project: RequestDemo
@author: YangYang_y00343969
@file: Prepared Requests.py
@ide: PyCharm
@time: 2019/2/15 17:02
"""

from requests import Request, Session

s = Session()
url = 'http://127.0.0.1:8082/postDemo'

req = Request('POST', url)
# prepare_request()可以应用到session级别的数据，所以推荐用
prepped = s.prepare_request(req)
# prepped = req.prepare()

# do something with prepped.body
prepped.body = "No, I want exactly this as the body"

# do something with prepped.headers
prepped.headers['new'] = 'new'

resp = s.send(prepped)

print(resp.status_code)
print(resp.headers)
print(resp.request.headers)
print(resp.request.body)


# 直接使用环境变量可能会报错，使用如下方式merge_environment_settings把环境变量merge到session中
s = Session()
geturl = 'http://127.0.0.1:8082/getDemo'
req = Request('GET', geturl)

prepped = s.prepare_request(req)

# Merge environment settings into session
settings = s.merge_environment_settings(prepped.url, None, None, None, None)
resp = s.send(prepped, **settings)

print(resp.status_code)
print(resp.request.body)
print(resp.request.headers)