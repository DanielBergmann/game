class Object:
    def __init__(self, name, description):
        """
        Initialize the Object instance with a name and description.

        Parameters:
        name (str): The name of the object.
        description (str): A short description of the object.
        """
        self.name = name
        self.description = description

    def describe(self):
        """
        Print the description of the object.
        """
        print(f"{self.name}: {self.description}")

    def set_name(self, new_name):
        """
        Set a new name for the object.

        Parameters:
        new_name (str): The new name to set.
        """
        self.name = new_name
        print(f"Object name updated to {self.name}")

    def set_description(self, new_description):
        """
        Set a new description for the object.

        Parameters:
        new_description (str): The new description to set.
        """
        self.description = new_description
        print(f"Object description updated to: {self.description}")

    def representation(self):
        """
        Return a 1-letter representation of the object (first letter of the name).
        """
        return self.name[0].upper()


class Location:
    def __init__(self, name, description):
        """
        Initialize the Location instance with a name and description.

        Parameters:
        name (str): The name of the location.
        description (str): A short description of the location.
        """
        self.name = name
        self.description = description
        self.objects = []  # List to store objects in this location
        self.entrances = {}  # Dictionary to store adjacent entrances

    def describe(self):
        """
        Print the description of the location and list the objects present.
        """
        print(f"{self.name}: {self.description}")
        if self.objects:
            print("Objects in this location:")
            for obj in self.objects:
                print(f"- {obj.name}")
        else:
            print("No objects in this location.")

        if self.entrances:
            print("Entrances:")
            for direction, location in self.entrances.items():
                print(f"- {direction}: {location.name}")

    def add_object(self, obj):
        """
        Add an object to the location.

        Parameters:
        obj (Object): The object to add to the location.
        """
        self.objects.append(obj)
        print(f"{obj.name} added to {self.name}")

    def remove_object(self, obj_name):
        """
        Remove an object from the location by its name.

        Parameters:
        obj_name (str): The name of the object to remove.
        """
        self.objects = [obj for obj in self.objects if obj.name != obj_name]
        print(f"{obj_name} removed from {self.name}")

    def representation(self):
        """
        Return a 1-letter representation of the location (first letter of the name).
        """
        return self.name[0].upper()

    def add_entrance(self, direction, location):
        """
        Add an entrance to an adjacent location.

        Parameters:
        direction (str): The direction of the entrance (e.g., 'north', 'south').
        location (Location): The adjacent location.
        """
        self.entrances[direction] = location
        print(f"Entrance added to the {direction} leading to {location.name}")