import pygame
from pygame import Rect

from board import Board

# Assigns a color to each shape
shape_colors: dict[int, tuple[int, int, int]] = {
    0: (0, 0, 0),
    1: (255, 0, 0),
    2: (0, 150, 0),
    3: (0, 0, 255),
    4: (255, 120, 0),
    5: (255, 255, 0),
    6: (180, 0, 255),
    7: (0, 220, 220)
}


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
