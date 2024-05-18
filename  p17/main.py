import pygame
import random
import sys

SCREEN_WIDTH = 900 # TODO: Розмір має змінитись (можливо)
SCREEN_HEIGHT = 800 #
IMAGES_PATH_MENU = 'images/menu/'
IMAGES_PATH_BG = 'images/background/'
IMAGES_PATH_PLAYER = 'images/'
IMAGES_PATH_ENEMY = 'images/'
FONTS_PATH = 'fonts/'
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Головне меню
class MainMenu:
    bg = None
    panel = None

    def __init__(self):
        self.add_bg()
        self.add_panel()

    def add_bg(self):
        img = pygame.image.load(IMAGES_PATH_MENU + 'bg-03.jpg')
        self.bg = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def add_panel(self):
        panel = pygame.image.load(IMAGES_PATH_MENU + 'Window.png')
        self.panel = pygame.transform.scale(panel, (300, 300))

    def draw(self):
        screen.blit(self.bg, (0, 0))
        screen.blit(self.panel, (20, 20))
        self.start_btn()
        self.exit_btn()


    def start_btn(self):
        font = pygame.font.Font(FONTS_PATH + 'PoetsenOne-Regular.ttf', 52)
        text = font.render('START', True, (0, 0, 0))
        screen.blit(text, (87, 100))

    def exit_btn(self):
        font = pygame.font.Font(FONTS_PATH + 'PoetsenOne-Regular.ttf', 52)
        text = font.render('EXIT', True, (0, 0, 0))
        screen.blit(text, (87, 150))

    # TODO: ЗРОБИШ КЛІК МИШКИ
    def click(self):
        pos = pygame.mouse.get_pos()
        btn = pygame.mouse.get_pressed()

        if btn[0] and (pos[0]):
            pass

#Задній фон
class Background:
    img = None

    def __init__(self):
        self.add()

    def add(self):
        self.img = pygame.image.load(IMAGES_PATH_BG + 'bg_03.png')

    def draw(self):
        screen.blit(self.img, (0, 0))


class Game:
    game_run: bool = False

    def __init__(self):
        self.menu = MainMenu()
        self.bg = Background()

    def quit(self):
        pygame.quit()
        sys.exit()

    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.run()

            self.menu.draw()
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
