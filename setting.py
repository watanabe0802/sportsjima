import tkinter as tk
import tkinter
from tkinter.scrolledtext import ScrolledText

class Setting(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_screen()

    def init_screen(self):
        self.master.title("設定")
        self.pack(fill=tk.BOTH, expand=1)

        button = tk.Button(self, text="戻る", command=self.go_to_screen1)
        button.pack()

    def go_to_screen1(self):
        self.master.switch_frame("screen1.Screen1")