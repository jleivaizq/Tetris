from random import randrange as rand

shape_colors = {
    0: (0, 0, 0),
    1: (255, 0, 0),
    2: (0, 150, 0),
    3: (0, 0, 255),
    4: (255, 120, 0),
    5: (255, 255, 0),
    6: (180, 0, 255),
    7: (0, 220, 220)
}

tetris_shapes = [
    {
        'layout': [[1, 1, 1],
                   [0, 1, 0]],
    },

    {
        'layout': [[0, 2, 2],
                   [2, 2, 0]],
    },

    {
        'layout': [[3, 3, 0],
                   [0, 3, 3]],
    },

    {
        'layout': [[4, 0, 0],
                   [4, 4, 4]],
    },

    {
        'layout': [[0, 0, 5],
                   [5, 5, 5]],
    },

    {
        'layout': [[6, 6, 6, 6]],
    },

    {
        'layout': [[7, 7],
                   [7, 7]],
    }
]


class Shape:

    def __init__(self, pos_x: int = None, pos_y: int = None):
        shape = tetris_shapes[rand(len(tetris_shapes))]
        self.layout = shape['layout']
        self.pos_x: int = pos_x - int(self.get_length() / 2)
        self.pos_y: int = pos_y

    def get_left(self):
        return self.pos_x

    def get_right(self):
        return self.pos_x + self.get_length()

    def get_bottom_pos(self):
        return self.get_height() + self.pos_y

    def get_length(self):
        return len(self.layout[0])

    def get_height(self):
        return len(self.layout)

    def is_boundary(self, off_x, off_y):
        return off_y == self.get_height() - 1

    def get_bottom_boundary(self):
        result = []
        for y, row in enumerate(self.layout):
            for x, val in enumerate(row):
                if val and (y == (self.get_height() - 1) or self.layout[y+1][x] == 0):
                    result.append((x,y))
        return result

    def rotate(self):
        self.layout = [[self.layout[-1 * (x+1)][y] for x in range(self.get_height())] for y in range(self.get_length())]



