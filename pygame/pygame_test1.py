# 在pygame中，导入和初始化是一个非常简单的过程。有多简单呢？

import pygame
import sys
pygame.init()

screen = pygame.display.set_mode([1600, 900])

screen.fill([255, 255, 255])

jpgFilePath = './../images/background.jpg'

imgRect = pygame.image.load(jpgFilePath)

screen.blit(imgRect, [0, 0])
# flip函数将重新绘制整个屏幕对应的窗口。
pygame.display.flip()
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
            pygame.quit()
