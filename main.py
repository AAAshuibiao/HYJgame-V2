import sys

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill((255, 255, 255))

    x, y = pygame.mouse.get_pos()

    pygame.draw.rect(screen, (255, 0, 0), (x-25, y-25, 50, 50))

    pygame.display.update()
