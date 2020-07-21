from attractions import Attraction


class Snake_pit(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animal):
        try:
            if animal.slither_speed >= 0:
                self.animals.append(animal)
        except AttributeError:
            print(f'{animal.name} does not belong in No Feet Knoll.')
