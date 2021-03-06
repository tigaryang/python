# -*- coding: utf-8 -*-

"""
@project: wehat
@author: YangYang_y00343969
@file: sendfile.py
@ide: PyCharm
@time: 2019/2/24 11:02
"""
from threading import Timer
from wxpy import *
import requests

bot = Bot()  # 连接微信,会出现一个登陆微信的二维码


def get_news():
    '''获取金山词霸每日一句'''
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_news():
    try:
        # contents = get_news()
        my_friend = bot.friends().search(u'雅丽')[0]  # 这里是你微信好友的昵称
        my_friend.send(u'How is your day?')
        my_friend.send(u'Python send message automatically')
        t = Timer(86400, send_news)  # 这里是一天发送一次，86400s = 24h

        t.start()

    except:
        my_friend = bot.friends().search('咩')[0]  # 这里是你的微信昵称
        my_friend.send(u'今天消息发送失败了')


if __name__ == '__main__':
    send_news()
