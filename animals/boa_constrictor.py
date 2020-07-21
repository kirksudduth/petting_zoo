from animals import Animal
from movements import Slithering


class Boa_constrictor(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        print(f'{self.name} the {self.species} was fed {self.food} while getting his scales lightly scraped.')
