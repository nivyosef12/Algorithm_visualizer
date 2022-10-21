# TODO list
# 1. generate maze

import pygame
from grid import Grid

WIDTH = 800
ROWS = 50
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("path finding algorithm")


def main():
    grid = Grid(ROWS, WIDTH)

    start_node = None
    end_node = None

    run = True
    started = False

    while run:
        grid.draw(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:  # when starting the algorithm cant change the grid
                continue

            if pygame.mouse.get_pressed()[0]:  # left click
                pos = pygame.mouse.get_pos()
                row, col = grid.get_clicked_pos(pos)
                node = grid.get_node(row, col)

                # define start node
                if not start_node:
                    start_node = node
                    start_node.make_start()

                # define end node
                elif not end_node and node != start_node:
                    end_node = node
                    end_node.make_end()

                # define barrier
                elif node != start_node and node != end_node:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # right click
                # feature for changing start and end position
                continue

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True
    pygame.quit()


main()