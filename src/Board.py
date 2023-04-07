import pygame
from pygame import Surface

from Piece import Piece


class Board:
    def __init__(self, window: Surface, clock: pygame.time.Clock):
        self.clock = clock
        self.window = window
        self.speed = 10
        self.vertical_speed = 1
        self.horizontal_speed = 0
        self.current_piece = None
        self.sprites_group = pygame.sprite.Group()

    def generate_new_piece(self):
        self.current_piece = Piece(Piece.generate_random_piece(), self.window, self.speed)
        self.sprites_group.add(self.current_piece)

    def update(self):
        if self.current_piece is None or self.current_piece.rect.bottom == self.window.get_rect().bottom:
            self.generate_new_piece()

        dt = self.clock.tick(30) / 1000
        self.sprites_group.draw(self.window)

        self.current_piece.move(self.speed * self.horizontal_speed)
        self.current_piece.fall(self.vertical_speed)

        self.window.fill((0, 0, 0))
        self.sprites_group.update(dt, self.window)
        self.sprites_group.draw(self.window)

    def set_horizontal_speed(self, s: float):
        self.horizontal_speed = s

    def update_horizontal_speed(self, s: float):
        self.horizontal_speed *= s if self.horizontal_speed > 0 else s

    def set_vertical_speed(self, s: float):
        self.vertical_speed = s

    def update_vertical_speed(self, s: float):
        self.vertical_speed *= s if self.vertical_speed > 0 else s

    def rotate_current_piece(self, clock_wise: bool = True):
        self.current_piece.rotate(clock_wise)
