from core.model.sort_inter import SortInterface
from core.view.realtime_sort_view import RealtimeSortView


class QuickSort(SortInterface):
    def __init__(self):
        self.name = "Insertion Sort"
        self.complexity = "Ο(n^2), Best: Ο(n)"
        self.iter_num = 0

    def sort(self, list_to_sort: list, sort_view: RealtimeSortView, *args):
        if args:
            start = args[0]
            end = args[1]
        else:
            return []

        if start >= end:
            return

        partition_index = self.partition(list_to_sort, sort_view, start, end)

        self.sort(list_to_sort, sort_view, start, partition_index - 1)
        self.sort(list_to_sort, sort_view, partition_index + 1, end)

    def partition(self, list_to_sort, sort_view, start, end):
        pivot = list_to_sort[start]
        low = start + 1
        high = end

        while True:
            while low <= high and list_to_sort[high] >= pivot:
                self.iter_num += 1
                high = high - 1

            while low <= high and list_to_sort[low] <= pivot:
                self.iter_num += 1
                low = low + 1

            if low <= high:
                self.iter_num += 1
                self.update_view(sort_view, list_to_sort, low, high)
                self.swap_elements(list_to_sort, low, high)

            else:
                self.iter_num += 1
                break
        self.swap_elements(list_to_sort, start, high)
        self.update_view(sort_view, list_to_sort, start, high)

        return high

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
