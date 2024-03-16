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
pygame.display.set_caption('Shake Game by belgorod')

clock = pygame.time.Clock()


def gameLoop()
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.k_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass

gameLoop()