import pygame as pg
import graphic
import settings
from scene import Scene

class ChumBucket(Scene):
    def __init__(self, screen, player, levelPack=0, level=1, difficulty=0, lives=None):
        super().__init__()
        self.screen = screen
        self.player = player
        self.levelPack = 0
        self.level = 0
        self.difficulty = difficulty
        self.lives = lives if lives else 6-(self.difficulty*2)

    def processEvents(self, events):

        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == settings.JUMP and self.player.onGround:
                    self.player.jump()
                if e.key == settings.LEFT:
                    self.player.thrustLeft = -self.player.maxRunThrust
                if e.key == settings.RIGHT:
                    self.player.thrustRight = self.player.maxRunThrust

                if e.key == settings.UP:
                    self.player.setSpawn(50,50)
                    self.player.kill()
                    self.player.onGround = False
                if e.key == settings.DOWN:
                    self.player.onGround = True
                    self.player.freeze()

                if e.key == pg.K_PERIOD:
                    settings.VOLUME = min(1,settings.VOLUME+0.1)
                    print(settings.VOLUME)
                    pg.mixer.music.set_volume(settings.VOLUME)
                if e.key == pg.K_COMMA:
                    settings.VOLUME = max(0,settings.VOLUME-0.1)
                    print(settings.VOLUME)
                    pg.mixer.music.set_volume(settings.VOLUME)

            if e.type == pg.KEYUP:
                if e.key == settings.LEFT:
                    self.player.thrustLeft = 0
                if e.key == settings.RIGHT:
                    self.player.thrustRight = 0
                if e.key == settings.JUMP and self.player.vy > 1:
                    self.player.vy *= 0.5

    def render(self, screen):
        screen.fill(graphic.CHUMBUCKETBLUE)
        #self.screen.blit(self.player.sprite, self.player.getPos())
        self.player.render()

    def update(self, screen):
        self.player.move()
        self.render(screen)
