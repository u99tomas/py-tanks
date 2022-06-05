from src.scenarios.scenery import Scenery
from ..stages.stage import Stage
from src.game_entities.tank import Tank
from src import constants as consts



class SandScenery(Scenery):

    def __init__(self, sprite_sheet):
        super().__init__(sprite_sheet)

        # Stages
        sand = Stage(consts.SAND_STAGE)
        oils = Stage(consts.OILS_STAGE)
        trees = Stage(consts.TREES_STAGE)

        # Game entities
        tank_image = sprite_sheet.get('tankBeige')
        tank = Tank(tank_image)

        self.add(sand)
        self.add(oils)
        self.add(tank)
        self.add(trees)
