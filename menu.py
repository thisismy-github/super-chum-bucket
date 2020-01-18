import pygame as pg
from menuitem import MenuItem
import graphic
import sound
import settings
from scene import Scene

class Menu(Scene):
    def __init__(self, menuItems, actions=None, mouseEnabled=True, keyboardEnabled=True,
                 bgcolor=(0,0,0), bgimage=None, bgassets=None, hlType=-1, hlIcon=None,
                 useHints=False, hintText=None, hintFont=None, hintPos=(0,0)):
        '''
        args:
            hlType -> number 0-2 representing highlight type.
                      0=icon next to item, 1=item changes colors, 2=both
            hlIcon -> icon image to be used for hlTypes 1 and 2.
            hlIconPos -> coordinate pair for position of icon to be used for hlTypes 1 and 2.
            useHints -> bool to determine whether or not hints (tooltips) will be displayed.
            hintPos -> coordinate pair for position of currently or globally displayed hint.
        '''
        super().__init__()
        self.isOpen = False
        self.objects = [(item, item.pos) for item in menuItems]
        self.menuItems = menuItems
        self.itemRange = (1,len(menuItems))
        self.actions = actions
        self.selected = menuItems[0]
        self.mouseEnabled = mouseEnabled
        self.keyboardEnabled = keyboardEnabled

        self.bgcolor = bgcolor
        self.bgimage = bgimage
        self.bgassets = bgassets
        self.hlType = hlType
        self.hlIcon = hlIcon
        self.hlIconPos = (0,0)
        self.useHints = useHints
        self.hintText = hintText
        self.hintFont = hintFont
        self.hintPos = hintPos

    def open(self):
        self.isOpen = True
        return self

    def close(self):
        self.isOpen = False
        return None

    def switchMenus(self, newMenu):
        self.isOpen = False
        newMenu.isOpen = True
        return newMenu

    def setActions(self, actions):
        self.actions = actions

    def setHlIconPos(self):
        self.hlIconPos = self.selected.highlight(self.hlType, self.hlIcon, self.hlIconPos)

    def scale(self, image, size):
        return pg.transform.scale(image,size)

    def searchItem(self,itemid):
        #TODO unused
        for menuItem in self.menuItems:
            if menuItem.id == itemid:
                return menuItem

    def click(self,mpos=None,keyboard=False):
        if not keyboard:
            for menuItem in self.menuItems:
                if mpos and menuItem.unlocked and menuItem.rect.collidepoint(mpos):
                    self.actions(menuItem.click())
        else:
            self.actions(self.selected.click())

    def hover(self,mpos=None,clicking=False):
        for menuItem in self.menuItems:
            if mpos and menuItem.unlocked and menuItem.rect.collidepoint(mpos):
                self.hlIconPos = menuItem.highlight(self.hlType, self.hlIcon, self.hlIconPos, clicked=clicking)
            else:
                self.hlIconPos = menuItem.highlight(self.hlType, self.hlIcon, self.hlIconPos, on=False)

    def keyboardHover(self, direction):
        if direction == "down":
            if self.selected.id+1 > self.itemRange[1]:
                self.selected = self.menuItems[self.itemRange[0]-1]
            else:
                self.selected = self.menuItems[self.selected.id]
        elif direction == "up":
            if self.selected.id-1 < self.itemRange[0]:
                self.selected = self.menuItems[self.itemRange[1]-1]
            else:
                self.selected = self.menuItems[self.selected.id-2]
        self.hlIconPos = self.selected.highlight(self.hlType, self.hlIcon, self.hlIconPos)

    def processEvents(self, events):
        for e in events:
            if e.type == pg.QUIT:
                pg.quit()
                exit(0)
            if self.mouseEnabled and e.type == pg.MOUSEMOTION:
                #print(e.pos,e.buttons)
                self.hover(e.pos,bool(e.buttons[0]))
            if self.keyboardEnabled and e.type == pg.KEYDOWN:
                if e.key == pg.K_RETURN:
                    self.click(keyboard=True)
                if e.key == pg.K_UP:
                    self.keyboardHover("up")
                elif e.key == pg.K_DOWN:
                    self.keyboardHover("down")
                if e.key == pg.K_RIGHT:
                    #print(self.hlIconPos)
                    pass
                elif e.key == pg.K_LEFT:
                    pass
                if e.key == pg.K_PERIOD:
                    settings.VOLUME = min(1,settings.VOLUME+0.1)
                    print(settings.VOLUME)
                    pg.mixer.music.set_volume(settings.VOLUME)
                if e.key == pg.K_COMMA:
                    settings.VOLUME = max(0,settings.VOLUME-0.1)
                    print(settings.VOLUME)
                    pg.mixer.music.set_volume(settings.VOLUME)

            if e.type == pg.MOUSEBUTTONUP and e.button == 1:
                self.click(e.pos)

    def render(self, screen):
        screen.fill(self.bgcolor)
        if self.bgimage:
            # (1280/2)-(self.bgimage.get_rect().width/2) = 229.0
            screen.blit(self.bgimage, (229,0))
        if self.hlIcon:
            screen.blit(self.hlIcon, self.hlIconPos)
        for item in self.menuItems:
            if item.isText:
                item.font.render_to(screen, item.pos, item.text)
            else:
                screen.blit(item.image)

    def update(self, screen):
        self.render(screen)
        for layer in self.layers:
            layer.update(screen)


# GAME-SPECIFIC
#TODO
mmSinglePlayer = MenuItem(pos=(0.43*1280,0.395*720), itemid=1, text="1 PLAYER",
                          font=pg.freetype.Font(graphic.fontArcade, size=24),
                          hlSound=sound.menuSelect)
mmOnline = MenuItem(pos=(0.43*1280,0.465*720), itemid=2, text="ONLINE",
                          font=pg.freetype.Font(graphic.fontArcade, size=24),
                          hlSound=sound.menuSelect)
mmEditMode = MenuItem(pos=(0.43*1280,0.535*720), itemid=3, text="EDIT MODE",
                          font=pg.freetype.Font(graphic.fontArcade, size=24),
                          hlSound=sound.menuSelect)
mmOptions = MenuItem(pos=(0.43*1280,0.605*720), itemid=4, text="OPTIONS",
                          font=pg.freetype.Font(graphic.fontArcade, size=24),
                          hlSound=sound.menuSelect)

mainMenuItems = [mmSinglePlayer, mmOnline, mmEditMode, mmOptions]

mainMenu = Menu(menuItems=mainMenuItems, mouseEnabled=False,
                bgcolor=graphic.LODERUNNERBLUE, bgimage=graphic.menuBG,
                hlType=0, hlIcon=graphic.menuSelect)