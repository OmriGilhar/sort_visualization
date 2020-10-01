import tkinter as tk

from core.model.bubble_sort import BubbleSort
from core.model.insertion_sort import InsertionSort
from core.model.selection_sort import SelectionSort
from core.utils.list_prepration import create_list
from core.view.realtime_sort_view import RealtimeSortView
from core.view.sort_choose_view import SortChooseView
from core.utils.sort_types import SortEnum
from core.view.sort_form_view import SortForm


class SortController:
    def __init__(self):
        # Master GUI process
        self.root = tk.Tk()

        # Root setting
        self.board_pad = 200
        self.current_view = None
        self.full_screen_state = True
        self.add_binds()

    def run(self):
        self.root.title("Sort Visualization")
        self.root.geometry("{0}x{1}".format(self.root.winfo_screenwidth() -
                                            self.board_pad,
                                            self.root.winfo_screenheight() -
                                            self.board_pad))
        self.root.configure(bg='black')
        self.root.deiconify()
        self.root.attributes("-fullscreen", self.full_screen_state)

        self.current_view = SortChooseView(self.root, self)

        self.root.mainloop()

    # Configurations
    def add_binds(self):
        # Full screen
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        """
        Make the app full screen with "F11" button
        """
        self.full_screen_state = not self.full_screen_state
        self.root.attributes("-fullscreen", self.full_screen_state)

    def end_fullscreen(self, event=None):
        """
        Exits full screen mode by pressing "esc" button
        """
        self.full_screen_state = False
        self.root.attributes("-fullscreen", False)

    def show_sort_options(self):
        self.current_view.destroy_view()
        self.current_view = SortChooseView(self.root, self)

    def show_form(self, sort_type: SortEnum):
        self.current_view.destroy_view()
        self.current_view = SortForm(self.root, self, sort_type)

    def check_valid_form(self, sort_type: SortEnum, num_of_element: int,
                         start: int, stop: int):
        if num_of_element and start and stop:
            if num_of_element > 2 and start < stop:
                self.current_view.destroy_view()
                self.run_sort(sort_type, num_of_element, start, stop)

    def run_sort(self, sort_type: SortEnum, num_of_element: int,
                 start: int, stop: int):
        orig_randomized_list = create_list(num_of_element, start, stop)
        self.current_view = RealtimeSortView(self.root, self)

        if sort_type == SortEnum.BUBBLE:
            b_sort = BubbleSort()
            bubble_sort_list = orig_randomized_list.copy()
            b_sort.sort(bubble_sort_list, self.current_view)

        elif sort_type == SortEnum.SELECTION:
            selection_sort = SelectionSort()
            selection_sort_list = orig_randomized_list.copy()
            selection_sort.sort(selection_sort_list, self.current_view)

        elif sort_type == SortEnum.INSERTION:
            insertion_sort = InsertionSort()
            insertion_sort_list = orig_randomized_list.copy()
            insertion_sort.sort(insertion_sort_list, self.current_view)

        self.current_view.back_button.config(state="normal")
