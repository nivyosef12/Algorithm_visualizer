# TODO list
# 1. generate maze
# 2. restart button
# 3. another algorithms
from time import sleep

import pygame
from grid import Grid
from pathAlgorithms import PathAlgorithm

WIDTH = 800
ROWS = 50
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("path finding algorithm")


def h(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return dx + dy


def reset_grid(grid, start, end):
    for row in grid:
        for node in row:
            if node.is_barrier():
                # do nothing
                pass
            else:
                node.reset()

    start.make_start()
    end.make_end()


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

            elif pygame.mouse.get_pressed()[2]:  # right click
                # feature for changing start and end position
                continue

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True
                    for row in grid.grid:
                        for node in row:
                            grid.update_neighbors(node.row, node.col)

                    algorithm = PathAlgorithm(grid.grid, lambda: grid.draw(WIN), start_node, end_node)

                    # a star
                    algorithm.a_star(h)

                    # bfs
                    sleep(3)
                    reset_grid(grid.grid, start_node, end_node)
                    algorithm.bfs()

                    # dfs
                    sleep(3)
                    reset_grid(grid.grid, start_node, end_node)
                    algorithm.dfs(start_node, set(), {})

    pygame.quit()


main()
