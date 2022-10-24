# TODO list
# 1.better h function

import pygame
from queue import PriorityQueue, Queue


class PathAlgorithm:
    def __init__(self, grid, draw, start, end):
        self.grid = grid
        self.draw_function = draw
        self.start = start
        self.end = end

    def reconstruct_path(self, came_from, curr):
        while curr in came_from:
            curr.make_path()
            curr = came_from[curr]
            self.draw_function()

        self.start.make_path()
        self.draw_function()

    def a_star(self, heuristic_function):
        # g_score -> distance from start node
        # h_score -> distance from end node
        # f_score -> g_score + h_score

        tie_breaker = 0  # in case of tie in scores take the one with lowest
        priority_queue = PriorityQueue()
        priority_queue.put((0, tie_breaker, self.start))  # (f_score, tie_breaker, curr_node)
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
                temp_g_score = g_score[curr_node] + 1
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

    def bfs(self):

        queue = Queue()
        queue.put(self.start)
        visited = set()
        came_from = dict()

        while not queue.empty():

            curr_node = queue.get()
            if curr_node != self.start:
                curr_node.make_open()
            visited.add(curr_node)
            insertions_to_queue = 0

            if curr_node == self.end:
                self.reconstruct_path(came_from, self.end)
                return True

            for neighbor in curr_node.get_neighbors():
                if neighbor not in visited:
                    insertions_to_queue += 1
                    queue.put(neighbor)
                    visited.add(neighbor)
                    came_from[neighbor] = curr_node

            if insertions_to_queue == 0:
                curr_node.make_close()

            self.draw_function()

        return False

    def dfs(self, curr_node, visited, came_from):
        self.draw_function()
        visited.add(curr_node)

        if curr_node != self.start:
            curr_node.make_open()

        if curr_node == self.end:
            self.reconstruct_path(came_from, self.end)
            return True

        for neighbor in curr_node.get_neighbors():
            if neighbor not in visited:
                came_from[neighbor] = curr_node
                if self.dfs(neighbor, visited, came_from):
                    return True

        curr_node.make_close()
        return False

    def dijkstra(self, start_node, weights):
        tie_breaker = 0  # in case of tie in scores take the one with lowest
        dist = {node: float("inf") for row in self.grid for node in row}
        dist[start_node] = 0
        came_from = {}
        priority_queue = PriorityQueue()
        priority_queue.put((0, tie_breaker, start_node))

        while not priority_queue.empty():

            curr_node = priority_queue.get()[2]

            if curr_node != self.start:
                curr_node.make_open()

            if curr_node == self.end:
                self.reconstruct_path(came_from, self.end)
                return True
            # TODO need to prove correctness -> if i_t_q == 0 then make_close()
            insertions_to_queue = 0
            for neighbor in curr_node.get_neighbors():

                if dist[neighbor] > dist[curr_node] + weights[neighbor]:  # weights[neighbor] = cost to move to neighbor
                    insertions_to_queue += 1
                    # neighbor.make_open()
                    dist[neighbor] = dist[curr_node] + weights[neighbor]  # TODO update()?!
                    tie_breaker += 1
                    priority_queue.put((dist[neighbor], tie_breaker, neighbor))

                    came_from[neighbor] = curr_node

            self.draw_function()

            if insertions_to_queue == 0:
                curr_node.make_close()

        return False
