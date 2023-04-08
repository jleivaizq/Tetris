import random

import pygame
from pygame import sprite, Surface


class Piece(sprite.Sprite):

    sprite_loc = {
        'square': [(18, 18, 76, 76)],
        's1': [(180, 18, 114, 76), (384, 0, 76, 112)],
        's2': [(569, 0, 77, 112), (735, 18, 113, 76)],
        't': [(0, 227, 112, 77), (193, 208, 76, 114), (379, 227, 114, 77), (558, 208, 77, 114)],
        'l1': [(0, 411, 112, 77), (202, 392, 77, 114), (385, 411, 114, 77), (562, 392, 76, 114)],
        'l2': [(0, 621, 112, 76), (199, 602, 77, 113), (382, 621, 114, 76), (577, 602, 77, 113)],
        'line': [(36, 793, 39, 150), (193, 849, 151, 39)],
    }

    @staticmethod
    def generate_random_piece() -> str:
        return random.choice(list(Piece.sprite_loc.keys()))

    def __init__(self, piece_type: str, window: Surface, speed: int):
        sprite.Sprite.__init__(self)
        self.window = window
        self.piece_type = piece_type
        self.current_pos = 0
        self.speed = speed
        self.spriteSheet = pygame.image.load('sprites/sheet.png').convert_alpha()
        self.image = self.spriteSheet.subsurface(Piece.sprite_loc[self.piece_type][self.current_pos])
        self.rect = self.image.get_rect()
        self.rect.midtop = (window.get_width() / 2, 0)
        sprite.mask = pygame.mask.from_surface(self.image)

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

    def rotate(self, clock_wise: bool = True):
        list_pos: list = Piece.sprite_loc[self.piece_type]
        self.current_pos = (self.current_pos + 1 if clock_wise else self.current_pos - 1) % len(list_pos)
        self.image = self.spriteSheet.subsurface(list_pos[self.current_pos])
