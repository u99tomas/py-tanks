import xml.etree.ElementTree as ET
import pygame
from .image import Image
from ..constants import RESOURCES_PATH


class SpriteSheet:

    def __init__(self, xml_sheet, resource_name):
        sheet_path = f'{RESOURCES_PATH}/{resource_name}.png'
        self.sheet = pygame.image.load(sheet_path).convert()
        self.xml_sheet = f'{RESOURCES_PATH}/{xml_sheet}.xml'
        self.images = self.get_images()

    def get_surface(self, rectangle):
        rect = pygame.Rect(rectangle)
        surface = pygame.Surface(rect.size).convert()
        surface.blit(self.sheet, (0, 0), rect)
        surface.set_colorkey((0, 0, 0))

        return surface

    def get_images(self):
        tree = ET.parse(self.xml_sheet)
        root = tree.getroot()
        images = [self.get_image(child.attrib) for child in root]
        return images

    def get_image(self, attrib):
        name = attrib['name']
        x = int(attrib['x'])
        y = int(attrib['y'])
        width = int(attrib['width'])
        height = int(attrib['height'])

        rect = (x, y, width, height)
        surface = self.get_surface(rect)

        return Image(name, surface)

    def get(self, image_name):
        for image in self.images:
            if image.name == image_name:
                return image.surface