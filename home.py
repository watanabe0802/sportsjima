import tkinter as tk
import tkinter
from tkinter.scrolledtext import ScrolledText

class Home(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_screen()

    def init_screen(self):
        self.master.title("ホーム")
        self.pack(fill=tk.BOTH, expand=1)

        self.button0 = tk.Button(self, text="価格計算", command=self.go_to_screen1)

        self.button2 = tk.Button(self, text="標準商品登録", command=self.go_to_screen3)

        self.button3 = tk.Button(self, text="せってい", command=self.go_to_setting)


        self.button0.grid(row = 0, column = 2, columnspan = 3)
        self.button2.grid(row = 1, column = 2, columnspan = 3)
        self.button3.grid(row = 2, column = 2, columnspan = 3)
        
    def go_to_screen1(self):
        self.master.switch_frame("screen1.Screen1")

    def go_to_setting(self):
        self.master.switch_frame("setting.Setting")

    def go_to_screen3(self):
        self.master.switch_frame("screen3.Screen3")