import pygame
from pygame import Surface

from Piece import Piece


def collide_bottom(sprite, other_sprite):
    return sprite.rect.bottom >= other_sprite.rect.top and \
        sprite.rect.bottom <= other_sprite.rect.bottom and \
        sprite.rect.centerx >= other_sprite.rect.left and \
        sprite.rect.centerx <= other_sprite.rect.right

class Board:

    def __init__(self, window: Surface, clock: pygame.time.Clock):
        self.clock = clock
        self.window = window
        self.speed = 10
        self.vertical_speed = 1
        self.horizontal_speed = 0
        self.current_piece = None
        self.current_group = pygame.sprite.GroupSingle()
        self.sprites_group = pygame.sprite.Group()

    def generate_new_piece(self) -> Piece:
        return Piece(Piece.generate_random_piece(), self.window, self.speed)

    def update(self):
        if self.current_piece is None:
            self.current_piece = self.generate_new_piece()
            self.current_group.add(self.current_piece)

        collisions = pygame.sprite.spritecollide(self.current_piece, self.sprites_group, False, collide_bottom)
        if self.current_piece.rect.bottom == self.window.get_rect().bottom or len(collisions) > 0:
            self.sprites_group.add(self.current_piece)
            self.current_group.remove(self.current_piece)
            self.current_piece = self.generate_new_piece()
            self.current_group.add(self.current_piece)

        dt = self.clock.tick(15) / 1000

        self.current_piece.move(self.speed * self.horizontal_speed)
        self.current_piece.fall(self.vertical_speed)

        self.window.fill((0, 0, 0))
        self.sprites_group.update(dt, self.window)
        self.sprites_group.draw(self.window)

        self.current_group.update(dt, self.window)
        self.current_group.draw(self.window)

        for sprite in self.current_group:
            colliderect = pygame.Surface(sprite.rect.size).convert_alpha()
            colliderect.fill((255, 255, 255, 50))
            self.window.blit(colliderect, sprite.rect)

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
