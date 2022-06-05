from src import game_entities
from src.game_entities.game_entity import GameEntity
from src.stages.stage import Stage


class Scenery:

    def __init__(self, sprite_sheet):
        self.sprite_sheet = sprite_sheet
        self.objects = []

    def draw(self, surface):
        for obj in self.objects:
            if(type(obj) is Stage):
                obj.draw(surface, self.sprite_sheet)
            elif(issubclass(type(obj), GameEntity)):
                obj.draw(surface)

    def notifyEvent(self, event):
        for obj in self.objects:
            if(issubclass(type(obj), GameEntity)):
                obj.event(event)

    def add(self, obj):
        self.objects.append(obj)
