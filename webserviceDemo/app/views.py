# -*- coding: utf-8 -*-

"""
@project: webserviceTest
@author: YangYang_y00343969
@file: views.py
@ide: PyCharm
@time: 2019/2/12 17:27
"""

from ladon.ladonizer import ladonize
from ladon.types.ladontype import LadonType


class Calculator(object):

    @ladonize(int, int, rtype=int)
    def add(self, a, b):
        return a + b

    @ladonize(int, int, rtype=int)
    def minus(self, a, b):
        return a - b


class MyService(object):

    @ladonize(int, rtype=int)
    def mytest(self, a):
        return a * a
