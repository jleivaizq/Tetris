from pygame import sprite
from pygame.locals import *
import pygame
import sys
import random

pygame.init()
window = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


class Piece(sprite.Sprite):
    sprite_loc = {
        'square': (18, 18, 76, 76),
        's1': (180, 18, 114, 76),
        's2': (569, 0, 77, 112),
        't': (0, 227, 112, 77),
        'l1': (0, 411, 112, 77),
        'l2': (0, 621, 112, 76),
        'line': (36, 793, 39, 150),
    }

    def __init__(self, piece_type):
        sprite.Sprite.__init__(self)
        self.spriteSheet = pygame.image.load('sprites/sheet.png').convert_alpha()
        self.image = self.spriteSheet.subsurface(Piece.sprite_loc[piece_type])
        self.rect = self.image.get_rect()
        self.rect.midtop = (window.get_width() / 2, 0)

        self.speed = 10

    def update(self, dt, w):
        pass

    def move(self, x=0, y=0):
        if self.rect.centerx + x >= window.get_width() or self.rect.centerx + x < 0:
            return
        if self.rect.bottom + y >= window.get_height() or self.rect.top + y < 0:
            return
        self.rect.center = (self.rect.centerx + x, self.rect.centery + y)

    def fall(self, g=1):
        self.move(0, self.speed * g)


if __name__ == '__main__':

    piece = Piece(random.choice(list(Piece.sprite_loc.keys())))
    sprites_group = pygame.sprite.GroupSingle()
    speed = piece.speed
    sprites_group.add(piece)
    gravity = 1
    elasticity = 1

    while True:

        dt = clock.tick(30) / 1000
        pixels_h = 0
        sprites_group.draw(window)

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            elasticity *= 1.2
            pixels_h = -speed
        if keys[K_RIGHT]:
            elasticity *= 1.2
            pixels_h = speed
        if keys[K_DOWN]:
            gravity *= 2
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    gravity = 1
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    elasticity = 1

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for p in sprites_group:
            p.move(pixels_h * elasticity)
            p.fall(gravity)

        window.fill((0, 0, 0))
        sprites_group.update(dt, window)
        sprites_group.draw(window)
        pygame.display.update()

