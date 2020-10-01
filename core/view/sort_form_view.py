import tkinter as tk

from core.utils.sort_types import SortEnum


class SortForm:
    def __init__(self, root, controller, sort_type: SortEnum):
        # Main frame
        self.pad = int(root.winfo_screenheight() / 6)
        self.main_frame = tk.Frame(root, width=root.winfo_screenwidth(),
                                   height=root.winfo_screenheight(),
                                   bg="black", relief=tk.SUNKEN, padx=25,
                                   pady=25)
        self.controller = controller
        self.main_frame.pack()

        self.num_of_elements_text = tk.StringVar()
        self.start_text = tk.StringVar()
        self.end_text = tk.StringVar()

        self.num_of_elements_label = tk.Label(
            self.main_frame,
            text="Number Of Elements:",
            font=("Helvetica", 16)
        )

        self.start_label = tk.Label(
            self.main_frame,
            text="Starting Element Number:",
            font=("Helvetica", 16)
        )

        self.end_label = tk.Label(
            self.main_frame,
            text="Ending Element Number:",
            font=("Helvetica", 16)
        )

        self.num_of_elements_entry = tk.Entry(
            self.main_frame,
            text=self.num_of_elements_text,
            font=("Helvetica", 16)
        )

        self.start_entry = tk.Entry(
            self.main_frame,
            text=self.start_text,
            font=("Helvetica", 16)
        )

        self.end_entry = tk.Entry(
            self.main_frame,
            text=self.end_text,
            font=("Helvetica", 16)
        )

        self.submit_button = tk.Button(
            self.main_frame,
            text="Run",
            bg='gray25',
            fg='white',
            font=(
                "Helvetica",
                30
            ),

            command=lambda: self.controller.check_valid_form(
                SortEnum.BUBBLE,
                int(self.num_of_elements_text.get()),
                int(self.start_text.get()),
                int(self.end_text.get())
            )

        )

        # Grid:
        self.num_of_elements_label.grid(row=0, column=0, padx=5, pady=5)
        self.num_of_elements_entry.grid(row=0, column=1, padx=5, pady=5)

        self.start_label.grid(row=1, column=0, padx=5, pady=5)
        self.start_entry.grid(row=1, column=1, padx=5, pady=5)

        self.end_label.grid(row=2, column=0, padx=5, pady=5)
        self.end_entry.grid(row=2, column=1, padx=5, pady=5)

        self.submit_button.grid(row=3, column=0, padx=5, pady=5)

    def destroy_view(self):
        self.main_frame.destroy()
