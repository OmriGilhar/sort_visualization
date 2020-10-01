import tkinter as tk
import matplotlib

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")


class RealtimeSortView:
    def __init__(self, root):
        # Main frame
        self.pad = int(root.winfo_screenheight() / 30)
        self.main_frame = tk.Frame(root, width=root.winfo_screenwidth(),
                                   height=root.winfo_screenheight(),
                                   bg="black", relief=tk.SUNKEN, padx=25,
                                   pady=25)

        self.f = None
        self.ax = None
        self.bar_plot = None
        self.canvas = None
        self.width = 0
        self.main_frame.pack()

    def destroy_view(self):
        self.main_frame.destroy()

    def update_new_graph(self, x_axis: list, list_to_sort: list,
                         current_index: int):
        if not self.f and not self.ax:
            self.f = Figure(figsize=(17, 12), dpi=100)
            self.ax = self.f.add_subplot(111)
            self.width = .025
            self.bar_plot = self.ax.bar(x_axis, list_to_sort, self.width,
                                        color='royalblue', align='edge')
            self.bar_plot[current_index].set_color('r')
            self.bar_plot[current_index+1].set_color('r')
            self.canvas = FigureCanvasTkAgg(self.f, master=self.main_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,
                                             expand=1)
        else:
            self.bar_plot.remove()
            self.bar_plot = self.ax.bar(x_axis, list_to_sort, self.width,
                                        color='royalblue')
            self.bar_plot[current_index].set_color('r')
            self.bar_plot[current_index + 1].set_color('r')
            self.canvas.draw()
