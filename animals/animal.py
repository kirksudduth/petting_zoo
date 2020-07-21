from datetime import date


class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food
        self.__chip_number = chip_num

    @property
    def chip_number(self):
        try:
            return self.__chip_number
        except AttributeError:
            return 0

    @chip_number.setter
    def chip_number(self, new_chip_number):
        if type(new_chip_number) is int:
            self.__chip_number = new_chip_number
        else:
            raise TypeError("Please provide a whole integer.")

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f'{self.name} is a {self.species}.'
