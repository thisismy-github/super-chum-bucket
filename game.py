import pygame as pg

class Game:
    def __init__(self, screen, clock):
        self.activeScene = None
        self.screen = screen
        self.clock = clock
        self.fadeScreen = pg.Surface((1280,720))
        self.fadeColor = pg.Color(0,0,0)

    def setActiveMenu(self,menu):
        self.activeScene = menu

    def fadeOut(self,speed=1,hold=0):
        for i in range(1,int(256/speed)):
            self.activeScene.update(self.screen)
            self.fadeScreen.fill(self.fadeColor)
            self.fadeScreen.set_alpha(i*speed)
            self.screen.blit(self.fadeScreen,(0,0))
            self.clock.tick(60)
            pg.display.flip()
        if hold > 1:
            self.fadeScreen.set_alpha(255)
            for i in range(1, hold):
                self.activeScene.update(self.screen)
                self.fadeScreen.fill(self.fadeColor)
                self.screen.blit(self.fadeScreen,(0,0))
                self.clock.tick(60)
                pg.display.flip()

    def fadeIn(self,speed=1,hold=0):
        if hold > 1:
            self.fadeScreen.set_alpha(255)
            for i in range(1, hold):
                self.activeScene.update(self.screen)
                self.fadeScreen.fill(self.fadeColor)
                self.screen.blit(self.fadeScreen,(0,0))
                self.clock.tick(60)
                pg.display.flip()
        for i in range(1,int(256/speed)):
            self.activeScene.update(self.screen)
            self.fadeScreen.fill(self.fadeColor)
            self.fadeScreen.set_alpha(256-i*speed)
            self.screen.blit(self.fadeScreen,(0,0))
            self.clock.tick(60)
            pg.display.flip()