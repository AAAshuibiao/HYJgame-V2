import sys
import random

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)


"""
class color_:
    def __init__(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.clr = (r,g,b)
"""


def returnColor():
    r,g,b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    return (r, g, b)

i = 0
c = returnColor()
d = returnColor()
try:
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                print("No u")

        i += 1
        
        #print(c)

        screen.fill(c)

        x, y = pygame.mouse.get_pos()

        pygame.draw.rect(screen, d, (x-25, y-25, 50, 50))
        if i > 1000:
            i = 0
            c = returnColor()
            d = returnColor()
        pygame.display.update()
        
        


except SystemExit:
    pass


#class block:
#    def __init__(self):
#        pygame.draw.rect()

