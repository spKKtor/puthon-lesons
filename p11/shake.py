import pygame
import random
import time
import sys

pygame.init()
#COLORS
white =  (255 ,255, 255)
yellow = (225, 225, 100)
black = (0, 0, 0)
green = (0, 225, 0)
red = (213, 50, 80)
blue = (43, 52, 65)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Shake Game by green')

clock = pygame.time.Clock()


def our_shake():
    pygame.draw.rect(dis, black, [10, 10, 50, 50])


def gameLoop():
    game_over = False
    shake_list = []
    length_of_shake = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.k_RIGHT:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass

        our_shake()

        pygame.display.flip()
        clock.tick(60)


    pygame.quit()
    sys.exit()

gameLoop()