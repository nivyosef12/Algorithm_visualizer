import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)


class Grid:
    def __init__(self, rows, width):
        self.width = width  # width of the entire grid
        self.rows = rows  # num of rows
        self.grid = []
        self.node_width = width // rows
        for i in range(rows):
            self.grid.append([])
            for j in range(rows):
                node = Node(i, j, self.node_width, rows)
                self.grid[i].append(node)

    def draw(self, win):
        win.fill(WHITE)

        # draw nodes
        for row in self.grid:
            for node in row:
                node.draw(win)

        for i in range(self.rows):
            # horizontal lines
            pygame.draw.line(win, GRAY, (0, i * self.node_width), (self.width, i * self.node_width))
            for j in range(self.rows):
                # vertical lines
                pygame.draw.line(win, GRAY, (j * self.node_width, 0), (j * self.node_width, self.width))

        pygame.display.update()

    def get_clicked_pos(self, pos):
        y, x = pos
        row = x // self.node_width
        col = y // self.node_width

        return col, row

    def get_node(self, row, col):
        return self.grid[row][col]


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.total_row = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == BLUE

    # def reset

    def make_close(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = BLUE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self):
        pass

    def print_(self):
        print(self.width)
