from attractions import Attraction


class Petting_zoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animal):
        try:
            if animal.walk_speed >= 0:
                self.animals.append(animal)
        except AttributeError:
            print(f'{animal.name} doesn\'t enjoy being touched and petted.')
