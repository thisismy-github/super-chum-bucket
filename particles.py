import pygame as pg
from layer import Layer
from random import randint, uniform, getrandbits

class Particle:
    def __init__(self, x, y, length, width, yspeed, xspeed, color, ):
        self.x = x
        self.y = y
        self.l = length
        self.w = width
        self.yspeed = yspeed
        self.xspeed = xspeed
        self.color = color

    def freeze(self):
        self.yspeed = 0
        self.xspeed = 0


class Rain(Layer):
    def __init__(self, xBounds, yBounds, lBounds, wBounds, sBounds, color, windSpeed=0):
        super().__init__()
        self.droplets = []
        self.frozenDroplets = {}
        self.xBounds = xBounds
        self.yBounds = yBounds
        self.lBounds = lBounds
        self.wBounds = wBounds
        self.sBounds = sBounds
        self.color = color          # change
        self.windSpeed = round(windSpeed, 1)
        self.targetWindSpeed = self.windSpeed
        self.windUpdateSpeed = 0.2

    def setWindSpeed(self, newSpeed, instant=False, speed=0.2):
        if not instant:
            self.targetWindSpeed = round(newSpeed, 1)
        else:
            self.windSpeed = round(newSpeed, 1)
            self.targetWindSpeed = self.windSpeed
        self.windUpdateSpeed = speed

    def freezeDroplet(self, droplet, now):
        droplet.freeze()
        droplet.color = (255,255,255)
        self.droplets.remove(droplet)
        self.frozenDroplets[now] = droplet

    def drop(self):
        self.droplets.append(Particle(randint(self.xBounds[0], self.xBounds[1]),
                                     randint(self.yBounds[0], self.yBounds[1]),
                                     randint(self.lBounds[0], self.lBounds[1]),
                                     randint(self.wBounds[0], self.wBounds[1]),
                                     randint(self.sBounds[0], self.sBounds[1]),
                                     self.windSpeed,
                                     self.color))

    def update(self, screen):
        self.drop()
        self.drop()
        #now = pg.time.get_ticks()
        #print(self.droplets[0].x, self.droplets[0].y, self.droplets[0].yspeed)
        for d in self.droplets:
            #pg.draw.line(screen, d.color, (d.x+self.windSpeed/3, d.y-d.l), (d.x, d.y), d.w)
            pg.draw.circle(screen, d.color, (int(d.x), d.y), d.w+randint(0,3))
            d.y+=randint(self.sBounds[0],self.sBounds[1])
            #d.y+=d.yspeed
            d.x-=uniform(self.windSpeed,self.windSpeed*2)
            d.x-=d.xspeed*10
            if d.y <= -20:
                self.droplets.remove(d)
            if d.x < -20:
                d.x = 1300
            elif d.x > 1300:
                d.x = -20

            #if (d.x > 435 and d.x < 845) and d.y > 207 and d.y < 212:
            #    d.y = 206
            #    self.freezeDroplet(d, now)

        #toDelete = []
        #for time, d in self.frozenDroplets.items():
        #    if now > time+3000:
        #        d.l -= 0.05
        #    if d.l <= 0:
        #        toDelete.append(time)
        #    pg.draw.line(screen, d.color, (d.x, d.y-d.l), (d.x, d.y), int(d.w))
        #for d in toDelete:
        #    del self.frozenDroplets[d]

        if self.windSpeed > self.targetWindSpeed:
            self.windSpeed -= self.windUpdateSpeed
            if self.windSpeed < self.targetWindSpeed:
                self.windSpeed = self.targetWindSpeed
        elif self.windSpeed < self.targetWindSpeed:
            self.windSpeed += self.windUpdateSpeed
            if self.windSpeed > self.targetWindSpeed:
                self.windSpeed = self.targetWindSpeed


class Snow(Layer):
    def __init__(self):
        pass