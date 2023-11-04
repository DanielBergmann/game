# testing map

import numpy


class Dot:
    def __init__(self):
        self.location = (0, 0)

    def move(self, direction: tuple[int, int] = (0, 0)):
        result = (direction[0] + self.location[0], direction[1] + self.location[1])
        self.location = result


rows, cols = (5, 5)
arr = [[0] * cols] * rows

a = numpy.array([[0] * cols] * rows)
dot = Dot()
a[dot.location] = 1
# print(a[1, 2])
# point = (1, 2)
# print(a[point])


def print_map(map):
    for row in map:
        for element in row:
            print(element, end=" ")
        print()
    print()


print_map(a)

a[dot.location] = 0
dot.move((1, 0))
a[dot.location] = 1

print_map(a)

a[dot.location] = 0
dot.move((1, 1))
a[dot.location] = 1

print_map(a)
a[dot.location] = 0
dot.move((1, 1))
a[dot.location] = 1

print_map(a)
