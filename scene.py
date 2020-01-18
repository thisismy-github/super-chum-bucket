import pygame as pg
from layer import Layer

class Scene:
    def __init__(self, windowCaption=None, windowIcon=None):
        # layer0: base layer -> CHUMBUCKETBLUE or sky texture
        # layer1 bottom background layer
        # layer2 middle background layer
        # layer3 top background layer
        # layer4 background game tiles
        # layer5 sprites
        # layer6 player
        # layer7 foreground game tiles (electricity?)
        # layer8 bottom foreground layer
        # layer9 middle foreground layer
        # layer10 top foreground layer
        # layer11 filter/shader
        # layer12 hud
        self.next = self
        self.layers = self.initLayers()
        self.windowCaption = windowCaption
        self.windowIcon = windowIcon

    def initLayers(self):
        return [Layer() for i in range(13)]

    def processEvents(self, events):
        raise NameError("Child class 'processEvents' not defined!")

    def render(self, screen):
        raise NameError("Child class 'render' not defined!")

    def update(self, screen):
        raise NameError("Child class 'update' not defined!")

    def switchScene(self, newScene):
        if self.next:
            #newScene.next = newScene
            self.next = newScene

    def closeScene(self):
        self.switchScene(None)