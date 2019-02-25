# -*- coding: utf-8 -*-

"""
@project: RequestDemo
@author: YangYang_y00343969
@file: request_demo.py
@ide: PyCharm
@time: 2019/2/14 19:44
"""
# 文档地址：http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
import requests
from requests import  HTTPError

# r = requests.post('https://httpbin.org/post', data={'key': 'value'})

# r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')
url = 'http://127.0.0.1:8082/getDemo'
payload = {'key': 'value', 'key1': 'value1'}
r = requests.get(url, params=payload)

print(r.url)

# 查看返回报文
print(r.text)

# 查看并修改coding
print(r.encoding)
r.encoding = 'ISO-8859-1'
print(r.encoding)

# You can also access the response body as bytes, for non-text requests
print(r.content)

# 用接口返回值创建一个图片,代码有问题
# from PIL import Image
# from io import BytesIO
#
# i = Image.open(BytesIO(r.content))
# i.show()

# 处理Json
print(r.json())

# 查看接口调用返回码
print(r.status_code)
print(requests.codes.ok)
# 请求返回异常可以用raise_for_status()获取，接口正常返回200时，这个函数返回None
bad_url = url + '/404'

try:
    bad_r = requests.get('https://httpbin.org/status/404')
    print(bad_r.raise_for_status())
except HTTPError as e:
    print("There is an Error: %s " % e)
    print(bad_r.status_code)
    # raise


#  get the raw socket response from the server
r = requests.get(url, stream=True)
print(r.raw)
print(r.raw.read(10))

# 自定义报文头
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)


# post请求
post_url = 'http://127.0.0.1:8082/postDemo'
postdata = {'key': 'value', 'key1': 'value1'}
r = requests.post(post_url, data=postdata)
print(r.content)

payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post(post_url, data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post(post_url, data=payload_dict)
print(r1.text == r2.text)


# 传json数据
import json

# url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r1 = requests.post(post_url, data=json.dumps(payload))

r2 = requests.post(post_url, json=payload)
print(r1.text == r2.text)


# 报文头,对名称大小写不敏感
print(r.headers)
print(r.headers.get('Content-Type'))
print(r.headers['content-Type'])

# Cookies

url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
# 报错 KeyError: "name='example_cookie_name', domain=None, path=None"
print(r.cookies)

# 设置Cookies
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
print(r.text)
print(r.cookies.keys())
print(r.cookies.iterkeys())
print(r.cookies.itervalues())
print(r.cookies.values())
print(r.cookies.iteritems())
print(r.cookies.items())
print(r.cookies.list_domains())
print(r.cookies.list_paths())
print(r.cookies.multiple_domains())
print(r.cookies.get_dict())

# Redirection and History
r = requests.get('http://github.com/')
print(r.url)
print(r.status_code)
# 显示重定向的历史响应
print(r.history)
#   If you’re using GET, OPTIONS, POST, PUT, PATCH or DELETE,
# you can disable redirection handling with the allow_redirects parameter
r = requests.get('http://github.com/', allow_redirects=False)
print(r.status_code)
print(r.history)
# If you’re using HEAD, you can enable redirection as well: Head don't allow redirection default.
r = requests.head('http://github.com/', allow_redirects=True)
print(r.url)
print(r.history)


# Timeout
# r = requests.get('https://github.com/', timeout=0.001)

# 异常可用以下这个对象raise
try:
    r = requests.get('https://github.com/', timeout=0.001)
except requests.exceptions.RequestException as e:
    print(e)
    # raise
