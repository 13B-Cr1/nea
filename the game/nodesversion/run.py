
from MazeOfNodes import NodeGroup
from constants import * 
import pygame
def startGame(self):
    self.setBackground()
    self.nodes = NodeGroup()
    self.nodes.setupTestNodes()
    # self.pacman = Pacman()

def render(self):
    self.screen.blit(self.background, (0,0))
    self.nodes.render(self.screen)
    self.pacman.render(self.screen)
    pygame.display.update()


class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup()
        self.nodes.setupTestNodes()
    

    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.checkEvents()
        self.render()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.nodes.render(self.screen)
        pygame.display.update()

if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()


