import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for screen size and grid dimensions
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20  # Size of each cell in the grid
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Grid")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw the grid
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, HEIGHT))  # Vertical lines
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (WIDTH, y))  # Horizontal lines

# Main game loop
while True:
    screen.fill((0, 0, 0))  # Clear screen with black

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 frames per second
    clock.tick(60)
