import sys
import random

class Maze:
    def __init__(self, width, height, tile_str=None):
        self.width, self.height = width, height
        self.tiles = ['.'] * (width * height) if tile_str is None else self.format_map_str(tile_str)
        self.available_positions = []  # Renamed from pos_list
        self.connections = {}  # Maps adjacent tiles
        self.verbose = False ## This needs to rechecked

    def format_map_str(self, tiles):
        """Converts the input string into a list of characters."""
        return [c for line in tiles.splitlines() for c in line.strip()]

    def __str__(self):
        """Returns the maze as a string."""
        return "\n".join("".join(self.tiles[y * self.width: (y + 1) * self.width]) for y in range(self.height))

    def xy_to_index(self, x, y):
        """Converts 2D coordinates to a 1D index."""
        return x + y * self.width

    def valid(self, x, y):
        """Checks if the given coordinates (x, y) are valid (inside the maze)."""
        return 0 <= x < self.width and 0 <= y < self.height

    def get_tile(self, x, y):
        """Returns the tile at coordinates (x, y), or None if it's out of bounds."""
        return self.tiles[self.xy_to_index(x, y)] if self.valid(x, y) else None

    def set_tile(self, x, y, tile):
        """Sets the tile at coordinates (x, y) to the specified tile if valid."""
        if self.valid(x, y):
            self.tiles[self.xy_to_index(x, y)] = tile

    def add_wall_block(self, x, y):
        """Adds a 2x2 block of walls (|) at the given coordinates (x, y)."""
        for dx in range(2):
            for dy in range(2):
                self.set_tile(x + 1 + dx, y + 1 + dy, '|')

    def can_new_wall_fit(self, x, y):
        """Checks if a new wall block can fit at the coordinates (x, y)."""
        return all(self.get_tile(x0, y0) == '.' for y0 in range(y, y + 4) for x0 in range(x, x + 4))

    def update_available_positions(self):
        """Updates the list of positions where new wall blocks can be placed."""
        self.available_positions = [(x, y) for y in range(self.height) for x in range(self.width) if self.can_new_wall_fit(x, y)]

    def add_connection(self, x, y, dx, dy):
        """Adds a connection between the position (x, y) and its adjacent positions."""
        src = (x, y)
        for step in range(1, 3):
            dest = (x + dx * step, y + dy * step)
            if dest in self.available_positions:
                self.connections.setdefault(dest, []).append(src)

    def update_connections(self):
        """Updates the connection map for the entire maze."""
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.available_positions:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if any(self.get_tile(x + 4 * dx, y + y0 * dy) == '|' for y0 in range(4)):
                            self.add_connection(x, y, dx, dy)

    def update(self):
        """Updates both the available positions and connections."""
        self.update_available_positions()
        self.update_connections()

    def expand_wall(self, x, y):
        """Expands walls starting from (x, y) recursively."""
        visited = []

        def expand(x, y):
            if (x, y) in visited:
                return 0
            visited.append((x, y))
            count = 0
            if (x, y) in self.connections:
                for x0, y0 in self.connections[(x, y)]:
                    if not all(self.get_tile(x + dx, y + dy) == '|' for dx in range(2) for dy in range(2)):
                        self.add_wall_block(x0, y0)
                        count += 1
                    count += expand(x0, y0)
            return count

        return expand(x, y)

    def add_wall_obstacle(self, extend=False):
        """Adds a wall obstacle at a random position and expands the walls."""
        self.update()
        if not self.available_positions:
            return False

        x, y = random.choice(self.available_positions)
        self.add_wall_block(x, y)
        count = self.expand_wall(x, y)

        if extend:
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            dx, dy = random.choice(directions)
            max_blocks = 4 + (4 if random.random() <= 0.35 else 0)
            for step in range(max_blocks):
                x0, y0 = x + dx * step, y + dy * step
                if (x0, y0) not in self.available_positions:
                    break
                if not all(self.get_tile(x0 + i, y0 + j) == '|' for i in range(2) for j in range(2)):
                    self.add_wall_block(x0, y0)
                    count += 1 + self.expand_wall(x0, y0)
                if step >= 4 and random.random() <= 0.35:
                    dx, dy = -dy, dx

        return True

if __name__ == "__main__":
    maze = Maze(16,  24,  """
        ||||||||||||||||
        |...............
        |...............
        |...............
        |...............
        |...............
        |...............
        |...............
        |...............
        |.........||||||
        |.........||||||
        |.........||||||
        |.........||||||
        |.........||||||
        |...............
        |...............
        |...............
        |...............
        |...............
        |...............
        |...............
        |...............
        |...............
        ||||||||||||||||""")

    if len(sys.argv) > 1 and sys.argv[1] == "-v":
        maze.verbose = True

    # Generate the maze with obstacles
    while maze.add_wall_obstacle(extend=True):
        pass

    # Print the generated maze
    for line in str(maze).splitlines():
        print(line[:16] + line[:16][::-1])