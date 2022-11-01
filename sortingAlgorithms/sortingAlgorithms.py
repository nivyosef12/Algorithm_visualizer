import pygame
import time


class SortingAlgorithms:

    def __init__(self, lst, draw):
        self.lst = lst  # list of Bar objects
        self.draw_function = draw

    # start - inclusive
    # end - exclusive
    # TODO edge cases?
    def __find_min(self, start, end):
        curr_min = self.lst[start].get_height()
        index = start
        for i in range(start + 1, end):
            if self.lst[i].get_height() < curr_min:
                curr_min = self.lst[i].get_height()
                index = i

        return curr_min, index

    def __swap(self, i, j):
        tmp = self.lst[i].get_height()
        self.lst[i].set_height(self.lst[j].get_height())
        self.lst[j].set_height(tmp)

    def swapping_sort(self):
        lst_len = len(self.lst)
        for i in range(0, lst_len):
            min_num, min_index = self.__find_min(i, lst_len)
            curr_bar = self.lst[i]
            min_bar = self.lst[min_index]

            # painting
            curr_bar.make_choose()
            min_bar.make_choose()

            # draw
            self.draw_function()
            time.sleep(0.05)

            # swap
            self.__swap(i, min_index)

            # draw
            self.draw_function()

            # painting
            curr_bar.make_static()
            min_bar.make_static()

        self.draw_function()

    def bubbleSort(self):
        lst_len = len(self.lst)

        for i in range(lst_len):

            # Last i elements are already in place
            for j in range(0, lst_len - i - 1):

                # allowing way out since the algorithm takes over
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                curr_bar = self.lst[j]
                curr_bar.make_choose()
                next_bar = self.lst[j + 1]
                next_bar.make_choose()

                # draw
                self.draw_function()
                time.sleep(0.05)

                # Swap if the element found is greater than the next element
                if curr_bar.get_height() > next_bar.get_height():
                    self.__swap(j, j + 1)

                    # draw
                    self.draw_function()
                    time.sleep(0.05)

                # draw
                curr_bar.make_static()
                next_bar.make_static()
                self.draw_function()
                time.sleep(0.05)

    def insertion_sort(self):
        for i in range(1, len(self.lst)):
            bar = self.lst[i]
            bar.make_choose()
            self.draw_function()
            key = bar.get_height()

            j = i - 1
            while j >= 0 and key < self.lst[j].get_height():

                # allowing way out since the algorithm takes over
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                time.sleep(0.1)
                self.lst[j + 1].make_move()
                self.draw_function()

                time.sleep(0.05)
                self.lst[j + 1].set_height(self.lst[j].get_height())
                self.draw_function()

                time.sleep(0.05)
                self.lst[j + 1].make_static()
                self.draw_function()

                j -= 1

            self.lst[j + 1].set_height(key)
            bar.make_static()

        self.draw_function()

    # __partition places the pivot a its correct position in sorted list
    def __partition(self, low, high):
        pivot = self.lst[high - 1]  # TODO choose "good" pivot
        pivot.make_move()
        i = low - 1

        for j in range(low, high):

            if self.lst[j].get_height() < pivot.get_height():
                i += 1
                bar_i = self.lst[i]
                bar_j = self.lst[j]

                # mark chosen bars and draw
                bar_i.make_choose()
                bar_j.make_choose()
                self.draw_function()
                time.sleep(0.05)

                # swap
                self.__swap(i, j)

                # draw after swap
                self.draw_function()
                time.sleep(0.05)
                bar_i.make_static()
                bar_j.make_static()
                self.draw_function()

        self.__swap(i + 1, high - 1)
        pivot.make_static()
        self.draw_function()

        return i + 1

    def __quick_sort(self, low, high):
        if low < high:
            partition_index = self.__partition(low, high)
            self.__quick_sort(low, partition_index)
            self.__quick_sort(partition_index + 1, high)

    def quick_sort(self):
        print("start")
        self.draw_function()
        self.__quick_sort(0, len(self.lst))
        self.draw_function()
        print("end")