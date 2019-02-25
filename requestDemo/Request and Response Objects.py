# -*- coding: utf-8 -*-

"""
@project: RequestDemo
@author: YangYang_y00343969
@file: Request and Response Objects.py
@ide: PyCharm
@time: 2019/2/15 16:50
"""

import requests
r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
print(r.headers)
print(r.request.headers)