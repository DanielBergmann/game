import pytest
from models.location import Object, Location
from models.map import Map
from models.person import Person


@pytest.fixture
def chair():
    return Object("Chair", "A wooden chair with four legs.")


@pytest.fixture
def living_room():
    return Location("Living Room", "A cozy living room with a fireplace.")


@pytest.fixture
def kitchen():
    return Location("Kitchen", "A modern kitchen.")


@pytest.fixture
def game_map():
    return Map(4, 4)


@pytest.fixture
def john():
    return Person("John", 1, 1, 1)


@pytest.mark.parametrize("name, description", [
    ("Chair", "A wooden chair with four legs."),
    ("Table", "A round table made of oak.")
])
def test_object_initialization(name, description):
    obj = Object(name, description)
    assert obj.name == name
    assert obj.description == description


def test_set_name(chair):
    chair.set_name("Stool")
    assert chair.name == "Stool"


def test_set_description(chair):
    chair.set_description("A small stool.")
    assert chair.description == "A small stool."


def test_location_initialization(living_room):
    assert living_room.name == "Living Room"
    assert living_room.description == "A cozy living room with a fireplace."
    assert len(living_room.objects) == 0
    assert len(living_room.entrances) == 0


def test_add_object(living_room, chair):
    living_room.add_object(chair)
    assert chair in living_room.objects


def test_add_entrance(living_room, kitchen):
    living_room.add_entrance("north", kitchen)
    assert "north" in living_room.entrances
    assert living_room.entrances["north"] == kitchen


def test_map_initialization(game_map):
    assert len(game_map.grid) == 4
    assert len(game_map.grid[0]) == 4
    for row in game_map.grid:
        for cell in row:
            assert cell is None


def test_set_location(game_map, living_room):
    game_map.set_location(1, 1, living_room)
    assert game_map.get_location(1, 1) == living_room


def test_get_location(game_map, living_room):
    game_map.set_location(1, 1, living_room)
    assert game_map.get_location(1, 1) == living_room
    assert game_map.get_location(0, 0) is None
    with pytest.raises(IndexError):
        game_map.get_location(5, 5)
    with pytest.raises(IndexError):
        game_map.get_location(-1, -1)


def test_person_initialization(john):
    assert john.name == "John"
    assert john.row == 1
    assert john.col == 1
    assert john.view_range == 1
    assert len(john.known_map) == 0


def test_move_person(john, game_map):
    john.move(game_map, 2, 2)
    assert john.row == 2
    assert john.col == 2


def test_move_person_out_of_bounds(game_map, john):
    john.move(game_map, -1, 1)
    assert john.row >= 0
    john.move(game_map, 4, 1)
    assert john.row < len(game_map.grid)
    john.move(game_map, 1, -1)
    assert john.col >= 0
    john.move(game_map, 1, 4)
    assert john.col < len(game_map.grid[0])


def test_update_knowledge(game_map, living_room, john):
    game_map.set_location(1, 1, living_room)
    john.update_knowledge(game_map)
    assert (1, 1) in john.known_map
    assert john.known_map[(1, 1)] == living_room
    assert (0, 0) in john.known_map
    assert (3, 3) not in john.known_map
