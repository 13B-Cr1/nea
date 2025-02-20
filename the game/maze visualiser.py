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
player_x = (60//TILE_SIZE) * TILE_SIZE 
player_y = (60//TILE_SIZE) * TILE_SIZE 
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
class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.size = TILE_SIZE # It equals 30 in here
        self.type = ""
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
    def draw(self,surface):
        pass


# walltile inherits from Tile
class WallTile(Tile):  
    def __init__(self,x,y):
        super().__init__(x, y)  # Call the constructor in tile class to set x, y
        self.colour = (255, 255, 0)  # Wall colour = yellow
        self.type = "Wall"
    
    def draw(self,surface):
        pygame.draw.rect(surface, self.colour, self.rect)


class PacdotTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.colour = (255, 255, 255)  # Pacdot colour  = white
        self.type = "Pacdot"

    # To draw a circle with radius 4
    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x + self.size // 2, self.y + self.size // 2), 4)

class PowerdotTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.colour = (0,255,255)  # Pacdot colour  =  cyan
        self.type = "Power Pellet"

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
        self.tiles = pygame.sprite.Group()
        self.walls_group = pygame.sprite.Group()  # Group for wall tiles
        self.pacdots_group = pygame.sprite.Group()  # Group for Pac-Dots
        self.powerdots_group = pygame.sprite.Group()  # Group for Power Pellets
        self.ghosthomes_group = pygame.sprite.Group()  # Group for ghost home tiles
        self.create_tiles()
    
    def create_tiles(self):
        for y, row in enumerate(self.map):
            for x, tile_type in enumerate(row):
                if tile_type == 1:
                    tile = WallTile(x * TILE_SIZE, y * TILE_SIZE)
                    self.tiles.add(tile) # .add() method comes from the sprite class
                    self.walls_group.add(tile)
                elif tile_type == 2:
                    tile = PacdotTile(x * TILE_SIZE, y * TILE_SIZE)
                    self.tiles.add(tile)
                    self.pacdots_group.add(tile)
                elif tile_type == 3:
                    tile = PowerdotTile(x * TILE_SIZE, y * TILE_SIZE)
                    self.tiles.add(tile)
                    self.powerdots_group.add(tile)
                elif tile_type == 4:
                    tile = GhosthomeTile(x * TILE_SIZE, y * TILE_SIZE, "region")
                    self.tiles.add(tile)
                    self.ghosthomes_group.add(tile)
                elif tile_type == 5:
                    tile = GhosthomeTile(x * TILE_SIZE, y * TILE_SIZE, "entrance")
                    self.tiles.add(tile)
                    self.ghosthomes_group.add(tile)
    
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


class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, images):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed  # Use a divisor of TILE_SIZE (e.g., 5)
        self.direction = 0  # 0=right, 1=left, 2=up, 3=down
        self.images = images
        self.counter = 0
        self.next_direction = None  # For queued direction changes



    def draw(self, surface):
        if self.direction == 0: # turns right
            surface.blit(self.images[self.counter // 5], (self.x, self.y))
        elif self.direction == 1: # turns left
            surface.blit(pygame.transform.flip(self.images[self.counter // 5], True, False), (self.x, self.y)) # left
        elif self.direction == 2: # turns up
            surface.blit(pygame.transform.rotate(self.images[self.counter // 5], 90), (self.x, self.y)) # up
        elif self.direction == 3: # turns down
            surface.blit(pygame.transform.rotate(self.images[self.counter // 5], 270), (self.x, self.y)) # down
    

    def move(self, direction):
        self.direction = direction
        new_x,new_y = self.x,self.y
        if self.direction == 0:  # right
            new_x = self.x + self.speed
        elif self.direction == 1:  # left
            new_x = self.x - self.speed
        elif self.direction == 2:  # up
            new_y = self.y - self.speed
        elif self.direction == 3:  # down
            new_y = self.y + self.speed

        grid_x = new_x // TILE_SIZE
        grid_y = new_y //TILE_SIZE

        if 0<= grid_x < GRID_WIDTH and  0 <= grid_y < GRID_HEIGHT:
            if GAME_MAP[grid_y][grid_x] != 1:
                self.x = new_x
                self.y = new_y
                
        

    def update(self): # Simple update logic for the animation counter
    
        self.counter += 1
        if self.counter > 19:
            self.counter = 0
    

    

# Draws the board using solid rectangles    
# def draw_board():
#     for y in range(GRID_HEIGHT):
#         for x in range(GRID_WIDTH):
#             rect = pygame.Rect(x*TILE_SIZE,y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
#             if GAME_MAP[y][x] == 1:
#                 pygame.draw.rect(screen, YELLOW, rect)
#             if GAME_MAP[y][x] == 2:
#                 pygame.draw.circle(screen, WHITE , (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), 4)
#             if GAME_MAP[y][x] == 3 and not flicker:
#                 pygame.draw.circle(screen, CYAN, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), 8)   
#             if GAME_MAP[y][x] == 4:
#                 pygame.draw.rect(screen, BLACK, rect)
#             if GAME_MAP[y][x] == 5:
#                 pygame.draw.rect(screen, WHITE, rect)



pacman_rect= pygame.Rect(player_x,player_y, TILE_SIZE,TILE_SIZE)
pacman = Pacman(player_x, player_y, 30, PACMAN_IMAGES)
make_ghost_home()    
place_dots()    
game_map = GameMap(GAME_MAP)
running = True
last_direction = None

while running:
    screen.fill(BLACK)  # Fill the screen with black

    # Draw the map and update the animation counter
    game_map.draw(screen)
    pacman.update()
    
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_UP):
                last_direction = 2  # up
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                last_direction = 1  # left
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                last_direction = 0  # right
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                last_direction = 3  # down
    if last_direction is not None:
        pacman.move(last_direction)
    pacman.draw(screen)  # Draw pacman on the screen
    pygame.display.flip()  # Update the screen
    pygame.time.Clock().tick(30)  # Frame rate (60 FPS)

pygame.quit()

