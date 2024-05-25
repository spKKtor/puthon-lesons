import pygame
import random
import sys

SCREEN_WIDTH = 960  # TODO: Розмір має змінитись (можливо)
SCREEN_HEIGHT = 540 #
IMAGES_PATH_MENU = 'images/menu/'
IMAGES_PATH_BG = 'images/background/'
IMAGES_PATH_PLAYER = 'images/Player/'
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
        self.btn()


    def start_btn(self, color=(0, 0, 0)):
        font = pygame.font.Font(FONTS_PATH + 'PoetsenOne-Regular.ttf', 52)
        text = font.render('START', True, color)
        screen.blit(text, (87, 100))

    def exit_btn(self, color=(0, 0, 0)):
        font = pygame.font.Font(FONTS_PATH + 'PoetsenOne-Regular.ttf', 52)
        text = font.render('EXIT', True, color)
        screen.blit(text, (87, 150))

    # TODO: ЗРОБИШ КЛІК МИШКИ
    def click(self):
        btn = pygame.mouse.get_pressed()

        if btn[0] and self.pos_start():
            return 'start'
        elif btn[0] and self.pos_exit():
            return 'exit'

        return None

    def pos_start(self):
        pos = pygame.mouse.get_pos()
        #print(pos)
        if ((pos[0] > 90 and pos[0] < 250) and (pos[1] > 110 and pos[1] < 150)):
            return True
        return False

    def pos_exit(self):
        pos = pygame.mouse.get_pos()
        if ((pos[0] > 90 and pos[0] < 200) and (pos[1] > 165 and pos[1] < 205)):
            return True
        return False

    def btn(self):
        if self.pos_start():
            self.start_btn((225, 225, 225))
        else:
            self.start_btn()

        if self.pos_exit():
            self.exit_btn((255, 255, 255))
        else:
              self.exit_btn()

#Задній фон
class Background:
    img = None

    def __init__(self):
        self.add()

    def add(self):
        self.img = pygame.image.load(IMAGES_PATH_BG + 'bg_03.png')

    def draw(self):
        screen.blit(self.img, (0, 0))

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - 100
        img = pygame.image.load(IMAGES_PATH_PLAYER + 'kvas52.png')
        self.img = pygame.transform.scale(img, (60,60))

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        pass
    def left(self):
        pass

    def right(self):
        pass
    def shoot(self):
        pass

class Game:
    game_run: bool = False

    def __init__(self):
        self.menu = MainMenu()
        self.bg = Background()
        self.player = Player()

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.menu.click()
                    if action == 'start':
                        self.run()
                    elif action == 'exit':
                        self.quit()

            self.menu.draw()
            pygame.display.update()

    def run(self):
        self.game_run =True
        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_run = False
                        break

            self.bg.draw()
            self.player.draw()
            pygame.display.update()


# Start game
if __name__ == '__main__':
    game = Game()
    game.init()
