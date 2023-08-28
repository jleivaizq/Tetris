from shape import Shape


class CollisionException(Exception):
    pass


class NoShapeException(Exception):
    pass


class Board:

    def __init__(self, cell_size: int, cols: int, rows: int):
        self.cell_size = cell_size
        self.cols = cols
        self.rows = rows
        # Last row of 1 at the bottom for conflict detection
        self.matrix = [[0 if y < self.rows else 1 for _ in range(self.cols)] for y in range(self.rows + 1)]
        self.shapes = []
        self.current_shape = None

    def start_position(self) -> (int, int):
        return int(self.cols / 2), 0

    def update_shape_in_board(self, shape: Shape, clean: bool = False):
        for off_y, row in enumerate(shape.layout):
            for off_x, val in enumerate(row):
                if val and 0 <= off_y + shape.pos_y < self.rows and 0 <= off_x + shape.pos_x < self.cols:
                    self.matrix[off_y + shape.pos_y][off_x + shape.pos_x] = val if not clean else 0

    def update(self, inc_y: int = 0, inc_x: int = 0, rotate: int = 0):
        if not self.current_shape:
            raise NoShapeException()

        if self.detect_collision(self.current_shape):
            raise CollisionException()

        self.update_shape_in_board(self.current_shape, True)
        self.current_shape.pos_y += inc_y
        if 0 <= self.current_shape.get_left() + inc_x and self.current_shape.get_right() + inc_x <= self.cols:
            self.current_shape.pos_x += inc_x
        if rotate:
            self.current_shape.rotate()
        self.update_shape_in_board(self.current_shape)

    def add_new_shape(self):
        self.current_shape = Shape(*self.start_position())
        self.update_shape_in_board(self.current_shape)
        self.shapes.append(self.current_shape)

    def detect_collision(self, shape: Shape) -> bool:
        boundary = shape.get_bottom_boundary()
        for (off_x, off_y) in boundary:
            if (shape.pos_y + off_y == self.rows) or (self.matrix[shape.pos_y + off_y + 1][shape.pos_x + off_x] != 0):
                return True
        return False

    def is_full(self) -> bool:
        for val in self.matrix[0]:
            if val != 0:
                return True
        return False

    def remove_line(self, y: int):
        for off_y in range(y, 1, -1):
            for off_x in range(0, self.cols):
                self.matrix[off_y][off_x] = self.matrix[off_y - 1][off_x]

    def check_completed_lines(self):
        for off_y, row in enumerate(self.matrix):
            if off_y < self.rows and all(cell != 0 for cell in row):
                self.remove_line(off_y)
