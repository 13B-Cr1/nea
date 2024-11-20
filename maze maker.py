## 20/11/2024
# Making a recursive backtracking algorithm

"""
Testing to see if the algorithm can build a valid maze:
- No gaps in the outside
- A ghost area zone reserved for ghosts (labelled with G)
- no "singular" routes
"""

directions = [(-2, 0), (2, 0), (0, -2), (0, 2)] #left, right, up or down
def generate_maze(maze,x,y): 
    maze[y][x] = " "
    random.shuffle(directions)
    for direction in directions:
        dx,dy = direction
        nx, ny = x + dx, y + dy

        if 0< nx < len(maze[0]) and 0<ny<len(maze) and maze[ny][nx] == "#":
            maze[ny][nx] = " "
            maze[y +dy// 2 ][x +dx//2] = " "

            generate_maze(maze,nx,ny)


def create_empty_maze(size):
    return [["#"] * size for _ in range(size)] # creates a 2d array with #



# this creates the ghost area where the ghosts will spawn from
def create_ghost_home(maze,x,y,size):
    
    ghost_area = [] # It keeps a list of the coordinates of the points inside the ghost home
    for gy in range(y, y + size):
        for gx in range(x - size // 2, x + size // 2 + 1):
            if 0 <= gy < len(maze) and 0 <= gx < len(maze[0]):  # Boundary check
                maze[gy][gx] = "G"
                ghost_area.append((gx, gy))
    return ghost_area


import random
def get_starting_point(maze,ghost_home):

    """ This finds a valid starting point outside the ghost home"""
    maze_size = len(maze)

    while True:
        x, y = random.randrange(1 ,maze_size,2), random.randrange(1,maze_size, 2)
        if (x,y) not in ghost_home:
            return x,y
        


#if the start_x value and start_y lie within the ghost area, new values for x and y will be chosen

def carve_path(maze,x,y,nx,ny):

    maze[y][x]= " "
    maze[ny][nx] = " "
    maze[(y+ny)//2][(x+nx)//2] = " "

 
def display_maze(maze):
    for row in maze:
        print("".join(row))


def main():
    #generate maze
    maze_size = 17
    maze = create_empty_maze(maze_size)
    ghost_home = create_ghost_home(maze,5,5,3)
    start_x,start_y = get_starting_point(maze,ghost_home)

    generate_maze(maze,start_x,start_y)
    display_maze(maze)

main()
