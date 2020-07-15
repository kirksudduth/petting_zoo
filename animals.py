from datetime import date

# WALKING CLASSES
class Llama:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

leif = Llama("Leif", "curly-haired llama", "afternoon", "oats and greens")
print(f'{leif.name} the {leif.species} is available for petting during the {leif.shift} shift.')

class Donkey:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

desmond = Donkey("Desmond", "agreeable donkey", "morning", "eggs benedict")
print(f'{desmond.name} the {desmond.species} is available for petting during the {desmond.shift} shift.')


class Sheep:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

shepherd = Sheep("Shepherd", "responsible sheep", "midday", "an ancient grain bowl")
print(f'{shepherd.name} the {shepherd.species} is available for petting during the {shepherd.shift} shift.')


class Ibex:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

ingrid = Ibex("Ingrid", "scared-of-heights ibex", "afternoon", "corn dogs and funnel cakes")
print(f'{ingrid.name} the {ingrid.species} is available for petting during the {ingrid.shift} shift.')


class Goat:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

geoffrey = Goat("Geoffrey", "billy goat", "morning", "fruit salad")
print(f'{geoffrey.name} the {geoffrey.species} is available for petting during the {geoffrey.shift} shift.')
#END WALKING CLASSES

#START SLITHERING CLASSES
class Coral_snake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

carol = Coral_snake("Carol", "deadly", "10 blind mice")
print(carol)

class Boa_constrictor:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

bill = Boa_constrictor("Bill", "extra clingy", "shrimp alfredo")
print(bill)

class Rattlesnake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

ridley = Rattlesnake("Ridley", "rhythmic rattler", "salmon with asparagus")
print(ridley)

class King_cobra:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

keira = King_cobra("Keira", "ruler cobra", "red lentil curry")
print(keira)

class Cyclops_snake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

seth = Cyclops_snake("Seth", "one-eyed snake", "black-eyed-peas (Fergie and will.i.am)")
print(seth)
#END SLITHERING CLASSES

#START SWIMMING CLASSES
class Mallard:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

maureen = Mallard("Maureen", "purple mallard", "arroz con pollo")
print(maureen)

class Beaver:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

bentley = Beaver("Bentley", "cabin building beaver", "drunken noodles")
print(bentley)

class Catfish:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

cheryl = Catfish("Cheryl", "talking catfish", "thom khai soup")
print(cheryl)

class Platypus:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

prose = Platypus("Prose", "poetic platypus", "birthday cake")
print(prose)

class Nemo:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

noelle = Nemo("Noelle", "navigational fish", "cotton candy")
print(noelle)

#END SWIMMING CLASSES
