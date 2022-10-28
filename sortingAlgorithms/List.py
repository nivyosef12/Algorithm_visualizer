# TODO
# 1. how to inherit/extend python list class
# 2. other names to has_swapped(), make_static()

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


class List:

    def __init__(self, num_list, width):
        self.lst = []
        self.bar_width = width // len(num_list)
        for i in range(len(num_list)):
            bar = Bar(num_list[i], self.bar_width, i)
            self.lst.append(bar)

    def draw(self, win):
        win.fill(WHITE)

        for bar in self.lst:
            bar.draw(win)

        pygame.display.update()

    def get_bar(self, index):
        if index < 0 or index >= len(self.lst):
            return None

        return self.lst[index]

class Bar:

    def __init__(self, height, width, i):
        self.height = height * 3  # height is the bar's value
        self.width = width
        self.x = i * width
        self.color = GREEN

    def make_choose(self):
        self.color = RED

    def make_move(self):
        self.color = BLUE

    def make_static(self):
        self.color = GREEN

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height

    def draw(self, win):
        # print(f"x: {self.x} , width: {self.width} , height: {self.height}")
        y_coordinate = 750  # TODO make generic

        # bar
        pygame.draw.rect(win, self.color, (self.x, y_coordinate - self.height, self.width, self.height))

        # frame
        pygame.draw.rect(win, BLACK, (self.x, y_coordinate - self.height, 1, self.height))
        pygame.draw.rect(win, BLACK, (self.x + self.width, y_coordinate - self.height, 1, self.height))
        pygame.draw.rect(win, BLACK, (self.x, y_coordinate - self.height, self.width, 1))

