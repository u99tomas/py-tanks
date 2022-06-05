

import pygame


class GameEntity:

    def __init__(self, image):
        self.x = 100
        self.y = 100
        self.image = image
        size = self.image.get_size()
        self.width = size[0]
        self.height = size[1]
        self.speed = 0.5
    
    def center(self):
        centerX = self.x + (self.width / 2)
        centerY = self.y + (self.height / 2)
        return (centerX, centerY)

    def draw(self, surface):
        self.time_now = pygame.time.get_ticks()
        

    def event(self, event):
        pass