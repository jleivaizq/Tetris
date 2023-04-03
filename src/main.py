from pygame import sprite
from pygame.locals import *
import pygame
import sys

pygame.init()
window = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Tetris")


class Piece(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.spriteSheet = pygame.image.load("sprites/sheet.png").convert_alpha()
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((0, 0, 100, 100)), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midtop = (window.get_width() / 2, 0)

    def update(self):
        pass


if __name__ == '__main__':

    piece = Piece()
    sprites_group = pygame.sprite.GroupSingle()
    sprites_group.add(piece)

    while True:

        sprites_group.draw(window)

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
