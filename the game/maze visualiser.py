
"""
rect = Pygame.rect(x_coordinate, y_coordinate, width, height)
circle = Pygame
"""

import random
import pygame
# other stuff
fps = 60
timer = pygame.time.Clock()
counter = 0
flicker = False

# Game map
GAME_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
def make_ghost_home():
    for y in range(10,13):
        for x in range(11,21):
            GAME_MAP[y][x] = 4

    for x in range(14,18):
        GAME_MAP[9][x] = 5

# Grid dimensions
GRID_WIDTH = 32
GRID_HEIGHT = 24

# Calculate screen size\
TILE_SIZE = 30
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE * 1
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE * 1

# Colours
YELLOW = (255,255,0)
CYAN = (0,255,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

# Pacman images
PACMAN_IMAGES = []
for i in range(1,5):
    PACMAN_IMAGES.append(pygame.transform.scale(pygame.image.load(f"assets/{i}.png"),(25,25)))

# Pacman position
player_x = 15 * TILE_SIZE
player_y = 17 * TILE_SIZE
# direction = 0
turns = [False, False,False,False]
# direction_command = 0
player_speed = 2
# Initialise Pygame
pygame.init()
pygame.display.set_caption("Pacman visualiser")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# This places Pac-dots into the matrix GAME_MAP
def place_dots():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
        
            if GAME_MAP[y][x] == 0:
                if random.random() < 0.80: # This adds pacdots
                    GAME_MAP[y][x] = 2
                elif random.random() < 0.05: # This adds power pellets
                    GAME_MAP[y][x] = 3

# class for a tile
class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = TILE_SIZE # It equals 30 in here
    def draw(self,surface):
        pass


# walltile inherits from Tile
class WallTile(Tile):  
    def __init__(self,x,y):
        super().__init__(x, y)  # Call the constructor in tile class to set x, y
        self.colour = (255, 255, 0)  # Wall colour = yellow
    
    def draw(self,surface):
        pygame.draw.rect(surface, self.colour, pygame.Rect(self.x, self.y, self.size, self.size))


class PacdotTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.colour = (255, 255, 255)  # Pacdot colour  = white

    # To draw a circle with radius 4
    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x + self.size // 2, self.y + self.size // 2), 4)

class PowerdotTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.colour = (0,255,255)  # Pacdot colour  =  cyan

    # To draw a circle with radius 8
    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x + self.size // 2, self.y + self.size // 2), 8)

class GhosthomeTile(Tile):
    def __init__(self, x, y,type):
        super().__init__(x, y)
        self.type = type
    # Forms an empty region
    def draw(self, surface):
        if self.type == "entrance":
            pygame.draw.rect(surface, WHITE, pygame.Rect(self.x, self.y, self.size, self.size))
        if self.type == "region":
            pygame.draw.rect(surface, BLACK, pygame.Rect(self.x, self.y, self.size, self.size))
class GameMap:
    def __init__(self, game_map):
        self.map = game_map
        self.tiles = self.create_tiles()
    
    def create_tiles(self):
        tiles = []
        for y, row in enumerate(self.map):
            for x, tile_type in enumerate(row):
                if tile_type == 1:
                    tiles.append(WallTile(x * TILE_SIZE, y * TILE_SIZE))
                elif tile_type == 2:
                    tiles.append(PacdotTile(x * TILE_SIZE, y * TILE_SIZE))
                elif tile_type == 3:
                    tiles.append(PowerdotTile(x * TILE_SIZE, y * TILE_SIZE))
                elif tile_type == 4:
                    tiles.append(GhosthomeTile(x * TILE_SIZE, y * TILE_SIZE, "region" ))
                elif tile_type == 5:
                    tiles.append(GhosthomeTile(x * TILE_SIZE, y * TILE_SIZE, "entrance" ))
        return tiles
    
    """
    PURPOSE: 
    - the parameter represents the sequence(in this case: the map)
    - the y gives the position of the sublist
    - row is the sublist

    - x represents the position of the tile in the sublist
    - tile_type could be a wall/pacdot/walldot
    """
    def draw(self,surface):
        for tile in self.tiles:
            tile.draw(surface)


class Pacman:
    def __init__(self, x, y, speed, images):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 0  # 0 = right, 1 = left, 2 = up, 3 = down
        self.images = images
        self.counter = 0

    def draw(self, surface):
        if self.direction == 0:
            surface.blit(self.images[self.counter // 5], (self.x, self.y))
        elif self.direction == 1:
            surface.blit(pygame.transform.flip(self.images[self.counter // 5], True, False), (self.x, self.y))
        elif self.direction == 2:
            surface.blit(pygame.transform.rotate(self.images[self.counter // 5], 90), (self.x, self.y))
        elif self.direction == 3:
            surface.blit(pygame.transform.rotate(self.images[self.counter // 5], 270), (self.x, self.y))

    def move(self, direction):
        # Update direction and position based on player input
        self.direction = direction
        if self.direction == 0:  # right
            self.x += self.speed
        elif self.direction == 1:  # left
            self.x -= self.speed
        elif self.direction == 2:  # up
            self.y -= self.speed
        elif self.direction == 3:  # down
            self.y += self.speed

    def update(self):
        # Simple update logic for the animation counter
        self.counter += 1
        if self.counter > 19:
            self.counter = 0
# Draws the board using solid rectangles    
def draw_board():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x*TILE_SIZE,y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if GAME_MAP[y][x] == 1:
                pygame.draw.rect(screen, YELLOW, rect)
            if GAME_MAP[y][x] == 2:
                pygame.draw.circle(screen, WHITE , (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), 4)
            if GAME_MAP[y][x] == 3 and not flicker:
                pygame.draw.circle(screen, CYAN, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), 8)   
            if GAME_MAP[y][x] == 4:
                pygame.draw.rect(screen, BLACK, rect)
            if GAME_MAP[y][x] == 5:
                pygame.draw.rect(screen, WHITE, rect)
    
# Put Pacman on the screen
def put_Pacman_on_screen():
    if direction == 0:
        screen.blit(PACMAN_IMAGES[counter // 5], (player_x,player_y))
    if direction == 1:
        screen.blit(pygame.transform.flip(PACMAN_IMAGES[counter // 5], True, False),(player_x,player_y))
    if direction == 2:
        screen.blit(pygame.transform.rotate(PACMAN_IMAGES[counter // 5], 90), (player_x,player_y))
    if direction == 3:
        screen.blit(pygame.transform.rotate(PACMAN_IMAGES[counter // 5],270), (player_x,player_y))
    

def check_position(centre_x, centre_y):
    turns = [False, False, False, False]
    num1 = GRID_HEIGHT
    num2 = GRID_WIDTH
    num3 = 15

    if centre_x // 30 < 32:
        if direction == 0:
            if GAME_MAP[centre_y // num1][(centre_x- num3) // num2] != (1 or 5):
                turns[1] = True
        if direction == 1:
            if GAME_MAP[centre_y // num1][(centre_x + num3) // num2] != (1 or 5):
                turns[0] = True
        if direction == 2:
            if GAME_MAP[(centre_y + num3) // num1][(centre_x) // num2] != (1 or 5):
                turns[3] = True

        if direction == 3:
            if GAME_MAP[(centre_y- num3) // num1][(centre_x) // num2] != (1 or 5):
                turns[2] = True

        if direction == (0 or 1):
            if 12 <= centre_x % num2 <= 18:
                if GAME_MAP[(centre_y + num3) // num1][centre_x // num2 ] < (1 or 5):
                    turns[3] = True
                if GAME_MAP[(centre_y - num3) // num1][centre_x // num2 ] < (1 or 5):
                    turns[2] = True

            if 12 <= centre_x % num1 <= 18:
                if GAME_MAP[(centre_y) // num1][centre_x // num2 ] < (1 or 5):
                    turns[3] = True
                if GAME_MAP[(centre_y) // num1][centre_x // num2 ] < (1 or 5):
                    turns[2] = True
        
        if direction == (2 or 3):
            if 12 <= centre_x % num2 <= 18:
                if GAME_MAP[(centre_y + num3) // num1][centre_x // num2 ] < (1 or 5):
                    turns[3] = True
                if GAME_MAP[(centre_y - num3) // num1][centre_x // num2 ] < (1 or 5):
                    turns[2] = True

            if 12 <= centre_y % num1 <= 18:
                if GAME_MAP[centre_y // num1][centre_x - num2 // num2 ] < (1 or 5):
                    turns[1] = True
                if GAME_MAP[centre_y // num1][centre_x + num2 // num2 ] < (1 or 5):
                    turns[0] = True
        
        if direction == (0 or 1):
            if 12 <= centre_x % num2 <= 18:
                if GAME_MAP[(centre_y + num1) // num1][centre_x // num2 ] < (1 or 5):
                    turns[3] = True
                if GAME_MAP[(centre_y - num1) // num1][centre_x // num2 ] < (1 or 5):
                    turns[2] = True

            if 12 <= centre_y % num1 <= 18:
                if GAME_MAP[centre_y // num1][centre_x - num2 // num2 ] < (1 or 5):
                    turns[1] = True
                if GAME_MAP[centre_y // num1][centre_x + num2 // num2 ] < (1 or 5):
                    turns[0] = True

    return turns

def move_player(player_x, player_y):

    if direction == 0 and turn_allowed[0]:
        player_x += player_speed
    if direction == 1 and turn_allowed [1]:
        player_x -= player_speed
    if direction == 2 and turn_allowed[2]:
        player_y -= player_speed
    if direction == 3 and turn_allowed[3]:
        player_x += player_speed

    return player_x, player_y
    
    





# run = True
# make_ghost_home()
# place_dots()
# while run:
#     timer.tick(fps)
#     if counter < 19:
#         counter += 1
#         if counter > 10 :
#             flicker = False
#     else:
#         counter = 0
#         flicker = True

#     screen.fill(BLACK)
#     draw_board()
#     put_Pacman_on_screen()
#     centre_x = player_x + 13
#     centre_y = player_y + 13
#     pygame.draw.circle(screen, WHITE, (centre_x, centre_y), 5)
#     turn_allowed = check_position(centre_x,centre_y)
#     player_x, player_y = move_player(player_x,player_y)

#     pygame.display.flip()

#     # options to close the game
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE: # this closes the program when I press the esc
#                 run = False
#             if event.key == pygame.K_RIGHT :
#                 direction_command = 0
#             if event.key == pygame.K_LEFT :
#                 direction_command = 1
#             if event.key == pygame.K_UP :
#                 direction_command = 2
#             if event.key == pygame.K_DOWN :
#                 direction_command = 3

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_ESCAPE: # this closes the program when I press the esc
#                 run = False
#             if event.key == pygame.K_RIGHT and direction_command == 0 :
#                 direction_command = direction
#             if event.key == pygame.K_LEFT and direction_command :
#                 direction_command = direction
#             if event.key == pygame.K_UP and direction_command:
#                 direction_command = direction
#             if event.key == pygame.K_DOWN and direction_command :
#                 direction_command = direction
            
#         for i in range(4):
#             if direction_command == i and turn_allowed[i]:
#                 direction = i
pacman = Pacman(player_x, player_y, player_speed, PACMAN_IMAGES)
make_ghost_home()    
place_dots()    
game_map = GameMap(GAME_MAP)
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black
   
    
    # Draw the map
    game_map.draw(screen)
    pacman.update()  # Update animation counter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_RIGHT :
                pacman.move(0)
            if event.key == pygame.K_LEFT :
                pacman.move(1)
            if event.key == pygame.K_UP :
                pacman.move(2)
            if event.key == pygame.K_DOWN :
                pacman.move(3)
    # Move pacman based on direction command
    pacman.draw(screen)  # Draw pacman on the screen
    
    pygame.display.flip()  # Update the screen
    pygame.time.Clock().tick(30)  # Frame rate (30 FPS)

pygame.quit()
            
