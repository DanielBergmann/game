class Map:
    def __init__(self, name: str, description: str):
        self.locations = []


class Location:
    def __init__(self, name: str, description: str, coordinates: tuple = None):
        self.coordinates = coordinates
