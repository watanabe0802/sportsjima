import tkinter as tk
import tkinter
from tkinter.scrolledtext import ScrolledText
import math

class Screen2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_screen()

    def init_screen(self):
        self.master.title("上下セット用")
        self.pack(fill=tk.BOTH, expand=1)

        self.button0 = tk.Button(self, text="戻る", command=self.go_to_screen1)


        self.radio_value = tk.IntVar()
        self.radio0 = tk.Radiobutton(self,
            text = "ヤマト",      # ラジオボタンの表示名
            variable = self.radio_value, # 選択の状態を設定する
            value = 0                    # ラジオボタンに割り付ける値の設定
        )
        self.radio1 = tk.Radiobutton(self,
            text = "ゆうパケット",      # ラジオボタンの表示名
            variable = self.radio_value, # 選択の状態を設定する
            value = 1                    # ラジオボタンに割り付ける値の設定
        )

        self.lbl3 = tkinter.Label(self,text='価格')
        self.txt3 = tkinter.Entry(self,width=20)
        self.txt3a = tkinter.Entry(self,width=20)

        self.radio_value1 = tk.IntVar()
        self.radio3 = tk.Radiobutton(self,
            text = "税込み",      # ラジオボタンの表示名
            variable = self.radio_value1, # 選択の状態を設定する
            value = 0                    # ラジオボタンに割り付ける値の設定
        )
        self.radio4 = tk.Radiobutton(self,
            text = "税抜き",      # ラジオボタンの表示名
            variable = self.radio_value1, # 選択の状態を設定する
            value = 1                    # ラジオボタンに割り付ける値の設定
        )

        self.lbl4 = tkinter.Label(self,text='出力結果')
        self.txt4 = ScrolledText(self, font=("", 15), height=10, width=30)

        button = tk.Button(self, text="Save", command=self.save_text)
        button.grid(row = 7, column = 2, columnspan = 3)

        self.button0.grid(row = 8, column = 2, columnspan = 3)

        self.radio0.grid(row = 2, column = 3, sticky="w")
        self.radio1.grid(row = 2, column = 4, sticky="w")

        self.lbl3.grid(row = 2, column = 1, rowspan = 2)
        self.txt3.grid(row = 2, column = 2)
        self.txt3a.grid(row = 3, column = 2)
        self.radio3.grid(row = 3, column = 3, sticky="w")
        self.radio4.grid(row = 3, column = 4, sticky="w") 

        self.lbl4.grid(row = 4, column = 2, columnspan = 3)
        self.txt4.grid(row = 5, column = 2, columnspan = 3)       




    def save_text(self):
        self.txt4.delete("1.0", tk.END)

        if self.radio_value.get()==0:
            self.insert_text1()
        else:
            self.insert_text2()

    def insert_text1(self):
        # ScrolledTextウィジェット内にテキストを挿入
        if self.radio_value1.get()==0:
            text3 = int(self.txt3.get())+int(self.txt3a.get())
        else:
            text3 = int(int(self.txt3.get())+int(self.txt3a.get()))*1.1

        self.txt4.insert(tk.END, "【定価】\n"+str(math.ceil(int(text3)))+"\n")
        self.txt4.insert(tk.END, "【楽天・ヤフー】\n"+str(math.ceil(int(text3)*0.8+800))+"\n")
        self.txt4.insert(tk.END, "【wauma】\n"+str(math.ceil(int(text3)*0.8))+"\n")
        self.txt4.insert(tk.END, "【原価】\n"+str(math.ceil(int(text3)*0.63))+"\n")

    def insert_text2(self):
        # ScrolledTextウィジェット内にテキストを挿入
        if self.radio_value1.get()==0:
            text3 = int(self.txt3.get())+int(self.txt3a.get())
        else:
            text3 = int(int(self.txt3.get())+int(self.txt3a.get()))*1.1

        self.txt4.insert(tk.END, "【定価】\n"+str(math.ceil(int(text3)))+"\n")
        self.txt4.insert(tk.END, "【楽天・ヤフー】\n"+str(math.ceil(int(text3)*0.85+263))+"\n")
        self.txt4.insert(tk.END, "【wauma】\n"+str(math.ceil(int(text3)*0.85+263))+"\n")
        self.txt4.insert(tk.END, "【原価】\n"+str(math.ceil(int(text3)*0.63))+"\n")

    def go_to_screen1(self):
        self.master.switch_frame("screen1.Screen1")