import random

# Constants
wall = "|"
path = "."
height = 21
width = 21

# Initialize the maze with walls
def initialise_maze(width, height):
    return [[wall] * width for _ in range(height)]

# Add symmetry to the maze
def add_symmetry(maze, width, height):
    for y in range(height):
        for x in range(width // 2):
            maze[y][width - x - 1] = maze[y][x]

# Check if coordinates are valid
def valid(x, y):
    return 0 < x < width and 0 < y < height

# Get the tile at a given coordinate
def get_tile(maze, x, y):
    return maze[y][x] if valid(x, y) else None

# Set the tile at a given coordinate
def set_tile(maze, x, y, tile):
    if valid(x, y):
        maze[y][x] = tile

# Add a 2x2 wall block at the given coordinates
def add_wall_block(maze, x, y):
    for dx in range(2):
        for dy in range(2):
            set_tile(maze, x + 1 + dx, y + 1 + dy, wall)

# Update connections between path tiles
def update_connections(maze):
    global connections
    connections = {}
    for y in range(height):
        for x in range(width):
            if get_tile(maze, x, y) == path:
                if valid(x + 1, y) and get_tile(maze, x + 1, y) == path:
                    connections.setdefault((x, y), []).append((x + 1, y))
                if valid(x - 1, y) and get_tile(maze, x - 1, y) == path:
                    connections.setdefault((x, y), []).append((x - 1, y))
                if valid(x, y + 1) and get_tile(maze, x, y + 1) == path:
                    connections.setdefault((x, y), []).append((x, y + 1))
                if valid(x, y - 1) and get_tile(maze, x, y - 1) == path:
                    connections.setdefault((x, y), []).append((x, y - 1))

# Expand walls starting from (x, y) recursively
def expand_wall(maze, x, y):
    visited = []

    def expand(x, y):
        if (x, y) in visited:
            return 0
        visited.append((x, y))
        count = 0
        if (x, y) in connections:
            for x0, y0 in connections[(x, y)]:
                if not all(get_tile(maze, x + dx, y + dy) == wall for dx in range(2) for dy in range(2)):
                    add_wall_block(maze, x0, y0)
                    count += 1
                count += expand(x0, y0)
        return count

    return expand(x, y)

# Add a wall obstacle at a random position and expand the walls
def add_wall_obstacle(maze, extend=False):
    update_connections(maze)
    if not available_positions:
        return False

    x, y = random.choice(available_positions)
    add_wall_block(maze, x, y)
    count = expand_wall(maze, x, y)

    if extend:
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        dx, dy = random.choice(directions)
        max_blocks = 4 + (4 if random.random() <= 0.35 else 0)
        for step in range(max_blocks):
            x0, y0 = x + dx * step, y + dy * step
            if (x0, y0) not in available_positions:
                break
            if not all(get_tile(maze, x0 + i, y0 + j) == wall for i in range(2) for j in range(2)):
                add_wall_block(maze, x0, y0)
                count += 1 + expand_wall(maze, x0, y0)
            if step >= 4 and random.random() <= 0.35:
                dx, dy = -dy, dx

    return True

# Print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

if __name__ == "__main__":
    maze = initialise_maze(width, height)
    add_symmetry(maze, width, height)
    available_positions = [(x, y) for y in range(height) for x in range(width) if get_tile(maze, x, y) == path]
    while add_wall_obstacle(maze, extend=True):
        pass
    print_maze(maze)