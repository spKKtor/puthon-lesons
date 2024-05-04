import pygame
import random

IMAGES_PATH: str = 'images/'
screen_width: int = 600
screen_height: int = 700

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


class Wizard:
    x: int = 0
    x: int = 0
    y: int = 500
    width: int = 0
    height: int = 0
    speed: int = 10
    image_name = '1_IDLE_000.png'
    image_surface = None
    player_move : str = ''

    def __init__(self):
        self.image_surface = pygame.image.load(IMAGES_PATH + self.image_name)
        self.width = self.image_surface.get_width()
        self.width = self.image_surface.get_height()
        self.x = int(screen_width / 2 - self.width / 2)

    def show(self):
        screen.blit(self.image_surface, (self.x, self.y))

    def move(self, direction: str):
        if direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.move_right()

    def move_left(self):
        if self.x - self.speed >= 0:
            self.x -= self. speed
        else:
            self.x = 0

    def move_right(self):
        if self.x + self.speed <= screen_width - self.width:
            self.x += self.speed
        else:
            self.x = screen_width - self.width

class Diamond:
    x: int = 0
    y: int = 0
    speed: int = 0
    image = None

    def __init__(self, image):
        self.image = image
        self.x = random.randint(0, screen_width - 40)
        self.speed = random.randint(2, 5)

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def fall(self):
        self.y += self.speed


class Diamonds:
    diamonds_image: list = []
    diamonds_list: list = []

    def __init__(self):
        self.load_images()

    def load_images(self):
        for i in ('8.png','9.png', '11.png' ):
            self.diamonds_image.append(pygame.image.load(IMAGES_PATH + i))

    def add(self):
        image = self.diamonds_image[random.randint(0,2)]
        self.diamonds_list.append(Diamond(image))

    def fall(self):
        for item in self.diamonds_list:
            item.fall()

    def draw(self):
        for item in self.diamonds_list:
            item.show()

    def check_collision(self, player):
        collision = 0
        for item in self.diamonds_list:
            if ((item.x >= player.x and item.y <= player.y) and
                     (item.x > player.x + player.width and item.y < player.y + player.height)):
                collision = 1
                self.diamonds_list.remove(item)
            elif item.y > screen_height:
                collision = -1
                self.diamonds_list.remove(item)

        return collision
class Game:
    run: bool = True
    background = None
    fps = 120
    clock = pygame.time.Clock()
    player = None
    player_move = ''
    diamonds = None
    diamond_event = pygame.USEREVENT + 1
    catch: int = 0
    lost: int = 0

    def __init__(self):
        pygame.display.set_caption('Wizard')
        self.background_add(IMAGES_PATH + 'background.png')
        self.player = Wizard()
        self.diamonds = Diamonds()
        self.diamonds_add()

    def status(self):
        check = self.diamonds.check_collision(self.player)
        if check == 1:
            self.catch += 1
        if check == -1:
            self.lost += 1

        font = pygame.font.SysFont('Arial', 30)
        message = "Score: " + str(self.catch) + ' - ' + str(self.lost) + ' '
        text = font.render(message, True,(255, 255, 255), (47, 14, 51))
        screen.blit(text, (10, 10))

    def diamonds_add(self):
        pygame.time.set_timer(self.diamond_event, random.randint(1000, 2500))
        self.diamonds.add()
    def background_add(self, image):
       self.background = pygame.image.load(image)

    def background_draw(self, xy: tuple = (0, 0)):
        screen.blit(self.background, xy)

    def play(self,):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_move = 'left'
                    if event.key == pygame.K_RIGHT:
                        self.player_move = 'right'
                elif event.type == pygame.KEYUP:
                    self.player_move = ''
                elif event.type == self.diamond_event:
                    self.diamonds_add()

            if self.run:
                self.background_draw()
                self.player.show()
                self.player.move(self.player_move)
                self.diamonds.draw()
                self.diamonds.fall()
                self.status()

                pygame.display.update()
                self.clock.tick(self.fps)

        # === end while ===

        pygame.quit()


g = Game()
g.play()
