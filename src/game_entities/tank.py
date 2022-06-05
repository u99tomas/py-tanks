import pygame
from src.game_entities.game_entity import GameEntity


class Tank(GameEntity):

    def __init__(self, image):
        super().__init__(image)

    def event(self, event):
        super().event(event)

        if(event.type == pygame.KEYDOWN):

            if(event.key == pygame.K_UP):
                self.up()

            if(event.key == pygame.K_DOWN):
                self.down()

            if(event.key == pygame.K_LEFT):
                self.left()

            if(event.key == pygame.K_RIGHT):
                self.right()
