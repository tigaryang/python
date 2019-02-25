# -*- coding: utf-8 -*-

"""
@project: webserviceTest
@author: YangYang_y00343969
@file: clientCall.py
@ide: PyCharm
@time: 2019/2/13 9:44
"""

from suds.client import Client


def call_my_service(url):
    client = Client(url)
    print(client.service.add(1, 2))
    print(type(client.html()))
    print(client.last_received())

    print(client.last_sent())


call_my_service('http://127.0.0.1:8088/mockMathUtilSoapBinding?wsdl')
