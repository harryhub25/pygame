import pygame, sys, random
import os
import math
import pygame.mixer
from pygame.locals import *

#3rd Edit

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
grey = 100, 100, 100
color = grey
yellow = 255,255,0

CAN_W = 400
CAN_H = 500
craft_w = 30
craft_h = 30

MOVE     = 20
UFO_MOVE =  5

canvas_size = (CAN_W, CAN_H)

# Initialize the game engine
pygame.init()

screen = pygame.display.set_mode(canvas_size)
pygame.display.set_caption("Tetris Coding")
clock = pygame.time.Clock()

class aircraft:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.life = True
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
    def drop(self):
        if self.life:
            self.y += UFO_MOVE
            if self.y >= CAN_H:
                self.life = False
            else:
                pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        else:
            i = random.randint(1,500)
            if i==1:
                self.life = True
                self.y = 0

class missile:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = 10
        self.h = 10
        self.color = white
        self.speed = 5;
    def shoot(self):
        self.y -= self.speed
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

me = aircraft(300, 300, craft_w, craft_h, blue)
ufo = []
for i in range(5):
    r=random.randint(1, CAN_W-craft_w)
    ufo.append(aircraft(r, 30, craft_w, craft_h, red))
mis = []

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_SPACE]:
            mis.append(missile(me.x, me.y, 10, 10, white))

        if keys[pygame.K_RIGHT]:
            me.x += MOVE
            if((me.x + craft_w) >= CAN_W):
                me.x = CAN_W - craft_w
        if keys[pygame.K_LEFT]:
            me.x -= MOVE
            if(me.x <= 0):
                me.x = 0
        if keys[pygame.K_UP]:
            me.y -= MOVE
            if(me.y <= 0):
                me.y = 0
        if keys[pygame.K_DOWN]:
            me.y += MOVE
            if((me.y + craft_h) >= CAN_H):
                me.y = CAN_H - craft_h



        screen.fill(black)
        me.draw()
        for xxx in ufo:
            xxx.drop()

        for yyy in mis:
            yyy.shoot()

        pygame.display.update()
        clock.tick(60)

"""

        

        pos_x=250
        pos_y=250
        radius=50

        screen.fill(yellow)
        pygame.draw.rect(screen, green, (x, y, 100, 100))
        pygame.draw.rect(screen, green, (150, 150, 100, 100),25)
        pygame.draw.circle(screen, green,  (pos_x, pos_y), radius, 0)

        if color is red:
            color = grey
        else:
            color = red
        pygame.display.update()
        clock.tick(60)
        #pygame.display.flip()
"""
