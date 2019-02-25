# -*- coding: utf-8 -*-

"""
@project: myLove
@author: YangYang_y00343969
@file: 2019.py
@ide: PyCharm
@time: 2019/2/14 7:03
"""

from PIL import Image


mw = 100
ms = 20

msize = mw * ms

# 选一张画布，关键确定画布大小
toImage = Image.new('RGB', (2000, 2000))

for y in range(1, 21):
    for x in range(1, 21):
        print(str(ms * (y - 1) + x))
        try:
            fromIamge = Image.open(r"D:/picture/1 (%s).jpg" % str(ms * (y - 1) + x))
            fromIamge = fromIamge.resize((100, 100), Image.ANTIALIAS)
            toImage.paste(fromIamge, ((x - 1) * mw, (y - 1) * mw))
        except IOError:
            pass

toImage.show()
toImage.save('D:/picture/love.png')
