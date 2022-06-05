from hashlib import new
import math
import pygame


class GameEntity:

    def __init__(self, image):
        self.x = 100
        self.y = 100
        self.image = image
        self.speed = 0.5
        self.speedX = 0
        self.speedY = 0

        size = self.image.get_size()
        self.width = size[0]
        self.height = size[1]
        self.mouse_movement = False
        self.last_mouse_event_tick = 0



    def draw(self, surface):
        #self.y = self.y - self.speedY
        #self.x = self.x - self.speedX
        #pos = (self.x, self.y)

        result = self.get_rotated_image()
        
        if not self.mouse_movement:
            new_pos = self.calculat_new_xy(result[2])
            self.x = new_pos[0]
            self.y = new_pos[1]

        surface.blit(result[0], result[1].topleft)
        
        time_now = pygame.time.get_ticks()
        if(time_now > self.last_mouse_event_tick + 10):
            self.mouse_movement = False
        

    def calculat_new_xy(self, angle_in_radians):
        new_x = self.x + (self.speed*math.cos(angle_in_radians))
        new_y = self.y + (self.speed*math.sin(angle_in_radians))
        return new_x, new_y

    def get_rotated_image(self):

        centerX = self.x + (self.width / 2)
        centerY = self.y + (self.height / 2)
        center = (centerX, centerY)
        player_rect = self.image.get_rect(center=center)
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - player_rect.centerx, my - player_rect.centery
        correction_angle = 90
        angle = math.degrees(math.atan2(-dy, dx)) - correction_angle

        rot_image = pygame.transform.rotate(self.image, angle)
        rot_image_rect = rot_image.get_rect(center=player_rect.center)
        return [rot_image, rot_image_rect, angle]

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

        if(event.type == pygame.MOUSEMOTION):
            self.mouse_movement = True
            self.last_mouse_event_tick = pygame.time.get_ticks()

            
            
