from models.things import Container, Craftable, Material, Recipe, Thing


class TestContainer:
    def test_container(self):
        container = Container(name="test", weight=1.5, capacity=10.0)
        assert container.name == "test"
        assert container.weight == 1.5
        assert container.capacity == 10.0
        assert container.type == "container"
        assert container.contains == []
        assert container.capacity_left == 10.0
        assert container.is_container() is True

    def test_container_add(self):
        container = Container(name="test", weight=1.5, capacity=10.0)
        item = Thing(name="test2", weight=1.5)
        container.add(item)
        assert container.weight == 3.0
        assert container.container_weight == 1.5
        assert container.contains == [item]
        assert container.capacity_left == 8.5

    def test_container_remove(self):
        container = Container(name="test", weight=1.5, capacity=10.0)
        item = Thing(name="test2", weight=1.5)
        container.add(item)
        assert container.weight == 3.0
        assert container.container_weight == 1.5
        assert container.contains == [item]
        assert container.capacity_left == 8.5
        container.remove(item)
        assert container.weight == 1.5
        assert container.contains == []
        assert container.capacity_left == 10.0


class TestThing:
    def test_thing(self):
        thing = Thing(name="test", weight=1.5)
        assert thing.name == "test"
        assert thing.weight == 1.5
        assert thing.type == "thing"

    def test_thing_multiply(self):
        thing = Thing(name="test", weight=1.5)
        several_things = thing * 4
        assert several_things == [thing, thing, thing, thing]

    def test_thing_multiply_wrong_value(self):
        thing = Thing(name="test", weight=1.5)
        try:
            thing = thing * "a"
        except TypeError:
            assert True


class TestCreatable:
    def test_creatable(self):
        recipe = Recipe(
            name="test",
            weight=0.1,
            recipe={
                Material(name="wood", weight=1.5, material_type="wood"): 2,
                Material(name="stone", weight=1.5, material_type="stone"): 1,
                Material(name="cloth", weight=1.5, material_type="cloth"): 1,
            },
        )

        creatable = Craftable(name="test", recipe=recipe)
        assert creatable.name == "test"

        creatable.add(Material(name="wood", weight=1.5, material_type="wood"))
        assert (
            creatable.contains.count(
                Material(name="wood", weight=1.5, material_type="wood")
            )
            == 1
        )

        creatable.add(Material(name="wood", weight=1.5, material_type="wood"))
        assert (
            creatable.contains.count(
                Material(name="wood", weight=1.5, material_type="wood")
            )
            == 2
        )

        creatable.add(Material(name="wood", weight=1.5, material_type="wood"))
        assert (
            creatable.contains.count(
                Material(name="wood", weight=1.5, material_type="wood")
            )
            == 2
        )  # not more than in recipe(2)
