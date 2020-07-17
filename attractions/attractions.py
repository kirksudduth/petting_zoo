class Petting_zoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "all the animals you could possibly want to pet"
        self.animals = list()

    def Add_animal(self, animal):
        self.animals.append(animal)

class Snake_pit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "legs are overrated -- come hang out with these smiling slitherers"
        self.animals = list()
    
    def Add_animal(self, animal):
        self.animals.append(animal)

class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "gotta love the water -- these critters do"
        self.animals = list()
    
    def Add_animal(self, animal):
        self.animals.append(animal)
        

creature_culdesac = Petting_zoo("Creature Culdesac")
no_feet_knoll = Snake_pit("No Feet Knoll")
swimmy_jazz = Wetlands("Swimmy Jazz")