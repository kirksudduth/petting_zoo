from animals import leif
from animals import desmond
from animals import shepherd
from animals import geoffrey
from animals import ingrid
from animals import carol
from animals import bill
from animals import ridley
from animals import keira
from animals import seth
from animals import maureen
from animals import bentley
from animals import cheryl
from animals import prose
from animals import noelle
from attractions import Petting_zoo
from attractions import Snake_pit
from attractions import Wetlands
from animals import Beaver
from animals import Llama
from animals import Donkey
from animals import Goat
from animals import Sheep
from animals import Ibex
from animals import Coral_snake
from animals import Cyclops_snake
from animals import Rattlesnake
from animals import Boa_constrictor
from animals import King_cobra
from animals import Mallard
from animals import Catfish
from animals import Nemo
from animals import Platypus

bosworth = Beaver("Bosworth", "belching beaver", "barley and rye", 210)

creature_culdesac = Petting_zoo(
    "Creature Culdesac", "all those creatures that want(?) to be petted to no end")
creature_culdesac.add_animal(leif)
creature_culdesac.add_animal(desmond)
creature_culdesac.add_animal(shepherd)
creature_culdesac.add_animal(geoffrey)
creature_culdesac.add_animal(ingrid)
print(f'{creature_culdesac.attraction_name} is where you can find {creature_culdesac.description}.')
for animal in creature_culdesac.animals:
    print(f'    * {animal.name} the {animal.species}')

no_feet_knoll = Snake_pit(
    "No Feet Knoll", "slithering is the new walking")
no_feet_knoll.add_animal(bill)
no_feet_knoll.add_animal(ridley)
no_feet_knoll.add_animal(keira)
no_feet_knoll.add_animal(seth)
no_feet_knoll.add_animal(carol)
print(f'{no_feet_knoll.attraction_name} is where {no_feet_knoll.description}!')
for animal in no_feet_knoll.animals:
    print(f'    * {animal.name} the {animal.species}')


swimmy_jazz = Wetlands(
    "Swimmy Jazz", "where you can find wet and wonderful creatures")
swimmy_jazz.add_animal(maureen)
swimmy_jazz.add_animal(bentley)
swimmy_jazz.add_animal(cheryl)
swimmy_jazz.add_animal(prose)
swimmy_jazz.add_animal(noelle)
swimmy_jazz.add_animal(bosworth)
print(f'{swimmy_jazz.attraction_name} is where you {swimmy_jazz.description}.')
for animal in swimmy_jazz.animals:
    print(f'    * {animal.name} the {animal.species}')
