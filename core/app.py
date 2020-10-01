from core.controller.sort_controller import SortController

from core.utils.list_prepration import create_list
from core.model.bubble_sort import BubbleSort


def main():
    controller = SortController()
    controller.run()

    # orig_randomized_list = create_list(15, 0, 100)
    # bubble_sort_list = orig_randomized_list.copy()
    # b_sort = BubbleSort()
    # b_sort.sort(bubble_sort_list)

    # print("Random List: {0}".format(orig_randomized_list))
    # print("---------------------------------")
    # print("Sorted_list: {0}, iterations: {1}".format(sorted_list,
    #                                                  b_sort.iter_num))

if __name__ == '__main__':
    main()

