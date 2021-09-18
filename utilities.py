import pygame as pg
from constants import *

def getRect(x,y):
    top = height-(y*box+box)+100 #height/n is pixels per square
    left = x*box
    return pg.Rect(left, top, box, box)

def colorBox(point, color):
    (x,y) = point
    pg.draw.rect(screen, color, getRect(x,y))

def indexInRange(point):
    (x,y) = point
    if (x >= n or y >= n):
        return False
    if (x < 0 or y < 0):
        return False
    return True
