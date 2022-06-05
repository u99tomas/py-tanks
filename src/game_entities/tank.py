import pygame
from src.game_entities.game_entity import GameEntity
import math
import pygame


class Tank(GameEntity):

    def __init__(self, image):
        super().__init__(image)

        self.can_move = True
        self.last_mouse_event_tick = 0

    def draw(self, surface):
        super().draw(surface)

        result = self.get_rotated_image()

        if self.can_move:
            new_pos = self.calculat_new_xy(result[2])
            self.x = new_pos[0]
            self.y = new_pos[1]

        surface.blit(result[0], result[1].topleft)


        if(self.time_now > self.last_mouse_event_tick + 5):
            self.can_move = True

    def calculat_new_xy(self, angle_in_radians):
        new_x = self.x + (self.speed*math.cos(angle_in_radians))
        new_y = self.y + (self.speed*math.sin(angle_in_radians))
        return new_x, new_y

    def get_rotated_image(self):
        tank_rect = self.image.get_rect(center=self.center())
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - tank_rect.centerx, my - tank_rect.centery
        correction_angle = 90
        angle = math.degrees(math.atan2(-dy, dx)) - correction_angle

        rot_image = pygame.transform.rotate(self.image, angle)
        rot_image_rect = rot_image.get_rect(center=tank_rect.center)
        return [rot_image, rot_image_rect, angle]

    def event(self, event):

        if(event.type == pygame.MOUSEMOTION):
            self.can_move = False
            self.last_mouse_event_tick = pygame.time.get_ticks()
