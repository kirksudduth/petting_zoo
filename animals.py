from datetime import date

# WALKING CLASSES
class Llama:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

leif = Llama("Leif", "curly-haired llama", "afternoon")
print(f'{leif.name} the {leif.species} is available for petting during the {leif.shift} shift.')

class Donkey:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

desmond = Donkey("Desmond", "agreeable donkey", "morning")
print(f'{desmond.name} the {desmond.species} is available for petting during the {desmond.shift} shift.')


class Sheep:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

shepherd = Sheep("Shepherd", "responsible sheep", "midday")
print(f'{shepherd.name} the {shepherd.species} is available for petting during the {shepherd.shift} shift.')


class Ibex:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

ingrid = Ibex("Ingrid", "scared-of-heights ibex", "afternoon")
print(f'{ingrid.name} the {ingrid.species} is available for petting during the {ingrid.shift} shift.')


class Goat:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
    # def __str__(self):
    #     return f''

geoffrey = Goat("Geoffrey", "billy goat", "morning")
print(f'{geoffrey.name} the {geoffrey.species} is available for petting during the {geoffrey.shift} shift.')
#END WALKING CLASSES

#START SLITHERING CLASSES
class Coral_snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

carol = Coral_snake("Carol", "deadly")
print(carol)

class Boa_constrictor:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

bill = Boa_constrictor("Bill", "extra clingy")
print(bill)

class Rattlesnake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

ridley = Rattlesnake("Ridley", "rhythmic rattler")
print(ridley)

class King_cobra:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

keira = King_cobra("Keira", "ruler cobra")
print(keira)

class Cyclops_snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

seth = Cyclops_snake("Seth", "one-eyed snake")
print(seth)
#END SLITHERING CLASSES

#START SWIMMING CLASSES
class Mallard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

maureen = Mallard("Maureen", "purple mallard")
print(maureen)

class Beaver:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

bentley = Beaver("Bentley", "cabin building beaver")
print(bentley)

class Catfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

cheryl = Catfish("Cheryl", "talking catfish")
print(cheryl)

class Platypus:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

prose = Platypus("Prose", "poetic platypus")
print(prose)

class Nemo:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

noelle = Nemo("Noelle", "navigational fish")
print(noelle)

#END SWIMMING CLASSES
