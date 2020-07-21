from animals import Animal
from movements import Slithering


class King_cobra(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
