from animals import Animal
from movements import Walking


class Donkey(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def feed(self):
        print(
            f'{self.name} the {self.species} was fed {self.food} while watching Matlock.')
