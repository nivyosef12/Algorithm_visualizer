import pygame
import time


class SortingAlgorithms:

    def __init__(self, lst, draw):
        self.lst = lst
        self.draw_function = draw

    # start - inclusive
    # end - exclusive
    # TODO edge cases?
    def find_min(self, start, end):
        curr_min = self.lst[start].get_height()
        index = start
        for i in range(start + 1, end):
            if self.lst[i].get_height() < curr_min:
                curr_min = self.lst[i].get_height()
                index = i

        return curr_min, index

    def swapping_sort(self):
        lst_len = len(self.lst)
        for i in range(0, lst_len):
            min_num, min_index = self.find_min(i, lst_len)
            curr_bar = self.lst[i]
            min_bar = self.lst[min_index]

            # painting
            curr_bar.make_choose()
            min_bar.make_choose()

            # draw
            self.draw_function()
            time.sleep(0.2)

            # swap
            min_bar.set_height(curr_bar.get_height())
            curr_bar.set_height(min_num)

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
                    tmp = curr_bar.get_height()
                    curr_bar.set_height(next_bar.get_height())
                    next_bar.set_height(tmp)

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
