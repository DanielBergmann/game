class Map:
    def __init__(self, rows, cols, fill_value=0):
        """
        Initialize the Map with a grid (2D list) with specified number of rows and columns.
        Fill the grid with the given value, default is zero.

        Parameters:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        fill_value (optional): Value to fill in the grid. Default is 0.
        """
        self.grid = [[fill_value for _ in range(cols)] for _ in range(rows)]
        self.previous_grids = [self.grid]

    def print_grid(self):
        """
        Print the grid in a way that displays rows and columns naturally.
        """
        for row in self.grid:
            print(" ".join(map(str, row)))
        print()  # Add an empty line for better readability

    def set_value(self, row, col, value):
        """
        Set a specific value at a given location in the grid.

        Parameters:
        row (int): The row index where the value should be set.
        col (int): The column index where the value should be set.
        value: The value to set at the specified location.
        """
        if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
            self.grid[row][col] = value
        else:
            print("Error: Row or column index out of bounds.")

    def set_value_with_memory(self, row, col, value):
        """
        Set a specific value at a given location in the grid, while remembering the previous state.
        If the value is moved to a new position, remove it from the old position.

        Parameters:
        row (int): The row index where the value should be set.
        col (int): The column index where the value should be set.
        value: The value to set at the specified location.
        """
        if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
            # Store the current grid state before modifying
            self.previous_grids.append([r[:] for r in self.grid])

            # Find and remove the value if it already exists in the grid
            for r in range(len(self.grid)):
                for c in range(len(self.grid[0])):
                    if self.grid[r][c] == value:
                        self.grid[r][c] = self.previous_grids[-2][r][c]

            # Update the grid with the new value
            self.grid[row][col] = value
        else:
            print("Error: Row or column index out of bounds.")

    def revert_to_previous(self):
        """
        Revert the grid to its previous state.
        """
        if self.previous_grids:
            self.grid = self.previous_grids.pop()
        else:
            print("No previous state to revert to.")


print("Initial 5x5 grid filled with the value 7:")
map2 = Map(1, 5, 7)
map2.print_grid()

print("Set value 5 at position (0, 0):")
map2.set_value_with_memory(0, 0, 5)
map2.print_grid()

print("Set value 5 at position (0, 1), moving it from (0, 0):")
map2.set_value_with_memory(0, 1, 5)
map2.print_grid()

print("Set value 5 at position (0, 1), moving it from (0, 0):")
map2.set_value_with_memory(0, 3, 4)
map2.print_grid()

print("Set value 5 at position (0, 1), moving it from (0, 0):")
map2.set_value_with_memory(0, 4, 4)
map2.print_grid()

print("Revert to previous state:")
map2.revert_to_previous()
map2.print_grid()

print("Revert to previous state:")
map2.revert_to_previous()
map2.print_grid()