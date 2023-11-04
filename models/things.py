from models.utils import calculate_weight


class Thing(object):
    def __init__(self, name: str, weight: float = 0.0):
        self.type = "thing"
        self.weight = weight
        self.name = name

    def __mul__(self, other: int):
        return [self for _ in range(other)]

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def is_thing(self):
        return self.type == "thing"


class Weapon(Thing):
    def __init__(self, name: str, weight: float = 0.0, damage: float = 0.0):
        super().__init__(name, weight)
        self.type = "weapon"
        self.damage = damage


class Tool(Thing):
    def __init__(self, name: str, weight: float = 0.0, eficiency: float = 0.0):
        super().__init__(name, weight)
        self.type = "tool"
        self.eficiency = eficiency


class Consumable(Thing):
    def __init__(self, name: str, weight: float = 0.0, effect: str = None):
        super().__init__(name, weight)
        self.type = "consumable"
        self.effect = effect


class Container(Thing):
    def __init__(
        self, name: str, weight: float = 0.0, capacity: float = 0.0, contains=None
    ):
        super().__init__(name, weight)
        if contains is None:
            contains = []

        self.type = "container"
        self.capacity = capacity
        self.contains: list[Thing] = contains
        self.capacity_left = self.capacity - calculate_weight(self.contains)
        self.container_weight = weight
        self.weight = weight + calculate_weight(self.contains)

    def add(self, thing: Thing):
        if self.check_weight(thing):
            self.contains.append(thing)
            if self.is_container():
                self.weight = self.container_weight + calculate_weight(self.contains)
                self.capacity_left = self.capacity_left - thing.weight
        else:
            raise Exception("Not enough capacity")

    def remove(self, thing: Thing):
        self.contains.remove(thing)
        self.weight = self.container_weight + calculate_weight(self.contains)
        self.capacity_left = self.capacity_left + thing.weight

    def check_weight(self, thing: Thing):
        if self.is_container():
            if self.capacity_left >= thing.weight:
                return True
            else:
                return False
        else:
            return True

    def is_container(self):
        return self.type == "container"


MATERIAL_TYPES = {
    "wood": "wood",
    "stone": "stone",
    "metal": "metal",
    "plastic": "plastic",
    "glass": "glass",
    "paper": "paper",
    "cloth": "cloth",
    "leather": "leather",
    "bone": "bone",
    "food": "food",
    "water": "water",
    "fuel": "fuel",
    "medicine": "medicine",
    "chemical": "chemical",
    "explosive": "explosive",
}


class Material(Thing):
    def __init__(self, name: str, weight: float = 0.0, material_type: str = None):
        super().__init__(name, weight)
        self.type = "material"
        if self.check_is_material_type(material_type):
            self.material_type = material_type
        else:
            raise Exception("Wrong material type")

    def check_is_material_type(self, material_type):
        if material_type in MATERIAL_TYPES:
            return True
        else:
            return False

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.weight == other.weight
            and self.material_type == other.material_type
        )

    def __hash__(self):
        return hash((self.name, self.weight, self.material_type))


class Recipe(Thing, dict):
    def __init__(
        self, name: str, weight: float = 0.0, recipe: dict[Material, int] = None
    ):
        super().__init__(name, weight)
        self.type = "recipe"
        self.recipe = recipe


class Craftable(Container):
    def __init__(self, name: str, recipe: Recipe = {}):
        super().__init__(name)
        self.recipe = recipe

    def add(self, thing: Material):
        if self._is_applicable(thing) and not self._is_enough(thing):
            self.contains.append(thing)
            self.weight = calculate_weight(self.contains)

    def _is_enough(self, thing: Material):
        return self.recipe.recipe[thing] <= self.contains.count(thing)

    def _is_applicable(self, thing: Material):
        recipe_materials = [m.material_type for m in self.recipe.recipe]
        return True if thing.material_type in recipe_materials else False


THING_TYPES = {
    "thing": Thing,
    "weapon": Weapon,
    "tool": Tool,
    "consumable": Consumable,
    "container": Container,
    "material": Material,
}
