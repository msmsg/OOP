from goose import Goose
from cow import Cow
from sheep import Sheep
from chicken import Chicken
from goat import Goat
from duck import Duck

 
grey = Goose('Grey', 12)


white = Goose('White', 13.5)
white.profit = 3


mary = Cow('Mary', 200)


barashek = Sheep('Barashek', 30)

kudryavyi = Sheep('Kudryavyi', 28)
kudryavyi.profit = 6

ko_ko = Chicken('Ko-Ko', 3)


kukareku = Chicken('Kukareku', 5)
kukareku.profit = 0
kukareku.voice = 'kukareku'

roga = Goat('Roga', 20)


kopyta = Goat('Kopyta', 19)
kopyta.profit = 4
kopyta.ad_profit = 2


kryakva = Duck('Kryakva', 2)



names_animals = [grey, white, mary, barashek, kudryavyi, ko_ko, kukareku, roga, kopyta, kryakva]


for item in names_animals:
    print(f'Name is {item.name}')
    print(f'{item.name} is {item.species}.')
    print(f'{item.name} weights {item.weight} kg.')
    print(f'{item.name} ate.')
    print(f'{item.name} {item.feed(item.weight)}')
    print(f'{item.take_profit(item.profit)} {item.name_profit}.')

    if hasattr(item, 'ad_profit'):
        print('Additionally we collected:')
        print(item.take_ad_profit(item.ad_profit))

        
    print(f'{item.name} said:')
    print(item.animals_say(item.voice))
    print()


max = 0
total = 0
for item in names_animals:
    total +=  item.weight   
    if max < item.weight:        
        max = item.weight
        big_species = item.species
        big_name = item.name
  
print(f'Total weight is {total} kg.')
print()
print(f'The heaviest animal is {big_species} {big_name}. Its weight is {max} kg.')


