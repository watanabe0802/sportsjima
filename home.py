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

        self.button0 = tk.Button(self, text="価格計算", command=self.go_to_screen1,width=20, height=5)

        self.button2 = tk.Button(self, text="HTML生成", command=self.go_to_screen3,width=20, height=5)

        self.button3 = tk.Button(self, text="画像URL生成", command=self.go_to_screen4,width=20, height=5)

        self.button4 = tk.Button(self, text="せってい", command=self.go_to_setting,width=20, height=5)

        self.button0.pack(expand = True)
        self.button2.pack(expand = True)
        self.button3.pack(expand = True)
        self.button4.pack(expand = True)
        #self.button0.grid(row=0, column=0,  pady=20)
        #self.button2.grid(row=1, column=0,  pady=20)
        #self.button3.grid(row=2, column=0,  pady=20)
        
    def go_to_screen1(self):
        self.master.switch_frame("screen1.Screen1")

    def go_to_setting(self):
        self.master.switch_frame("setting.Setting")

    def go_to_screen3(self):
        self.master.switch_frame("screen3.Screen3")

    def go_to_screen4(self):
        self.master.switch_frame("screen4.Screen4")