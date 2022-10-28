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
        self.num_of_rows = rows  # num of rows
        self.grid = []
        self.node_width = width // rows
        for i in range(rows):
            self.grid.append([])
            for j in range(rows):
                node = Node(i, j, self.node_width)
                self.grid[i].append(node)

    def draw(self, win):
        win.fill(WHITE)

        # draw nodes
        for row in self.grid:
            for node in row:
                node.draw(win)

        for i in range(self.num_of_rows):
            # horizontal lines
            pygame.draw.line(win, GRAY, (0, i * self.node_width), (self.width, i * self.node_width))
            for j in range(self.num_of_rows):
                # vertical lines
                pygame.draw.line(win, GRAY, (j * self.node_width, 0), (j * self.node_width, self.width))

        pygame.display.update()

    def get_clicked_pos(self, pos):
        x, y = pos
        row = x // self.node_width
        col = y // self.node_width

        return row, col

    def get_node(self, row, col):
        return self.grid[row][col]

    def update_neighbors(self, row, col):
        neighbors = []
        if row < self.num_of_rows - 1 and not self.grid[row + 1][col].is_barrier():  # right
            neighbors.append(self.grid[row + 1][col])

        if row > 0 and not self.grid[row - 1][col].is_barrier():  # left
            neighbors.append(self.grid[row - 1][col])

        if col < self.num_of_rows - 1 and not self.grid[row][col + 1].is_barrier():  # up
            neighbors.append(self.grid[row][col + 1])

        if col > 0 and not self.grid[row][col - 1].is_barrier():  # down
            neighbors.append(self.grid[row][col - 1])

        self.grid[row][col].update_neighbors(neighbors)


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []

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

    def is_available(self):
        return self.color == WHITE

    def reset(self):
        self.color = WHITE

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

    def update_neighbors(self, neighbors):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors
