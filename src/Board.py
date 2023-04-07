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
        self.pixels_h = 0
        self.current_piece = Piece(Piece.generate_random_piece(), window, self.speed)
        self.sprites_group = pygame.sprite.GroupSingle()
        self.sprites_group.add(self.current_piece)

    def update(self):
        dt = self.clock.tick(30) / 1000
        self.sprites_group.draw(self.window)
        print(self.vertical_speed)

        for p in self.sprites_group:
            p.move(self.speed * self.horizontal_speed)
            p.fall(self.vertical_speed)

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