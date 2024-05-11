import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
IMAGES_PATH = 'images/'
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Game:
    background = None
    game_run: bool = False
    def __init__(self):
        pass

    def menu(self):
        pass

    def add_background(self):
        self.background = pygame.image.load(IMAGES_PATH + 'bg_03.png')
        screen.blit(self.background,(0, 0))

    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.run()

            screen.fill((50, 50, 50))
            pygame.display.update()
    def run(self):

        self.game_run =True
        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        break


# Start game
if __name__ == '__main__':
    game = Game()
    game.init()