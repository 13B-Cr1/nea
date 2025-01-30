import random

# Directions for BFS (up, down, left, right)
DIRECTIONS = [(-2, 0), (2, 0), (0, -2), (0, 2)]  # Move in steps of 2 to ensure walls are intact

def initialise_maze(width, height):
    """Create an initial maze filled with walls ('|')."""
    return [['|' for _ in range(width)] for _ in range(height)]

def valid(x, y, width, height):
    """Check if the given (x, y) coordinates are within maze bounds."""
    return 0 <= x < width and 0 <= y < height

def bfs(maze, start_x, start_y, width, height):
    """Ensure all paths are interconnected using BFS."""
    visited = set()
    queue = [(start_x, start_y)]
    visited.add((start_x, start_y))

    while queue:
        x, y = queue.pop(0)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if valid(nx, ny, width, height) and (nx, ny) not in visited and maze[ny][nx] == '.':
                visited.add((nx, ny))
                queue.append((nx, ny))

    # Return False if there are any isolated paths
    for y in range(height):
        for x in range(width):
            if maze[y][x] == '.' and (x, y) not in visited:
                return False
    return True

def carve_maze_bfs(maze, start_x, start_y, width, height):
    """Carve paths in the maze using BFS starting from (start_x, start_y)."""
    queue = [(start_x, start_y)]
    maze[start_y][start_x] = '.'  # Mark the starting point as a path

    while queue:
        x, y = queue.pop(0)
        random.shuffle(DIRECTIONS)  # Shuffle directions to introduce randomness

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            # If the new position is valid and it's a wall, break it down to make a path
            if valid(nx, ny, width, height) and maze[ny][nx] == '|':
                maze[ny][nx] = '.'  # Mark the neighboring cell as a path
                # We also need to break the wall in between (e.g. the 2x1 space between paths)
                maze[y + dy // 2][x + dx // 2] = '.'  # Break the wall in between
                queue.append((nx, ny))  # Add the new position to the BFS queue

def add_symmetry(maze, width, height):
    """Mirror the left half of the maze to the right half to create symmetry."""
    for y in range(height):
        for x in range(width // 2):
            maze[y][width - x - 1] = maze[y][x]

def update_available_positions(maze, width, height):
    """Update the list of positions where new 2x2 wall blocks can be added."""
    available_positions = []
    for y in range(1, height - 1, 2):
        for x in range(1, width - 1, 2):
            # Check if a 2x2 wall block can fit at position (x, y)
            if maze[y][x] == '.' and maze[y + 1][x] == '.' and maze[y][x + 1] == '.' and maze[y + 1][x + 1] == '.':
                available_positions.append((x, y))
    return available_positions

def add_wall_block(maze, x, y):
    """Adds a 2x2 block of walls at the given coordinates (x, y)."""
    for dx in range(2):
        for dy in range(2):
            maze[y + dy][x + dx] = '|'

def generate_maze(width, height):
    """Generate the maze and ensure it's interconnected using BFS."""
    maze = initialise_maze(width, height)

    # Start BFS carving from (1, 1), ensuring walls are intact but paths are carved
    start_x, start_y = 1, 1  # Starting point for BFS carving
    maze[start_y][start_x] = '.'  # Mark the starting point as a path
    carve_maze_bfs(maze, start_x, start_y, width, height)

    # Apply symmetry
    add_symmetry(maze, width, height)

    # Ensure all paths are interconnected
    if not bfs(maze, start_x, start_y, width, height):
        print("Maze is disconnected, regenerating...")
        return generate_maze(width, height)  # Retry if disconnected

    # Add 2x2 wall blocks in random locations, ensuring they fit
    available_positions = update_available_positions(maze, width, height)
    for _ in range(10):  # Try to add 10 wall blocks
        if available_positions:
            x, y = random.choice(available_positions)
            add_wall_block(maze, x, y)

    # Print the generated maze
    for row in maze:
        print("".join(row))

# Example usage:
generate_maze(30, 21)
