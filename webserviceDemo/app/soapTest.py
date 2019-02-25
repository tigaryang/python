# -*- coding: utf-8 -*-

"""
@project: webserviceTest
@author: YangYang_y00343969
@file: ScfPccSoapServiceEndpointPort.py
@ide: PyCharm
@time: 2019/2/13 15:56
"""
from suds.client import Client, SoapClient, Method


# url后补充“?wsdl”
# url = 'http://10.148.55.34:8080/axis/services/ScfPccSoapServiceEndpointPort?wsdl'
url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'

# 设置报文头信息，SOAPAction必须的，否则报“Missing operation for soapAction”报错
headers1 = {'SOAPAction': 'http://WebXml.com.cn/getDatabaseInfo'}
# 建立客户端连接
client1 = Client(url, headers=headers1, faults=False, timeout=60)
print(client1)
client2 = Client(url, faults=False, timeout=60)
SOAPAction = 'SOAPAction'
action = 'http://WebXml.com.cn/getMobileCodeInfo'
client2.set_options(soapheaders=(SOAPAction, action))
print(client2)

# 复杂参数使用工厂来构造 Create的参数可以查看print(client)结果中对应接口的参数
# inPara = client2.factory.create('ns0:SInSubscriberAllInfParaVO')
# print(inPara)
# 参数设置可以参考print(inPara)中参数的路径和请求报文中的具体参数
# 在print(inPara)中我们可以看到参数有subscriber.attribute、subscriberService[]、subscriberQuota[]等，结合请求报文中attribute的具体内容进行设置
# inPara.subscriber.attribute = {
#     "key": "usrIdentifier",
#     "value": "4000080061332"
# }
#
# # 带参数调用具体接口
# res = client.service.getSubscriberAllInf(inPara)
res1 = client1.service.getDatabaseInfo()
print(res1[1])
res2 = client2.service.getMobileCodeInfo(13552028376)
print(res2[1])


