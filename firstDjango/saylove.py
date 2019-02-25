# -*- coding: utf-8 -*-

"""
@project: firstDjangoWeb
@author: YangYang_y00343969
@file: saylove.py
@ide: PyCharm
@time: 2019/2/9 16:08
"""
import datetime
from django.http import HttpResponse


def say_love(request):
    now = datetime.datetime.now()
    return HttpResponse('Time is %s, I just want to say: I love you, Gui Yali!' % now)
