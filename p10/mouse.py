import pygame
import pygame.display

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def main():
    is_draw = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_draw = True
                if event.button == 3:
                    screen.fill((0, 0, 0))
                    pygame.display.flip()
                if event.button == 2:
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, 20)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_draw = False

            if is_draw:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (225, 0, 50), pos, 20)
                pygame.display.update()

            clock.tick(30)

main()