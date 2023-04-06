from pygame import sprite
from pygame.locals import *
import pygame
import sys


from Piece import Piece

pygame.init()
window = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()



if __name__ == '__main__':

    piece = Piece(Piece.generate_random_piece(), window)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    piece.rotate(clock_wise=False)
                if event.key == pygame.K_d:
                    piece.rotate(clock_wise=True)

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

