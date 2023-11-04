from models.event import Event
from models.things import Container, Thing
from models.utils import calculate_weight


class Inventory(Container):
    def __init__(self, contains: list[Thing], name: str, max_weight: float = 100.0):
        super().__init__(name, contains=contains)
        self.max_weight = max_weight


class Task:
    def __init__(self, name: str, description: str, priority: int):
        self.name = name
        self.description = description
        self.priority = priority


class Trait:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Ability:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Job:
    def __init__(self, name: str, description: str, pay_rate: float = 0.0):
        self.name = name
        self.description = description
        self.pay_rate = pay_rate


class Stats:
    def __init__(
        self,
        strength: int = 1,
        wisdom: int = 1,
        movement_speed: int = 1,
        intelligence: int = 1,
        luck: int = 1,
        charisma: int = 1,
        constitution: int = 1,
        dexterity: int = 1,
        perception: int = 1,
        willpower: int = 1,
    ):
        self.strength = strength
        self.wisdom = wisdom
        self.movement_speed = movement_speed
        self.intelligence = intelligence
        self.charisma = charisma
        self.luck = luck
        self.constitution = constitution
        self.dexterity = dexterity
        self.perception = perception
        self.willpower = willpower


class Person:
    def __init__(
        self,
        current_health: int,
        inventory: Inventory,
        stats: Stats,
        tasks: list,
        job: str,
        name: str,
        family: list,
        age: int,
        relationships: list,
        traits: list,
        abilities: list,
        mental_state: str,
        mental_state_history: list,
        morality: str,
        morality_history: list,
        events: list,
        event_history: list,
        known_locations: list,
        known_locations_history: list,
        known_people: list,
        known_things: list[Thing],
        known_events: list[Event],
        known_jobs: list[Job],
        known_relationships: list,
        known_quests: list,
        known_factions: list,
        known_guilds: list,
        known_groups: list,
        known_organizations: list,
        max_health: int = 100,
        location: tuple(int, int) = (0, 0),
    ):
        self.max_health = max_health
        self.current_health = current_health
        self.inventory = inventory
        self.stats = stats
        self.tasks = tasks
        self.job = job
        self.name = name
        self.age = age
        self.family = family
        self.relationships = relationships
        self.traits = traits
        self.abilities = abilities
        self.mental_state = mental_state
        self.mental_state_history = mental_state_history
        self.morality = morality
        self.morality_history = morality_history
        self.events = events
        self.event_history = event_history

        self.known_locations = known_locations
        self.known_locations_history = known_locations_history
        self.known_people = known_people
        self.known_things = known_things
        self.known_events = known_events
        self.known_jobs = known_jobs
        self.known_relationships = known_relationships
        self.known_quests = known_quests
        self.known_factions = known_factions
        self.known_guilds = known_guilds
        self.known_groups = known_groups
        self.known_organizations = known_organizations
        self.location = location

    def move(self, direction: tuple[int, int] = (0, 0)):
        result = (direction[0] + self.location[0], direction[1] + self.location[1])
        self.location = result

    def use(self):
        pass

    def equip(self):
        pass

    def unequip(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass

    def talk(self):
        pass

    def trade(self):
        pass

    def buy(self):
        pass

    def sell(self):
        pass

    def steal(self):
        pass

    def pickpocket(self):
        pass

    def craft(self):
        pass

    def cook(self):
        pass

    def eat(self):
        pass

    def drink(self):
        pass

    def sleep(self):
        pass

    def work(self):
        pass

    def study(self):
        pass

    def train(self):
        pass
