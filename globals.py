#KEEPING THE CODE CLEAN, PUTTING THESE OBNOXIOUS DEFINITIONS HERE
import pygame as pg

width = 900
height = 900

black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
up = (0,1)
down = (0,-1)
left = (-1, 0)
right = (1, 0)

n = 30 #size of the board
box = height/n

pg.init()
screen = pg.display.set_mode((width, height+100))
screen.fill(black)