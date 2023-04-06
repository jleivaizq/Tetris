import random

import pygame
from pygame import sprite, Surface


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

    @staticmethod
    def generate_random_piece() -> str:
        return random.choice(list(Piece.sprite_loc.keys()))

    def __init__(self, piece_type: str, window: Surface):
        sprite.Sprite.__init__(self)
        self.window = window
        self.spriteSheet = pygame.image.load('sprites/sheet.png').convert_alpha()
        self.image = self.spriteSheet.subsurface(Piece.sprite_loc[piece_type])
        self.rect = self.image.get_rect()
        self.rect.midtop = (window.get_width() / 2, 0)

        self.speed = 10

    def update(self, dt, w):
        pass

    def move(self, x=0, y=0):

        if self.rect.right + x > self.window.get_width():
            self.rect.right = self.window.get_width()
        elif self.rect.left + x < 0:
            self.rect.left = 0
        else:
            self.rect.centerx += x

        if self.rect.bottom + y > self.window.get_height():
            self.rect.bottom = self.window.get_height()
        elif self.rect.top + y < 0:
            self.rect.top = 0
        else:
            self.rect.centery += y

    def fall(self, g=1):
        self.move(0, self.speed * g)