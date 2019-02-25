# -*- coding: utf-8 -*-

"""
@project: webserviceTest
@author: YangYang_y00343969
@file: urllibTest.py
@ide: PyCharm
@time: 2019/2/14 16:11
"""
# -*- coding: utf-8 -*-
import http.client


def mdsmssend():
    # 定义发送报文
    SoapMessage = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://schemas.xmlsoap.org/soap/encoding/" xmlns:ns2="rm:soap" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
        <SOAP-ENV:Header/>
        <ns0:Body>
            <ns2:getSubscriberAllInf>
                <inPara>
                    <subscriber>
                        <attribute>
                            <key>usrIdentifier</key>
                            <value>4000080061332</value>
                        </attribute>
                    </subscriber>
                </inPara>
            </ns2:getSubscriberAllInf>
        </ns0:Body>
    </SOAP-ENV:Envelope>
    '''
    # SoapMessage = SoapMessage % (sn, pwd, mobile, context)
    # 使用的WebService地址为sdk.entinfo.cn:8061/webservice.asmx，
    # webservice = http.client.HTTP("10.148.55.34:8080")
    webservice = http.client.HTTPConnection("127.0.0.1", 8081)
    webservice.connect()
    # 连接到服务器后的第一个调用。它发送由request字符串到到服务器
    # webservice.putrequest("POST", "/ScfPccSoapServiceEndpointPort")
    # webservice.putheader("Host", "10.148.55.34:8080")
    # webservice.putheader("Host", "127.0.0.1:8081")
    # webservice.putheader("User-Agent", "Apache-HttpClient/4.1.1 (java 1.5)")
    # webservice.putheader("Content-type", "text/xml;charset=UTF-8")
    # webservice.putheader("Content-length", "%d" % len(SoapMessage))
    # webservice.putheader("SOAPAction", "getSubscriberAllInf")
    headerdata = {"SOAPAction", "getSubscriberAllInf"}
    # 发送空行到服务器，指示header的结束
    # webservice.endheaders()
    # 发送报文数据到服务器

    # webservice.send(str.encode(SoapMessage))
    webservice.request(method='POST', url='/ScfPccSoapServiceEndpointPort', body=SoapMessage)
    # 获取返回HTTP 响应信息
    response = webservice.getresponse()
    return response


if __name__ == '__main__':
    print(mdsmssend().status)
    print(mdsmssend().msg)
    print(mdsmssend().headers)
