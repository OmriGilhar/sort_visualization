from core.model.sort_inter import SortInterface
from core.view.realtime_sort_view import RealtimeSortView


class BubbleSort(SortInterface):
    def __init__(self):
        self.name = "Bubble Sort"
        self.complexity = "Ο(n^2), Best: Ο(n)"
        self.iter_num = 0
        self.index = 0

    def sort(self, list_to_sort: list, sort_view: RealtimeSortView):
        while not self.check_if_sorted(list_to_sort):
            self.iter_num += 1

            if list_to_sort[self.index] > list_to_sort[self.index + 1]:
                self.swap_elements(list_to_sort, self.index, self.index + 1)
            self.update_view(sort_view, list_to_sort, self.index)

            self.index += 1
            if self.index == len(list_to_sort) - 1:
                self.index = 0

    @staticmethod
    def check_if_sorted(list_to_sort: list) -> bool:
        for i in range(len(list_to_sort)-1, 0, -1):
            if list_to_sort[i] < list_to_sort[i-1]:
                return False
        return True

    @staticmethod
    def swap_elements(list_to_sort: list, pos1: int, pos2: int) -> list:
        list_to_sort[pos1], list_to_sort[pos2] = \
            list_to_sort[pos2], list_to_sort[pos1]
        return list_to_sort

    def update_view(self, sort_view: RealtimeSortView,
                    list_to_sort: list, current_index: int):
        x_axis = list(range(1, len(list_to_sort) + 1))
        sort_view.update_new_graph(x_axis, list_to_sort, current_index,
                                   current_index+1, self.name,
                                   self.complexity, self.iter_num)
