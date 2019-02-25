# -*- coding: utf-8 -*-

"""
@project: webserviceTest
@author: YangYang_y00343969
@file: handler.py
@ide: PyCharm
@time: 2019/2/12 17:26
"""

from spyne import Application, rpc, ServiceBase
from spyne import Integer, Unicode, Array, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import sys


class SomeSampleServices(ServiceBase):

    @rpc(Unicode, Unicode_returns=Unicode)
    def make_project(self, name):
        pass


if __name__ == "__main__":
    soap_app = Application([SomeSampleServices],
                           'SampleServices',
                           in_protocol=Soap11(validator="lxml"),
                           out_protocol=Soap11())
    wsgi_app = WsgiApplication(soap_app)
    server = make_server('127.0.0.1', '8801', wsgi_app)

    sys.exit(server.serve_forever())
