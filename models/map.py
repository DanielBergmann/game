import copy


class Map:
    def __init__(self, rows, cols, fill_value=None):
        """
        Initialize the Map with a grid (2D list) with specified number of rows and columns.
        Fill the grid with the given value, default is None.

        Parameters:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        fill_value (optional): Value to fill in the grid. Default is None.
        """
        self.grid = [[fill_value for _ in range(cols)] for _ in range(rows)]
        self.previous_grids = [copy.deepcopy(self.grid)]

    def print_grid(self):
        """
        Print the grid in a way that displays rows and columns naturally.
        """
        for row in self.grid:
            print(" ".join([cell.representation() if cell else '.' for cell in row]))
        print()  # Add an empty line for better readability

    def set_location(self, row, col, location):
        """
        Set a specific location at a given position in the grid.

        Parameters:
        row (int): The row index where the location should be set.
        col (int): The column index where the location should be set.
        location (Location): The location to set at the specified position.
        """
        if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
            self.grid[row][col] = location
        else:
            raise IndexError("Row or column index out of bounds.")

    def get_location(self, row, col):
        """
        Get the location at a specific position in the grid.

        Parameters:
        row (int): The row index.
        col (int): The column index.

        Returns:
        Location: The location at the specified position, or None if empty.
        """
        if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
            return self.grid[row][col]
        else:
            raise IndexError("Row or column index out of bounds.")
