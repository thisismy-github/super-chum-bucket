import pygame as pg

class MenuItem:
    def __init__(self, pos, itemid, unlocked=True, hint=None, hlSound=None, slSound=None,
                 image=None, hlImage=None, slImage=None,
                 text=None, font=None, color=(255,255,255), hlColor=None, slColor=None):
        self.pos = pos
        self.id = itemid
        self.isText = bool(text)
        #self.highlighted = 1
        self.unlocked = unlocked
        self.hint = hint
        self.hlSound = hlSound
        self.slSound = slSound
        self.defaultImage = image
        self.image = image
        self.hlImage = hlImage
        self.slImage = slImage
        self.text = text
        self.font = font
        self.defaultColor = color
        self.hlColor = hlColor
        self.slColor = slColor
        if color and font:
            self.font.fgcolor = color
        self.rect = self.setRect()

    def setRect(self):
        if self.isText:
            rect = self.font.get_rect(self.text, size=self.font.size)
        else:
            rect = self.defaultImage.get_rect()
        rect.x, rect.y = self.pos
        return rect

    def click(self):
        if self.slSound:
            self.slSound.play()
        return self.id

    def highlight(self, hlType, icon=None, iconPos=None, on=True, clicked=False):
        # type -1 -> no highlighting whatsoever
        # type 0 -> move select icon to menu item
        # type 1 -> change color of menu item
        # type 2 -> both

        if on and self.hlSound:
            self.hlSound.play()

        if (hlType == 0 or hlType == 2) and on:
            iconPos = self.pos[0] - icon.get_rect().width*1.37, self.pos[1]-2
        if hlType == 1 or hlType == 2:
            if not clicked:
                if self.isText:
                    self.font.fgcolor = self.hlColor if on and self.hlColor else self.defaultColor
                else:
                    self.image = self.hlImage if on and self.hlImage else self.defaultImage
            else:
                if self.isText:
                    self.font.fgcolor = self.slColor if on and self.slColor else self.defaultColor
                else:
                    self.image = self.slImage if on and self.slImage else self.defaultImage
        return iconPos