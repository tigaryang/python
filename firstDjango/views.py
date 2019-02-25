# -*- coding: utf-8 -*-

"""
@project: firstDjangoWeb
@author: YangYang_y00343969
@file: views.py
@ide: PyCharm
@time: 2019/2/9 15:56
"""

import datetime
from django.http import HttpResponse


def sayhello(request):
    now = datetime.datetime.now()
    return HttpResponse('Hello World! %s' % now)
