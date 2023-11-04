class Thing:
    def __init__(
            self,
            name: str,
            weight: float = 0.0
    ):
        self.weight = weight
        self.name = name



def calculate_weight(things: list[Thing]):
    total_weight = 0.0
    for thing in things:
        print(thing)
        total_weight += thing.weight
    return total_weight


class Inventory:
    def __init__(
            self,
            contains: list[Thing],
            max_weight: float = 100.0
    ):
        self.max_weight = max_weight
        self.contains = contains
        self.weight = calculate_weight(self.contains)


class Stats:
    def __init__(
            self,
            strength: int = 1,
            wisdom: int = 1,
            movement_speed: int = 1,
            agility: int = 1,
            intelligence: int = 1,
            luck: int = 1,
    ):
        self.strength = strength
        self.wisdom = wisdom
        self.movement_speed = movement_speed
        self.agility = agility
        self.intelligence = intelligence
        self.luck = luck


class Person:
    def __init__(
            self,
            current_health: int,
            inventory: Inventory,
            stats: Stats,
            max_health: int = 100,
    ):
        self.max_health = max_health
        self.current_health = current_health
        self.inventory = inventory
        self.stats = stats
