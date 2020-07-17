import sys
import random
import pygame
from pygame.locals import *

pygame.init()

print("Game by SS and ZW: press the mouse button when color inside the square is closest to the rest")
pygame.time.wait(1000)

screen = pygame.display.set_mode((500, 500), 0, 32)


"""
class color_:
    def __init__(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.clr = (r,g,b)
"""

gayClock = pygame.time.Clock()


def returnColor():
    r,g,b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    return (r, g, b)

i = 0
c = returnColor()
d = returnColor()
mousePressed = False
try:
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                mousePressed = True
                totalDifference = abs(c[0]-d[0]) + abs(c[1]-d[1]) + abs(c[2]-d[2])
                score = 100 - (totalDifference // 5)
                print("Color of the background " + str(c) )
                print("Color of the square: " + str(d) )
                print("Your score is " + str(score) + " points out of 100" )

        if not mousePressed:
            i += 1
            x, y = pygame.mouse.get_pos()
        
        #print(c)

        screen.fill(c)

        

        pygame.draw.rect(screen, d, (x-25, y-25, 50, 50))
        if i > 30:
            i = 0
            c = returnColor()
            d = returnColor()
        pygame.display.update()

        gayClock.tick(60)
        
        


except SystemExit:
    pass


#class block:
#    def __init__(self):
#        pygame.draw.rect()

