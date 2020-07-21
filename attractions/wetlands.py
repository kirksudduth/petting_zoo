from attractions import Attraction


class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animal):
        try:
            if animal.swim_speed >= 0:
                self.animals.append(animal)
        except AttributeError:
            print(f'{animal.name} is not a water loving critter.')
