import pygame as pg
import settings
import os

if settings.FULLSCREEN:
    screen = pg.display.set_mode((1280,720), pg.FULLSCREEN)
else:
    screen = pg.display.set_mode((1280,720))
pg.display.set_caption("bonnie's lode")

CHUMBUCKETBLUE = (0,20,152)
LODERUNNERBLUE = (14,66,255)

### Fonts
fontArcade = ("./graphics/ui/ARCADE_LODERUNNER.TTF")

# Main Menu
menuBG = pg.image.load("./graphics/ui/mainmenu.png".replace("/", os.sep)).convert()
menuSelect = pg.image.load("./graphics/ui/select.png".replace("/", os.sep))