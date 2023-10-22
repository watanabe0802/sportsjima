import tkinter as tk
import tkinter
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from bs4 import BeautifulSoup
import configparser

class Screen4(tk.Frame):

    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        config_ini = configparser.ConfigParser()
        config_ini.read('config.ini', encoding='utf-8')
        self.var1 = config_ini['DEFAULT']['rakuten_parts']
        self.var2 = config_ini['DEFAULT']['rakuten_evidence']
        self.var3 = config_ini['DEFAULT']['yahoo_parts']
        self.var4 = config_ini['DEFAULT']['yahoo_evidence']
        self.var5 = config_ini['DEFAULT']['wauma_parts']
        self.var6 = config_ini['DEFAULT']['wauma_evidence']
        self.init_screen()
    def init_screen(self):
########ウィジェット定義###################################################################################################################333
        self.lbl_generate_size = tkinter.Label(self,text='商品情報 サイズ')
        self.txt_generate_size = tkinter.Entry(self, font=("", 10), width=100)

        self.lbl_generate_evidence = tkinter.Label(self,text='生成結果 エビデンス')
        self.txt_generate_evidence = tkinter.Entry(self, font=("", 10), width=100)        

        self.lbl_generate_URL = tkinter.Label(self,text='生成結果 商品画像')
        self.txt_generate_URL = ScrolledText(self, font=("",10), height=20, width=100)

        self.lbl_Productnumber = tkinter.Label(self,text='品番')
        self.txt_Productnumber = tkinter.Entry(self,width=20)

        self.lbl_URL = tkinter.Label(self,text='URLの数')
        self.txt_URL = tkinter.Entry(self,width=20)




        self.radio_value = tk.IntVar()
        self.radio1 = tk.Radiobutton(self,
            text = "楽天",      # ラジオボタンの表示名
            variable = self.radio_value, # 選択の状態を設定する
            value = 0                    # ラジオボタンに割り付ける値の設定
        )
        self.radio2 = tk.Radiobutton(self,
            text = "ヤフー",      # ラジオボタンの表示名
            variable = self.radio_value, # 選択の状態を設定する
            value = 1                    # ラジオボタンに割り付ける値の設定
        )
        self.radio3 = tk.Radiobutton(self,
            text = "ワウマ",      # ラジオボタンの表示名
            variable = self.radio_value, # 選択の状態を設定する
            value = 2                    # ラジオボタンに割り付ける値の設定
        )




        self.back_button = tk.Button(self, text="戻る", command=self.go_to_home)
        self.generate_button = tk.Button(self, text="生成", command=self.save_text)
#############################################################################################################################################        

        #品番
        self.lbl_Productnumber.grid(row = 1, column = 0)
        self.txt_Productnumber.grid(row = 1, column = 1 )
        #URLのかず
        self.lbl_URL.grid(row = 1, column = 2 )
        self.txt_URL.grid(row = 1, column = 3 )
        #生成結果 サイズ
        self.lbl_generate_size.grid(row = 4, column = 0 )
        self.txt_generate_size.grid(row = 4, column = 1 ,columnspan = 3)
        #生清結果 エビデンス
        self.lbl_generate_evidence.grid(row = 5, column = 0 )
        self.txt_generate_evidence.grid(row = 5, column = 1 ,columnspan = 3)
        #生成結果 URL
        self.lbl_generate_URL.grid(row = 3, column = 0 )
        self.txt_generate_URL.grid(row = 3, column = 1 ,columnspan = 3, pady=20 )

        #生成ボタン
        self.generate_button.grid(row = 6, column = 2,sticky=tkinter.NSEW)
        self.back_button.grid(row = 7, column = 2,sticky=tkinter.NSEW)

        self.radio1.grid(row = 2, column = 1, sticky="w")
        self.radio2.grid(row = 2, column = 2, sticky="w")
        self.radio3.grid(row = 2, column = 3, sticky="w")




############################################################################################################################################# 

    def save_text(self):
        self.txt_generate_URL.delete("1.0", tk.END)
        self.txt_generate_size.delete("0", tk.END)
        self.txt_generate_evidence.delete("0", tk.END)

        self.line = self.txt_Productnumber.get()
        self.line2 = self.txt_URL.get()

        if self.radio_value.get()==0:
            self.insert_text1()
        elif self.radio_value.get()==1:
            self.insert_text2()
        else:
            self.insert_text3()


    def insert_text1(self):
        for num in range(1,int(self.line2)+1):
            self.txt_generate_URL.insert(tk.END, '''<img SRC="https://image.rakuten.co.jp/sportsjima/cabinet/'''+self.var1+"/"+self.line+"-728-"+str(num)+'''.jpg" width="100%" /><br><br>'''+"\n")

        self.txt_generate_size.insert(tk.END, '''<img SRC="https://image.rakuten.co.jp/sportsjima/cabinet/'''+self.var1+"/"+self.line+'''-size.gif" width="100%" /><br><br>'''+"\n")
        self.txt_generate_evidence.insert(tk.END, '''"<p><img SRC="https://image.rakuten.co.jp/sportsjima/cabinet/'''+self.var2+"/"+self.line+'''-evidence.gif" border="0" /></p><br>'''+"\n")

    def insert_text2(self):
        for num in range(1,int(self.line2)+1):
            self.txt_generate_URL.insert(tk.END, '''<img SRC="https://shopping.c.yimg.jp/lib/sportsjima/'''+self.line+"-728-"+str(num)+'''.jpg" width="100%" /><br><br>'''+"\n")

        self.txt_generate_size.insert(tk.END, '''<img SRC="https://shopping.c.yimg.jp/lib/sportsjima/'''+self.line+'''-size.gif" width="100%" /><br><br>'''+"\n")
        self.txt_generate_evidence.insert(tk.END, '''https://shopping.c.yimg.jp/lib/sportsjima/'''+self.line+'''-evidence.gif'''+"\n")

    def insert_text3(self):
        for num in range(1,int(self.line2)+1):
            self.txt_generate_URL.insert(tk.END, '''<img SRC="https://image.wowma.jp/'''+self.var5+"/"+self.line+"-728-"+str(num)+'''.jpg" width="100%" /><br><br>'''+"\n")

        self.txt_generate_size.insert(tk.END, '''<img SRC="https://image.wowma.jp/'''+self.var5+"/"+self.line+'''-size.gif" width="100%" /><br><br>'''+"\n")
        self.txt_generate_evidence.insert(tk.END, '''"<img SRC=""https://image.wowma.jp/'''+self.var5+"/"+self.line+'''-evidence.gif" width="100%" /><br><br>'''+"\n")


    def go_to_home(self):
        self.master.switch_frame("home.Home")