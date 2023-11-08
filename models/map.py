import numpy


class Map:
    def __init__(self, size: tuple[int, int] = None):
        self.locations = []
        self.size = size
        self.map = numpy.array([[0] * size[0]] * size[1])

    def print_map(self):
        for row in self.map:
            for element in row:
                print(element, end=" ")
            print()
        print()

    def __getitem__(self, item):
        return self.map[item]

    def __setitem__(self, key, value):
        self.map[key] = value


class Location:
    def __init__(self, name: str, description: str, coordinates: tuple = None):
        self.coordinates = coordinates
