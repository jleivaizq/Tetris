import pygame
from pygame import Rect

from board import Board
from shape import shape_colors


class Display:

    def __init__(self, board: Board):
        self.width = board.cell_size * board.cols
        self.height = board.cell_size * board.rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board = board

    def get_rect_cell(self, x: int, y: int, off_x: int, off_y: int) -> Rect:
        return pygame.Rect(
            (off_x + x) * self.board.cell_size,
            (off_y + y) * self.board.cell_size,
            self.board.cell_size,
            self.board.cell_size
        )

    def update(self):
        for y, row in enumerate(self.board.matrix):
            for x, val in enumerate(row):
                rect = self.get_rect_cell(x, y, 0, 0)
                pygame.draw.rect(self.screen, shape_colors[val], rect, 0, 10)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1, 10)
        pygame.display.update()


