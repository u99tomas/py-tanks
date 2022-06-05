import pygame


class GameEntity:

    def __init__(self, image):
        self.x = 100
        self.y = 100
        self.image = image
        self.speed = 0.2
        self.speedX = 0
        self.speedY = 0

    def draw(self, surface):
        self.y = self.y - self.speedY
        self.x = self.x - self.speedX
        pos = (self.x, self.y)

        surface.blit(self.image, pos)
           
    def up(self):
        self.speedY = self.speed
        self.speedX = 0

    def down(self):
        self.speedY = self.speed * -1
        self.speedX = 0

    def left(self):
        self.speedX = self.speed
        self.speedY = 0

    def right(self):
        self.speedX = self.speed * -1
        self.speedY = 0

    def event(self, event):
        pass