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
from attractions.attractions_instances import creature_culdesac
from attractions.attractions_instances import no_feet_knoll
from attractions.attractions_instances import swimmy_jazz

creature_culdesac.Add_animal(leif)
creature_culdesac.Add_animal(desmond)
creature_culdesac.Add_animal(shepherd)
creature_culdesac.Add_animal(geoffrey)
creature_culdesac.Add_animal(ingrid)
print(f'{creature_culdesac.attraction_name} is where you can find {creature_culdesac.description}.')
for animal in creature_culdesac.animals:
    print(f'    * {animal.name} the {animal.species}')


no_feet_knoll.Add_animal(bill)
no_feet_knoll.Add_animal(ridley)
no_feet_knoll.Add_animal(keira)
no_feet_knoll.Add_animal(seth)
no_feet_knoll.Add_animal(carol)
print(f'{no_feet_knoll.attraction_name} is where {no_feet_knoll.description}!')
for animal in no_feet_knoll.animals:
    print(f'    * {animal.name} the {animal.species}')

swimmy_jazz.Add_animal(maureen)
swimmy_jazz.Add_animal(bentley)
swimmy_jazz.Add_animal(cheryl)
swimmy_jazz.Add_animal(prose)
swimmy_jazz.Add_animal(noelle)
print(f'{swimmy_jazz.attraction_name} is where you {swimmy_jazz.description}.')
for animal in swimmy_jazz.animals:
    print(f'    * {animal.name} the {animal.species}')
