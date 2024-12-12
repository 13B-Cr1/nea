# 20/11/2024
# Making a recursive backtracking algorithm

"""
Testing to see if the algorithm can build a valid maze:
- No gaps in the outside
- A ghost area zone reserved for ghosts (labelled with G)
- no "singular" routes
"""



import random

# maze size
maze_size = 21
maze = [["|"] * maze_size for _ in range(maze_size)]

# directions for carving the maze
directions = [(-2, 0), (2, 0), (0, -2), (0, 2)] # this will be used by a function to visit cells by moving left, right, up or down

#  the fixed ghost spawn area
ghost_home_size = 3
ghost_home_x = 9 # X coordinate for ghost home
ghost_home_y = 9 # Y coordinate for ghost home 

def is_within_bounds(x,y):
    return 0 < x < maze_size - 1 and 0 < y < maze_size - 1


def generate_maze(maze,x,y): 
    maze[y][x] = " "

    random.shuffle(directions)

    for direction in directions:
        dx,dy = direction

        nx, ny = x + dx, y + dy

        if is_within_bounds(nx,ny) and maze[ny][nx] == "|":
            accessible_paths = sum(
                1 for ddx,ddy in directions
                if is_within_bounds(nx+ddx,ny+ddy) and maze[ny+ddy][nx+ddx] == " "
            )
            if accessible_paths == 1:
                maze[ny][nx] = " "
                maze[y + dy//2 ][x + dx//2] = " "
                generate_maze(maze,nx,ny)
        # if 0<nx < len(maze[0]) and 0<ny<len(maze) and maze[ny][nx] == "|":
        #     maze[ny][nx] = " "
        #     maze[y +dy// 2 ][x +dx//2] = " "

        #     generate_maze(maze,nx,ny)



# this creates the ghost area where the ghosts will spawn from
def create_ghost_area(): 
    for gy in range(ghost_home_y, ghost_home_y + ghost_home_size):
        for gx in range(ghost_home_x - ghost_home_size //2, ghost_home_x + ghost_home_size // 2 + 1):
            maze[gy][gx] = "G"

create_ghost_area()


#start_x, start_y = random.randrange(1 ,maze_size,2), random.randrange(1,maze_size, 2)


#if the start_x value and start_y lie within the ghost area, new values for x and y will be chosen
def get_start_position():
    while True:
        start_x, start_y = random.randrange(1,maze_size,2), random.randrange(1,maze_size,2)
        if not (ghost_home_x - ghost_home_size // 2 <= start_x <= ghost_home_x + ghost_home_size // 2 and
                ghost_home_y - ghost_home_size // 2 <= start_y <= ghost_home_y + ghost_home_size // 2):
            return start_x, start_y

    
 
#generate maze
start_x, start_y = get_start_position()
generate_maze(maze,start_x,start_y)


for row in maze:
    print("".join(row))