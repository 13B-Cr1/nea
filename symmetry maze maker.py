
# 18/12/2024
# Making a recursive backtracking algorithm for Pac-man

"""
I'm trying to use a recursive backtracking algorithm along with
with adding symmetry to the maze.
This has to be done
"""

import random

wall = "|"
path  ="."
height = 21
width = 21

def initialise_maze(width,height):
    return[[wall] * width for _ in range(height)]


# This mirrors whatever is on the left side of the maze to the right side

def add_symmetry(maze,width,height):
    for y in range(height):
        for x in range(width//2):
            
            maze[y][width -x -1] = maze[y][x]


"""This is the recursive backtracking algorithm"""
def carve_maze(maze,x,y,available_positions):
    directions = [(0,2),(0,-2),(2,0),(-2,0)]
    random.shuffle(directions)

    for dx,dy in directions:
        nx,ny = x + dx, y + dy
        if 0 < nx < width  and 0 < ny < height and maze[ny][nx] == wall:
            maze[y + dy//2][x + dx//2] = path
            maze[ny][nx] = path # this chosen coordinates becomes part of a path
            available_positions.append((nx,ny))
            carve_maze(maze,nx,ny,available_positions)


def add_random_obstacles(maze,num_obstacles = 5):
    for _ in range(num_obstacles):
        x = random.randint(1,width - 2)
        y = random.randint(1, height - 2)
        if maze[y][x] == path:
            maze[y][x] = wall

def place_start_end(maze, width, height):
    start_x = width // 2
    start_y = height // 2
    maze[start_x][start_y] = "S"
    maze[height - 2][width - 2] = path




def print_maze(maze):
    for row in maze:
        print("".join(row))


""" This ensures interconnected paths.
    It uses BFS, which checks if all accebsible areas are reachable from the starting point"""
def bfs(maze,start_x, start_y):
    visited = set()
    queue = [(start_x,start_y)]
    visited.add((start_x,start_y))

    while queue:
        x,y = queue.pop(0)
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == path and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny))

    for y in range(height):
        for x in range(width):
            if maze[y][x] == path and (x,y) not in visited:
                return False # Returns false if an isolated spot is found
            
    return True


"""This runs the maze generator"""
def generate_maze():
    maze = initialise_maze(width,height)
    
    available_positions = [(1,1)] # This keeps the available positions that wre carved out


    maze[1][1] = path
    carve_maze(maze,1,1,available_positions)
    add_symmetry(maze,width,height)

    place_start_end(maze,width,height)
    if not bfs(maze,1,1):
        print("Maze has isolated areas")
        print_maze(maze)
        return #Exix if the maze is not fully connected
    
    add_random_obstacles(maze)
    

generate_maze()