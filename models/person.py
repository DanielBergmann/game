class Person:
    def __init__(self, name, row, col, view_range):
        """
        Initialize a Person instance with a name, position, and view range.

        Parameters:
        name (str): The name of the person.
        row (int): The starting row position of the person.
        col (int): The starting column position of the person.
        view_range (int): The range of the person's view (number of cells).
        """
        self.name = name
        self.row = row
        self.col = col
        self.view_range = view_range
        self.known_map = {}  # Dictionary to store known locations and objects

    def move(self, new_row, new_col):
        """
        Move the person to a new position.

        Parameters:
        new_row (int): The new row position.
        new_col (int): The new column position.
        """
        self.row = new_row
        self.col = new_col

    def update_knowledge(self, map_obj):
        """
        Update the person's knowledge of the map based on their current position and view range.

        Parameters:
        map_obj (Map): The map to explore.
        """
        for r in range(max(0, self.row - self.view_range), min(len(map_obj.grid), self.row + self.view_range + 1)):
            for c in range(max(0, self.col - self.view_range),
                           min(len(map_obj.grid[0]), self.col + self.view_range + 1)):
                location = map_obj.get_location(r, c)
                if location:
                    self.known_map[(r, c)] = location
                else:
                    self.known_map[(r, c)] = 'empty'

    def print_known_map(self, map_obj):
        """
        Print the map from the person's perspective, marking visible and known areas.

        Parameters:
        map_obj (Map): The map to display.
        """
        for r in range(len(map_obj.grid)):
            row_representation = []
            for c in range(len(map_obj.grid[0])):
                if (r, c) in self.known_map:
                    if abs(self.row - r) <= self.view_range and abs(self.col - c) <= self.view_range:
                        # Visible locations
                        if self.known_map[(r, c)] == 'empty':
                            row_representation.append('.')
                        else:
                            row_representation.append(self.known_map[(r, c)].representation())
                    else:
                        # Known but not currently visible locations
                        if self.known_map[(r, c)] == 'empty':
                            row_representation.append('-')
                        else:
                            row_representation.append(self.known_map[(r, c)].representation().lower())
                else:
                    # Unknown locations
                    row_representation.append('?')
            print(" ".join(row_representation))
        print()  # Add an empty line for better readability
