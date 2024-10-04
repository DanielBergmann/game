from models.location import Object, Location
from models.map import Map
from models.person import Person
import getch

# Initialize objects
print("Initializing objects...")
chair = Object("Chair", "A wooden chair with four legs.")
table = Object("Table", "A round table made of oak.")

# Initialize locations
print("Initializing locations...")
living_room = Location("Living Room", "A cozy living room with a fireplace.")
kitchen = Location("Kitchen", "A kitchen with modern appliances.")

# Add objects to the living room
print("Adding objects to the Living Room...")
living_room.add_object(chair)
living_room.add_object(table)

# Add entrances between locations
print("Adding entrances between locations...")
living_room.add_entrance("north", kitchen)
kitchen.add_entrance("south", living_room)

# Create a 3x3 map
print("Creating a 3x3 map...")
house_map = Map(7, 7)

# Set locations on the map
print("Setting locations on the map...")
house_map.set_location(1, 1, living_room)
house_map.set_location(0, 1, kitchen)

# Print the initial map
print("Initial map:")
house_map.print_grid()

# Initialize a person at position (1, 1) with a view range of 1
print("Initializing person 'John' at position (1, 1) with view range of 1...")
john = Person("John", 1, 1, 1)

# Update John's knowledge of the map
print("Updating John's knowledge of the map...")
john.update_knowledge(house_map)

# Print the map from John's perspective
print("\nMap from John's perspective:")
john.print_known_map(house_map)

# Function to handle movement using input commands without pressing Enter
def handle_movement():
    print("Use W/A/S/D keys to move. Press 'q' to quit.")
    while True:
        # Print the map from John's perspective
        print("\nMap from John's perspective:")
        john.print_known_map(house_map)

        # Get user input without needing Enter
        key = getch.getch().lower()
        print(f"Key pressed: {key}")  # Debugging: Log key pressed

        # Move John based on the key pressed
        if key == 'w' and john.row > 0:
            print("Moving John up...")
            john.move(john.row - 1, john.col)
        elif key == 's' and john.row < len(house_map.grid) - 1:
            print("Moving John down...")
            john.move(john.row + 1, john.col)
        elif key == 'a' and john.col > 0:
            print("Moving John left...")
            john.move(john.row, john.col - 1)
        elif key == 'd' and john.col < len(house_map.grid[0]) - 1:
            print("Moving John right...")
            john.move(john.row, john.col + 1)
        elif key == 'q':
            print("Quitting...")
            break
        else:
            print("Invalid input. Use W/A/S/D to move or Q to quit.")

        # Update John's knowledge of the map
        print("Updating John's knowledge of the map after movement...")
        john.update_knowledge(house_map)

# Run the input-based movement handler
handle_movement()
