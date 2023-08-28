import pygame, sys
from board import Board, NoShapeException, CollisionException
from display import Display

config = {
    'cell_size': 40,
    'cols': 10,
    'rows': 20,
    'delay': 200,
    'max_fps': 60,
}


class TetrisApp(object):

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(250, 25)
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        self.board = Board(config['cell_size'], config['cols'], config['rows'])
        self.display = Display(self.board)

    @staticmethod
    def quit():
        pygame.display.update()
        sys.exit()

    def run(self):
        pygame.time.set_timer(pygame.USEREVENT + 1, config['delay'])
        dont_burn_my_cpu = pygame.time.Clock()

        while 1:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.USEREVENT + 1:
                        self.board.update(inc_y=1)
                    elif event.type == pygame.QUIT:
                        self.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.board.update(inc_y=1, inc_x=-1)
                        elif event.key == pygame.K_RIGHT:
                            self.board.update(inc_y=1, inc_x=1)
                        elif event.key == pygame.K_SPACE:
                            self.board.update(inc_y=1, rotate=1)
            except NoShapeException:
                self.board.add_new_shape()
            except CollisionException:
                if self.board.is_full():
                    self.quit()
                else:
                    self.board.check_completed_lines()
                    self.board.add_new_shape()

            self.display.update()
            dont_burn_my_cpu.tick(config['max_fps'])


if __name__ == '__main__':
    App = TetrisApp()
    App.run()
