import pygame as pg
import random

class Player(pg.sprite.Sprite):
    def __init__(self, screen, lives=6):
        self.x, self.y = random.randint(20,1200), random.randint(50,200)
        self.spawnX, self.spawnY = 0,0

        self.vx, self.vy = 0,0
        self.thrustFactor = 0.1925
        self.thrustLeft = 0
        self.thrustRight = 0
        #self.thrustJump = 0
        self.maxRunThrust = 6
        #self.maxJumpThrust = 0.01
        self.maxRunSpeed = 2.695
        self.maxFallSpeed = 12
        self.pFriction = 0.7
        self.pGravity = 0.8

        self.facingRight = True
        self.onGround = True
        self.onLadder = False
        self.isHanging = False

        self.lives = lives
        self.screen = screen
        self.sprite = self.redraw2()

    def move(self):
        self.vx *= self.pFriction
        self.vx += (self.thrustLeft+self.thrustRight)*self.thrustFactor

        if not self.onGround and not self.isHanging:
            self.vy -= self.pGravity

        if self.vx > self.maxRunSpeed:
            self.vx = self.maxRunSpeed
        elif self.vx < -self.maxRunSpeed:
            self.vx = -self.maxRunSpeed
        if self.vy < -self.maxFallSpeed:
            self.vy = -self.maxFallSpeed

        if abs(self.vx) < 0.01:
            self.freezeX()
        if self.vy < 1 and self.vy > 0:
            # player is actively jumping and reaching the peak of their jump
            self.freezeY()
            self.isHanging = True
            pg.time.set_timer(pg.USEREVENT + 1, 220)

        self.x += self.vx
        if not self.isHanging:
            self.y -= self.vy

        if self.y > 640:
            self.y = 640
            self.onGround = True
            self.freezeY()

        if self.x > 1232:
            self.x = 1232
        elif self.x < 0:
            self.x = 0

    def jump(self):
        self.onGround = False
        self.vy = self.maxFallSpeed + 0.5

    def freeze(self):
        self.freezeX()
        self.freezeY()

    def freezeX(self):
        self.vx = 0

    def freezeY(self):
        self.vy = 0

    def getPos(self):
        return self.x, self.y

    def getVel(self):
        return self.vx, self.vy

    def spawn(self, facingRight=True):
        self.x = self.spawnX
        self.y = self.spawnY
        self.facingRight = facingRight

    def setSpawn(self, newSpawnX, newSpawnY):
        self.spawnX = newSpawnX
        self.spawnY = newSpawnY

    def kill(self):
        # PLACEHOLDER, NEEDS MORE CODE AND STUFF
        self.lives -= 1
        self.onGround = False
        if self.lives <= 0:
            self.gameover()
        else:
            self.spawn()

    def gameover(self):
        # PLACEHOLDER
        print("gameover")

    def render(self):
        # TEMPORARY
        pg.draw.rect(self.screen, (225,225,0), (self.x,self.y,48,80))
        pg.draw.rect(self.screen, (255,255,255), (0,624,96,48))        # height test 1
        pg.draw.rect(self.screen, (0,0,0), (0,672,96,48))              # height test 2

    def redraw2(self):
        return pg.draw.rect(self.screen, (225,225,0), (0,0,48,80))

class TestPlayer(Player):
    def __init__(self, screen, players):
        super().__init__(screen)
        self.players = players

    def move(self):
        for p in self.players:
            p.move()

    def jump(self):
        for p in self.players:
            p.jump()

    def freeze(self):
        for p in self.players:
            p.freeze()

    def freezeX(self):
        for p in self.players:
            p.freezeX()

    def freezeY(self):
        for p in self.players:
            p.freezeY()

    def spawn(self, facingRight=True):
        for p in self.players:
            p.spawn(facingRight)

    def setSpawn(self, newSpawnX, newSpawnY):
        for p in self.players:
            p.setSpawn(newSpawnX, newSpawnY)

    def kill(self):
        # PLACEHOLDER, NEEDS MORE CODE AND STUFF
        for p in self.players:
            p.kill()

    def gameover(self):
        # PLACEHOLDER
        for p in self.players:
            p.gameover()

    def render(self):
        # TEMPORARY
        for p in self.players:
            p.render()

