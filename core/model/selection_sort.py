from core.model.sort_inter import SortInterface
from core.view.realtime_sort_view import RealtimeSortView


class SelectionSort(SortInterface):
    def __init__(self):
        self.name = "Selection Sort"
        self.complexity = "Worst: Ο(n^2), Best: Ο(n^2)"
        self.iter_num = 0
        self.min_j = None
        self.index = 0

    def sort(self, list_to_sort: list, sort_view: RealtimeSortView):
        for i in range(len(list_to_sort)):
            self.min_j = i
            for j in range(i+1, len(list_to_sort)):
                self.iter_num += 1
                self.update_view(sort_view, list_to_sort, i, j)
                if list_to_sort[j] < list_to_sort[self.min_j]:
                    self.min_j = j
            if self.min_j != i:
                self.swap_elements(list_to_sort, i, self.min_j)
                self.update_view(sort_view, list_to_sort, i, self.min_j)

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
                    list_to_sort: list, current_index: int, check_index=None):
        x_axis = list(range(1, len(list_to_sort) + 1))
        sort_view.update_new_graph(x_axis, list_to_sort, current_index,
                                   check_index, self.name, self.complexity,
                                   self.iter_num)
