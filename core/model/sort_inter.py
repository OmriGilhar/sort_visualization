from core.view.realtime_sort_view import RealtimeSortView


class SortInterface:
    def sort(self, list_to_sort: list, sort_view: RealtimeSortView):
        pass

    def update_view(self, sort_view: RealtimeSortView,
                    list_to_sort: list, current_index: int, check_index=None):
        pass

    @staticmethod
    def swap_elements(list_to_sort: list, pos1: int, pos2: int) -> list:
        pass
