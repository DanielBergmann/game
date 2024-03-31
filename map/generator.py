import numpy

from map.constants import MapObjects as MO


class Unit:
    def __init__(
        self,
        location: tuple[int, int] = (0, 0),
        previous_location: tuple[int, int] = None,
        value: str = MO.objects["player"],
    ):
        self.location = location
        self.previous_location = previous_location
        self.value = value

    def move(self, direction: tuple[int, int] = (0, 0)):
        self.previous_location = self.location
        if self.location[0] + direction[0] < 0 or self.location[1] + direction[1] < 0:
            print("You can't move there!")
            return
        self.location = (
            direction[0] + self.location[0],
            direction[1] + self.location[1],
        )


class Map:
    def __init__(
        self, size: tuple[int, int] = None, locations: list[tuple[int, int]] = None
    ):
        self.locations = locations
        self.size = size
        self.map = numpy.array([[MO.objects["unvisited"]] * size[0]] * size[1])

    def print_map(self):
        for row in self.map:
            for element in row:
                print(element, end=" ")
            print()
        print()

    def populate(self, unit: Unit):
        try:
            if unit.previous_location:
                self.map[unit.previous_location[0]][
                    unit.previous_location[1]
                ] = MO.objects["visited"]
            self.map[unit.location[0]][unit.location[1]] = unit.value

        except IndexError:
            print("You can't move there!")
            unit.location = unit.previous_location
            self.map[unit.location[0]][unit.location[1]] = unit.value


map = Map((5, 5))
map.print_map()
unit = Unit()
map.populate(unit)
map.print_map()


def move(direction: tuple[int, int], unit: Unit, map: Map):
    unit.move(direction)
    map.populate(unit)
    map.print_map()


from pynput import keyboard
from pynput.keyboard import Key


def on_key_release(key):
    if key == Key.right:
        move((0, 1), unit, map)
    elif key == Key.left:
        move((0, -1), unit, map)
    elif key == Key.up:
        move((-1, 0), unit, map)
    elif key == Key.down:
        move((1, 0), unit, map)
    elif key == Key.esc:
        exit()


with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
