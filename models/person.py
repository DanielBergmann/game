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

    def move(self, map_obj, new_row, new_col):
        """
        Move the person to a new position.

        Parameters:
        new_row (int): The new row position.
        new_col (int): The new column position.
        """
        if self._is_within_bounds(map_obj, new_row, new_col):
            self.row = new_row
            self.col = new_col

    def _is_within_bounds(self, map_obj, row, col):
        """
        Check if the given position is within the bounds of the map.

        Parameters:
        row (int): The row position to check.
        col (int): The column position to check.

        Returns:
        bool: True if the position is within bounds, False otherwise.
        """
        return 0 <= row < len(map_obj.grid) and 0 <= col < len(map_obj.grid[0])

    def update_knowledge(self, map_obj):
        # Clear knowledge that was in view but is no longer visible
        self.known_map = {key: value for key, value in self.known_map.items() if
                          not self._is_within_view(key[0], key[1])}
        # Update the current knowledge with new visible locations
        """
        Update the person's knowledge of the map based on their current position and view range.

        Parameters:
        map_obj (Map): The map to explore.
        """
        for r in range(self._get_min_row(), self._get_max_row(len(map_obj.grid))):
            for c in range(self._get_min_col(), self._get_max_col(len(map_obj.grid[0]))):
                location = map_obj.get_location(r, c)
                if location:
                    self.known_map[(r, c)] = location
                else:
                    self.known_map[(r, c)] = 'empty'

    def _get_min_row(self):
        return max(0, self.row - self.view_range)

    def _get_max_row(self, max_rows):
        return min(max_rows, self.row + self.view_range + 1)

    def _get_min_col(self):
        return max(0, self.col - self.view_range)

    def _get_max_col(self, max_cols):
        return min(max_cols, self.col + self.view_range + 1)

    def _is_within_view(self, r, c):
        """
        Check if a given position is within the person's view range.

        Parameters:
        r (int): The row position to check.
        c (int): The column position to check.

        Returns:
        bool: True if the position is within view range, False otherwise.
        """
        return abs(self.row - r) <= self.view_range and abs(self.col - c) <= self.view_range

    def print_known_map(self, map_obj):
        """
        Print the map from the person's perspective, marking visible and known areas.

        Parameters:
        map_obj (Map): The map to display.
        """
        for r in range(len(map_obj.grid)):
            row_representation = []
            for c in range(len(map_obj.grid[0])):
                if r == self.row and c == self.col:
                    row_representation.append('P')
                elif (r, c) in self.known_map:
                    if self._is_within_view(r, c):
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
