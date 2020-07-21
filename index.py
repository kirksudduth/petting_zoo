from animals.animals_instances import leif
from animals.animals_instances import desmond
from animals.animals_instances import shepherd
from animals.animals_instances import geoffrey
from animals.animals_instances import ingrid
from animals.animals_instances import carol
from animals.animals_instances import bill
from animals.animals_instances import ridley
from animals.animals_instances import keira
from animals.animals_instances import seth
from animals.animals_instances import maureen
from animals.animals_instances import bentley
from animals.animals_instances import cheryl
from animals.animals_instances import prose
from animals.animals_instances import noelle
from attractions import Petting_zoo
from attractions import Snake_pit
from attractions import Wetlands
from animals import Beaver

benny = Beaver("Benny", "beaver", "barley and rye", 210)

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
    "No Feet Knoll", "slithering -- it's the new walking")
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
print(f'{swimmy_jazz.attraction_name} is where you {swimmy_jazz.description}.')
for animal in swimmy_jazz.animals:
    print(f'    * {animal.name} the {animal.species}')
