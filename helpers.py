from constants import *
from utilities import *
import random

class GameData:
    def __init__(self, dic, arr, shadow, dir, food, score):
        self.dic = dic
        self.arr = arr
        self.shadow = shadow
        self.dir = dir
        self.food = food
        self.score = 0

def updateScoreboard(text, score):
    pg.draw.rect(screen, green, pg.Rect(0,0,900,100))
    pg.draw.rect(screen, white, pg.Rect(700, 10, 100, 80))

    font = pg.font.Font('freesansbold.ttf', 32) #get the desired font
    score_text = font.render("Score:", True, black, white) #get image of text from font
    screen.blit(score_text, (700,10)) #draws at the given location, top left as index
    count_text = font.render(str(score), True, black, white)
    screen.blit(count_text, (700,50))

    bigfont = pg.font.Font('freesansbold.ttf', 72) #get the desired font
    display_text = font.render(text, True, blue, green)
    screen.blit(display_text, (100, 30))

    pg.display.flip()

def generateFood(dic, arr):
    pantry = dict()
    if (len(arr) >= box*box):
        return None
    
    bites_remaining = 1
    if (random.randint(0,10) == 0):
        bites_remaining = 10

    while (bites_remaining > 0):
        P = (random.randint(0, n-1),random.randint(0, n-1))
        if (dic.get(P) == None and pantry.get(P) == None):
            colorBox(P, red)
            bites_remaining -= 1
            pantry[P] = True
    return pantry


def moveSnake(data):
    (h1,h2) = data.arr[len(data.arr)-1]
    (u,v) = data.dir
    tail = data.arr[0]
    new_head = (h1+u, h2+v)

    #check if we ate the new food
    if (data.food.get(new_head) != None):
        data.score += 1
        updateScoreboard("Snake Game+", data.score)
        data.arr.append(new_head)
        data.dic[new_head] = True
        colorBox(new_head, blue)
        data.food.pop(new_head)
        if (len(data.food) == 0):
            data.food = generateFood(data.dic, data.arr)
        if (data.food == None):
            GameOver(data)
        return data

    #did we exit the screen or run into ourselves?
    if (data.dic.get(new_head) != None or not(indexInRange(new_head))):
        return None
    
    ### Move the snake itself below###
    #edit array
    data.shadow = data.arr.pop(0)
    data.arr.append(new_head)
    #edit dict
    data.dic.pop(data.shadow)
    data.dic[new_head] = True
    #color appropriately
    colorBox(new_head, blue)
    colorBox(data.shadow, black)

    
    return data


def GameOver(data):
    updateScoreboard("GAMEOVER!", data.score)
    quit = False
    while(not(quit)):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit = True


