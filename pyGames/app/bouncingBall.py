# -*- coding: utf-8 -*-

"""
@project: pyGames
@author: YangYang_y00343969
@file: bouncingBall.py
@ide: PyCharm
@time: 2019/2/16 10:33
"""
import sys
import pygame


pygame.init()

size = width, height = 640, 420
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load(r"D:\Software\Python\pyProjects\pyGames\images\intro_ball.gif")
ballrect = ball.get_rect()
print(ballrect)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
