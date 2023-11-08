from models.map import Map


class Person:
    def __init__(
        self,
        location: tuple[int, int] = (0, 0),
    ):
        self.name = "Dummy"
        self.location = location
        self.previous_location = None

    def move(self, direction: tuple[int, int] = (0, 0), map: Map = None):
        try:
            self.previous_location = self.location
            new_location = (
                direction[0] + self.location[0],
                direction[1] + self.location[1],
            )
            map[new_location] = 1

            map[self.previous_location] = 2
            self.location = new_location

        except IndexError:
            print("You can't move there!")
