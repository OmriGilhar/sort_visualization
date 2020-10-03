import tkinter as tk

from core.utils.sort_types import SortEnum


class SortChooseView:
    def __init__(self, root, controller):
        # Main frame
        self.pad = int(root.winfo_screenheight() / 30)
        self.main_frame = tk.Frame(root, width=root.winfo_screenwidth(),
                                   height=root.winfo_screenheight(),
                                   bg="black", relief=tk.SUNKEN, padx=25,
                                   pady=25)
        self.controller = controller
        self.main_frame.pack()

        # Border frame
        self.border_frame = tk.Frame(
            self.main_frame,
            width=self.main_frame.winfo_screenwidth() - self.pad,
            height=self.main_frame.winfo_screenheight() - self.pad,
            bg="black", relief=tk.SUNKEN, padx=25, pady=25
        )

        self.bubble_sort_button = tk.Button(
            self.border_frame,
            text="Bubble Sort",
            bg='gray25',
            fg='white',
            font=(
                "Helvetica",
                30
            ),

            command=lambda: self.controller.show_form(SortEnum.BUBBLE)
        )

        self.selection_sort_button = tk.Button(
            self.border_frame,
            text="Selection Sort",
            bg='gray25',
            fg='white',
            font=(
                "Helvetica",
                30
            ),

            command=lambda: self.controller.show_form(SortEnum.SELECTION)
        )

        self.insertion_sort_button = tk.Button(
            self.border_frame,
            text="Insertion Sort",
            bg='gray25',
            fg='white',
            font=(
                "Helvetica",
                30
            ),

            command=lambda: self.controller.show_form(SortEnum.INSERTION)
        )

        self.quick_sort_button = tk.Button(
            self.border_frame,
            text="Quick Sort",
            bg='gray25',
            fg='white',
            font=(
                "Helvetica",
                30
            ),

            command=lambda: self.controller.show_form(SortEnum.QUICK)
        )

        self.border_frame.grid(row=0, column=0)
        self.bubble_sort_button.grid(row=0, column=0)
        self.selection_sort_button.grid(row=0, column=1)
        self.insertion_sort_button.grid(row=0, column=2)
        self.quick_sort_button.grid(row=1, column=0)
        self.border_frame.update()

    def destroy_view(self):
        self.main_frame.destroy()
