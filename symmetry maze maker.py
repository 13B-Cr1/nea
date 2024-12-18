
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


def carve_maze(maze,x,y):
    directions = [(0,2),(0,-2),(2,0),(-2,0)]
    random.shuffle(directions)

    for dx,dy in directions:
        nx,ny = x + dx, y + dy
        if 0 < nx < width  and 0 < ny < height and maze[ny][nx] == wall:
            maze[y + dy//2][x + dx//2] = path
            maze[ny][nx] = path
            carve_maze(maze,nx,ny)

def place_start_end(maze, width, height):
    start_x = width // 2
    start_y = height // 2
    maze[start_x][start_y] = "S"
    maze[height - 2][width - 2] = path

def print_maze(maze):
    for row in maze:
        print("".join(row))


def generate_maze():
    maze = initialise_maze(width,height)

    maze[1][1] = path
    carve_maze(maze,1,1)
    add_symmetry(maze,width,height)

    place_start_end(maze,width,height)

    print_maze(maze)

generate_maze()