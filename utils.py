import tkinter as tk
from tkinter import ttk


class MessageBox(tk.Toplevel):
    def __init__(self, master, title, message):
        super().__init__(master)
        self.title(title)
        self.geometry("300x150+630+80")
        self.transient(master)
        self.grab_set()
        self.message_label = ttk.Label(self, text=message, wraplength=250, justify=tk.LEFT)
        self.message_label.pack(pady=20, padx=20)
        self.ok_button = ttk.Button(self, text="OK", command=self.destroy)
        self.ok_button.pack(pady=10)


def toggle_button_state(button, state):
    if state:
        button.config(state=tk.NORMAL)
    else:
        button.config(state=tk.DISABLED)