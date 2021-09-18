from constants import *
from helpers import *
from utilities import *
import pygame as pg
import sched, time

score = 1

Snake_d = dict()
Snake_d[(0,0)] = True

Snake_a = [(0,0)]

tail_shadow = (1,0)

direction = up

food = generateFood(Snake_d, Snake_a)

GD = GameData(Snake_d, Snake_a, tail_shadow, direction, food, score)

colorBox((0,0), blue)
updateScoreboard("Snake Game + ", GD.score)


done = False
counter = 0
interval = 10
while(not(done)):
    time.sleep(.1/interval)
    counter += 1
    if (counter % interval == 0):
        GDalias = GD
        GD = moveSnake(GD)
        if (GD == None):
            done = True
            GameOver(GDalias)
        


    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if (event.key == pg.K_UP and GD.dir != down): #want to avoid backing into themselves
                GD.dir = up
            elif (event.key == pg.K_DOWN and GD.dir != up):
                GD.dir = down
            elif (event.key == pg.K_LEFT and GD.dir != right):
                GD.dir = left
            elif (event.key == pg.K_RIGHT and GD.dir != left):
                GD.dir = right
    
    pg.display.flip()
        
