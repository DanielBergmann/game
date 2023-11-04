class Map:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.locations = []


class Location:
    def __init__(self, name: str, description: str, coordinates: tuple = None):
        self.name = name
        self.description = description
        self.coordinates = coordinates
