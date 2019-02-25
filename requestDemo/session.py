# -*- coding: utf-8 -*-

"""
@project: RequestDemo
@author: YangYang_y00343969
@file: session.py
@ide: PyCharm
@time: 2019/2/15 15:50
"""
import requests
geturl = 'http://127.0.0.1:8082/getDemo'

# 保留cookies
# s = requests.session()
# s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('https://httpbin.org/cookies')
# print(r.text)

# 利用Session向request传参数
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get(geturl, headers={'x-test2': 'true'})

# Note, however, that method-level parameters will not be persisted across requests, even if using a session.
s = requests.Session()
r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
print(type(r.cookies))
# '{"cookies": {"from-my": "browser"}}'
r = s.get('https://httpbin.org/cookies')
print(r.text)
# '{"cookies": {}}'


# Sessions can also be used as context managers:
with requests.Session() as s:
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# This will make sure the session is closed as soon as the with block is exited, even if unhandled exceptions occurred.
