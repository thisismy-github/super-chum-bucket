import pygame as pg
import pygame.freetype
import pygame_functions as pgf
import settings
import menu
import sound
from graphic import *
from scene import Scene
from game import Game
from player import Player, TestPlayer
from chumbucket import ChumBucket
from particles import *
import random

pg.init()

pg.mixer.music.load(sound.titleTheme)
pg.mixer.music.play(loops=-1)
pg.mixer.music.set_volume(settings.VOLUME)


pFriction = 0.5
pGrav = 0.81
eVelCheck = pg.USEREVENT + 3
eWindFade = pg.USEREVENT + 4


clock = pg.time.Clock()
tics = pg.time.get_ticks()


eJumpHang = pg.USEREVENT + 1
ePlanktonAttack = pg.USEREVENT + 2
ePlanktonAttackInterval = 8000
pg.time.set_timer(ePlanktonAttack,ePlanktonAttackInterval)


# TEST VARIABLES
test = pg.USEREVENT + 5
pg.time.set_timer(test, 5000)
now = 0
then = 10000



sponge = Player(screen)
sponges = [Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen),Player(screen)]
spongeDimensions = sponge.sprite

spongeTestPlayer = TestPlayer(screen, sponges)

game = Game(screen, clock)
chumBucket = ChumBucket(screen, sponge)
def mainMenuActions(itemid):
    if itemid == 1:
        pg.mixer.music.stop()
        sound.startChoir.play()
        game.fadeOut(speed=1.5, hold=120)
        game.activeScene.switchScene(chumBucket)
        game.activeScene = game.activeScene.next
        game.fadeIn(speed=8)
    elif itemid == 2:
        pass
    elif itemid == 3:
        pass
    elif itemid == 4:
        pass

game.setActiveMenu(menu.mainMenu.open())
game.activeScene.setActions(mainMenuActions)
game.activeScene.bgimage = game.activeScene.scale(game.activeScene.bgimage, (int(256*3.2142857),720))
if game.activeScene.hlIcon:
    game.activeScene.hlIcon = game.activeScene.scale(game.activeScene.hlIcon,(24,24))
game.activeScene.setHlIconPos()
#game.fadeIn(2, 120)

game.activeScene.layers[1] = Rain((-5,1350),(1300,1300),(5,5),(2,4),(-7,-2),(200,200,200), windSpeed=1)


while True:
    events = pg.event.get()
    for e in events:
        if e.type == pg.QUIT:
            pg.quit()
            exit(0)

        if e.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_ESCAPE]:
                pg.quit()
                exit(0)
            elif keys[pg.K_LALT] and keys[pg.K_RETURN]:
                settings.FULLSCREEN = not settings.FULLSCREEN
                if settings.FULLSCREEN:
                    screen = pg.display.set_mode((1280,720), pg.FULLSCREEN)
                else:
                    screen = pg.display.set_mode((1280,720))
            if keys[pg.K_l]:
                game.activeScene.layers[1].setWindSpeed(100, speed=0.5)
            if keys[pg.K_k]:
                game.activeScene.layers[1].setWindSpeed(1, speed=0.1)
            if keys[pg.K_j]:
                game.activeScene.layers[1].setWindSpeed(0, speed=0.2)
            if keys[pg.K_h]:
                game.activeScene.layers[1].setWindSpeed(-15, speed=0.5)
            if keys[pg.K_g]:
                then = tics + 3000
        if e.type == test:
            #print(sponge.getVel(), sponge.getPos())
            print(clock.get_fps())

        if e.type == eJumpHang:
            game.activeScene.player.isHanging = False
            pg.time.set_timer(eJumpHang, 0)


    game.activeScene.processEvents(events)
    game.activeScene.update(screen)
    game.activeScene = game.activeScene.next




    pg.display.flip()
    clock.tick(60)
    tics = pg.time.get_ticks()

