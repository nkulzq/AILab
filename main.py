import tkinter as tk
from tkinter import ttk
from n_queen_prob import Board
from utils import MessageBox, toggle_button_state

import sv_ttk

root = tk.Tk()
root.title('n-queen problem')
root.geometry("750x500+630+80")
canvas = tk.Canvas(root)
board = Board(canvas)


def get_size():
    board.size = int(size_entry.get())
    board.reset()


def show_num_solutions():
    message = MessageBox(root, "number of solutions", "{} queen problem has {} solutions".format(board.size, board.num_solutions))
    root.wait_window(message)


def solve_step():
    board.solve_step()
    toggle_button_state(button_solutions, board.num_solutions)


def solve_continuous():
    board.solve_continuous()
    toggle_button_state(button_solutions, board.num_solutions)


button_step = ttk.Button(root, text="step", command=solve_step)
button_continuous = ttk.Button(root, text="continuous", command=solve_continuous)
size_entry = ttk.Entry(root)
button_submit = ttk.Button(root, text="submit", command=get_size)
button_solutions = ttk.Button(root, text="solutions", command=show_num_solutions, state=tk.NORMAL if board.finish else tk.DISABLED)
canvas.place(x=50, y=50)
button_step.place(x=550, y=25, width=100, height=30)
button_continuous.place(x=550, y=125, width=100, height=30)
size_entry.place(x=550, y=225, width=100, height=30)
button_submit.place(x=550, y=325, width=100, height=30)
button_solutions.place(x=550, y=425, width=100, height=30)
sv_ttk.set_theme("dark")
root.mainloop()
