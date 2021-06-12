import os, sys, array
import pygame as pg
from pygame.locals import *

if not pg.font: print('Warning, fonts disabled')
if not pg.mixer: print('Warning, sound disabled')

pg.init()

#Create basic parameters
#Width = left => right
#Height = top => bottom
size = width, height = 650, 450
offwhite = 250, 250, 250
sqSize = 50
bWidth = width // sqSize
bHeight = height // sqSize
bGrid = [[0] * bWidth] * bHeight

#Create window
screen = pg.display.set_mode(size)


def getGridPos(pos):
    pos = ((pos[0] // sqSize), (pos[1] // sqSize))
    print(pos)
    print(bGrid[pos[1]][pos[0]])
    return pos

    

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            pos = getGridPos(pos)
            



    screen.fill(offwhite)
    pg.display.flip()

