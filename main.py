import sys
import random

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)

class color_:
    def __init__(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.clr = (r,g,b) 

def returnColor():
    r,g,b = random.randint(0,256), random.randint(0,256), random.randint(0,256)


try:

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                print("No u")

        screen.fill(color_A.clr)

        x, y = pygame.mouse.get_pos()


        pygame.display.update()


except SystemExit:
    pass





#class block:
#    def __init__(self):
#        pygame.draw.rect()

        
