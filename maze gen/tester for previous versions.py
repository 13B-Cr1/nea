import random

# Maze Generator using recursive backtracking
def generate_maze(width, height):
    # Initialize the maze with walls
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    # Helper function to check if a cell is within bounds and empty
    def in_bounds(x, y):
        return 0 <= x < height and 0 <= y < width

    # Recursive backtracking function to carve out paths
    def carve_path(x, y):
        maze[x][y] = ' '  # Mark the current cell as a path
        
        # Directions to move in the maze (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)  # Randomize directions to ensure a random maze
        
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2  # Move two steps in the chosen direction
            if in_bounds(nx, ny) and maze[nx][ny] == '#':  # If it's a wall, carve a path
                maze[x + dx][y + dy] = ' '  # Carve the wall between the two cells
                carve_path(nx, ny)  # Recursively carve the new cell

    # Start carving from the top-left corner of the maze
    carve_path(1, 1)
    
    # Ensure the center is a path (for ghosts' fixed spot)
    center_x, center_y = height // 2, width // 2
    maze[center_x][center_y] = ' '  # Mark the center as an open path

    # Return the generated maze
    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# Example usage:
maze_width, maze_height = 21, 21  # Maze size (odd numbers for better carving)
maze = generate_maze(maze_width, maze_height)
print_maze(maze)
