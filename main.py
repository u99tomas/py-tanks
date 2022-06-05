import sys
import pygame
from src.sprites.sprite_sheet import SpriteSheet
from src import constants as consts
from src.game_entities import *
from src.scenarios.sand_scenery import SandScenery
pygame.init()

size = width, height = 800, 600
surface = pygame.display.set_mode(size)

sprite_sheet = SpriteSheet(consts.XML_SHEET, consts.SPRITE_SHEET)
sand_scenery = SandScenery(sprite_sheet)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            sand_scenery.notifyEvent(event)

    sand_scenery.draw(surface)

    pygame.display.flip()
