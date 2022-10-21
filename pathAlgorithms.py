import pygame
from queue import PriorityQueue


class PathAlgorithm:
    def __init__(self, grid, draw, start, end):
        self.grid = grid
        self.draw_function = draw
        self.start = start
        self.end = end

    def reconstruct_path(self, came_from, curr):
        while curr in came_from:
            curr = came_from[curr]
            curr.make_path()
            self.draw_function()

    def a_star(self, heuristic_function):
        # g_score -> distance from start node
        # h_score -> distance from end node
        # f_score -> g_score + h_score

        tie_breaker = 0  # in case of tie in scores take the one with lowest
        priority_queue = PriorityQueue()
        priority_queue.put((0, tie_breaker, self.start))  # (g_score, tie_breaker, curr_node)
        nodes_set = {self.start}  # keep track of nodes in the priority queue
        came_from = {}
        g_score = {node: float("inf") for row in self.grid for node in row}
        g_score[self.start] = 0
        f_score = {node: float("inf") for row in self.grid for node in row}
        # in case of circling around to start node -> everything is less then infinity
        f_score[self.start] = heuristic_function(self.start.get_pos(), self.end.get_pos())

        while not priority_queue.empty():
            # allowing way out since the algorithm takes over
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # get curr node
            curr_node = priority_queue.get()[2]
            # curr node wont be considered again
            nodes_set.remove(curr_node)

            if curr_node == self.end:
                self.reconstruct_path(came_from, self.end)
                return True

            for neighbor in curr_node.get_neighbors():
                temp_g_score = g_score[curr_node]
                # updating
                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = curr_node
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + heuristic_function(neighbor.get_pos(), self.end.get_pos())
                    # if neighbor has not been considered
                    if neighbor not in nodes_set:
                        tie_breaker += 1
                        priority_queue.put((f_score[neighbor], tie_breaker, neighbor))
                        nodes_set.add(neighbor)
                        neighbor.make_open()

            self.draw_function()

            if curr_node != self.start:
                curr_node.make_close()

        return False
