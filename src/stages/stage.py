import xml.etree.ElementTree as ET
from ..constants import STAGE_PATH


class Stage:

    def __init__(self, stage_name):
        tree = ET.parse(f'{STAGE_PATH}/{stage_name}.xml')
        self.root = tree.getroot()

    def draw(self, surface, sprite_sheet):
        for child in self.root:
            name = child.attrib['name']
            x = int(child.attrib['x'])
            y = int(child.attrib['y'])
            image = sprite_sheet.get(name)
            surface.blit(image, (x, y))
