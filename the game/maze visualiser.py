
"""
rect = Pygame.rect(x_coordinate, y_coordinate, width, height)
circle = Pygame
"""

import random
import pygame
fps = 60
timer = pygame.time.Clock()
# Game map
GAME_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Grid dimensions
GRID_WIDTH = 32
GRID_HEIGHT = 24

# Calculate screen size\
TILE_SIZE = 30
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE * 1
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE * 1

# Colours
YELLOW = (255,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

# Pacman images
PACMAN_IMAGES = []
for i in range(1,5):
    PACMAN_IMAGES.append(pygame.transform.scale(pygame.image.load(f"assets/{i}.png"),(25,25)))

# Pacman position
player_x = 15 * TILE_SIZE
player_y = 17 * TILE_SIZE
direction = 0
counter = 0
# Initialise Pygame
pygame.init()
pygame.display.set_caption("Pacman visualiser")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# This places Pac-dots into the matrix GAME_MAP
def place_dots():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
        
            if GAME_MAP[y][x] == 0:
                if random.random() < 0.7: # This adds pacdots
                    GAME_MAP[y][x] = 2
                elif random.random() < 0.05: # This adds power pellets
                    GAME_MAP[y][x] = 3

# Make a ghost area location
def make_ghost_home():
    for y in range(10,13):
        for x in range(11,21):
            GAME_MAP[y][x] = 4

    for x in range(14,18):
        GAME_MAP[9][x] = 5
    
# Put Pacman on the screen
def put_Pacman_on_screen():
    if direction == 0:
        screen.blit(PACMAN_IMAGES[counter // 5], (player_x,player_y))
    if direction == 1:
        screen.blit(pygame.transform.flip(PACMAN_IMAGES[counter // 5], True, False),(player_x,player_y))
    if direction == 2:
        screen.blit(pygame.transform.rotate(PACMAN_IMAGES[counter // 5], 90), (player_x,player_y))
    if direction == 3:
        screen.blit(pygame.transform.rotate((PACMAN_IMAGES[counter // 5],270), (player_x,player_y)))
    

run = True
while run:
    timer.tick(fps)
    make_ghost_home()
    place_dots()
    put_Pacman_on_screen()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x*TILE_SIZE,y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if GAME_MAP[y][x] == 1:
                pygame.draw.rect(screen, YELLOW, rect)
            if GAME_MAP[y][x] == 2:
                pygame.draw.circle(screen, WHITE , (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), 4)
            if GAME_MAP[y][x] == 3:
                pygame.draw.circle(screen, BLUE, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), 8)   
            if GAME_MAP[y][x] == 4:
                pygame.draw.rect(screen, BLACK, rect)
            if GAME_MAP[y][x] == 5:
                pygame.draw.rect(screen, WHITE, rect)
    pygame.display.flip()

    # options to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # this closes the program when I press the esc
                run = False
pygame.quit()