class Petting_zoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "all the animals you could possibly want to pet"
        self.animals = list()

    def Add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'


class Snake_pit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "legs are overrated -- come hang out with these smiling slitherers"
        self.animals = list()
    
    def Add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'

class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "gotta love the water -- these critters do"
        self.animals = list()
    
    def Add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'
        

