from animals import Animal
from movements import Swimming, Walking


class Platypus(Animal, Swimming, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def feed(self):
        print(f'{self.name} the {self.species} was fed {self.food} while listening to lectures on self-improvement.')
