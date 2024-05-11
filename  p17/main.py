import pygame
import random

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100
pygame.init()
self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Game:
    def __init__(self):
        pass

    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

    def run(self):
        pass


# Start game
if __name__ == '__main__':
    game = Game()
    game.init()