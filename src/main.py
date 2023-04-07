from pygame.locals import *
import pygame
import sys

from Board import Board

pygame.init()
window = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


if __name__ == '__main__':

    board = Board(window, clock)
    speed = board.speed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    board.set_vertical_speed(1)
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    board.set_horizontal_speed(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.set_horizontal_speed(-1)
                if event.key == pygame.K_RIGHT:
                    board.set_horizontal_speed(1)
                if event.key == pygame.K_a:
                    board.rotate_current_piece(clock_wise=False)
                if event.key == pygame.K_d:
                    board.rotate_current_piece(clock_wise=True)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            board.update_horizontal_speed(1.2)
        if keys[K_RIGHT]:
            board.update_horizontal_speed(1.2)
        if keys[K_DOWN]:
            board.update_vertical_speed(1.2)
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        board.update()
        pygame.display.update()


