# TODO
# 1. display performance -> num of comparisons, num of array accesses, runtime?

import pygame
import random
from List import List
from sortingAlgorithms import SortingAlgorithms

WIDTH = 800
ROWS = 50
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("sorting algorithm")


def main():
    num_list = [random.randint(1, 60) for i in range(50)]
    # num_list = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1]
    # num_list = [1, 11, 21, 31, 41, 51, 61]
    lst = List(num_list, WIDTH)

    run = True
    started = False

    while run:
        lst.draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True

                    algorithm = SortingAlgorithms(lst.lst, lambda: lst.draw(WIN))

                    # algorithm.insertion_sort()

                    # algorithm.swapping_sort()

                    algorithm.bubbleSort()

    return 0


main()
