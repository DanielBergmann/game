# testing map

import numpy
from map import Map

from models.person import Person

rows, cols = (5, 5)
map = Map((rows, cols))
person = Person()

map[person.location] = 1
map.print_map()
person.move((1, 0), map)
map.print_map()
person.move((1, 0), map)
map.print_map()
person.move((1, 0), map)
map.print_map()
person.move((1, 0), map)
map.print_map()
person.move((1, 0), map)
map.print_map()
person.move((1, 0), map)
map.print_map()

map2 = Map((10, 10))
map2[person.location] = 1
map2.print_map()
