from goose import Goose
from cow import Cow
from sheep import Sheep
from chicken import Chicken
from goat import Goat
from duck import Duck

 
grey = Goose()
grey.weight = 12
grey.name = 'Grey'


white = Goose()
white.weight = 13.5
white.name = 'White'
white.profit = 3


mary = Cow()
mary.weight = 200
mary.name = 'Mary'
mary.profit = 15

barashek = Sheep()
barashek.weight = 30
barashek.name = 'Barashek'
barashek.profit = 5


kudryavyi = Sheep()
kudryavyi.weight = 28
kudryavyi.name = 'Kudryavyi'
kudryavyi.profit = 6

ko_ko = Chicken()
ko_ko.weight = 3
ko_ko.name = 'Ko-Ko'
ko_ko.profit = 3


kukareku = Chicken()
kukareku.weight = 5
kukareku.name = 'Kukareku'
kukareku.profit = 0
kukareku.voice = 'kukareku'

roga = Goat()
roga.weight = 20
roga.name = 'Roga'
roga.profit = 5
roga.ad_profit = 3


kopyta = Goat()
kopyta.weight = 19
kopyta.name = 'Kopyta'
kopyta.profit = 4
kopyta.ad_profit = 2


kryakva = Duck()
kryakva.weight = 2
kryakva.name = 'Kryakva'
kryakva.profit = 2



names_animals = [grey, white, mary, barashek, kudryavyi, ko_ko, kukareku, roga, kopyta, kryakva]
max = 0
for item in names_animals:    
    if max < item.weight:
        max = item.weight
        big_species = item.species
        big_name = item.name
  

print(f'The heaviest animal is {big_species} {big_name}. Its weight is {max} kg.')


