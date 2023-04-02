from pygame.locals import *
import pygame
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Tetris")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_w]:
                    window.fill(pygame.Color("blue"))
                if keys[K_a]:
                    window.fill(pygame.Color("red"))
                if keys[K_d]:
                    window.fill(pygame.Color("green"))
                if keys[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()