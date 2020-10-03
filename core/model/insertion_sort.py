from core.model.sort_inter import SortInterface
from core.view.realtime_sort_view import RealtimeSortView


class InsertionSort(SortInterface):
    def __init__(self):
        self.name = "Insertion Sort"
        self.complexity = "Worst: Ο(n^2), Best: Ο(n)"
        self.iter_num = 0

    def sort(self, list_to_sort: list, sort_view: RealtimeSortView):
        for i in range(1, len(list_to_sort)):
            key = list_to_sort[i]

            j = i - 1
            while j >= 0 and key < list_to_sort[j]:
                self.iter_num += 1
                list_to_sort[j + 1] = list_to_sort[j]
                self.update_view(sort_view, list_to_sort, i, j)
                j -= 1
            list_to_sort[j + 1] = key

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
