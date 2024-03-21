import tkinter as tk
import tkinter
import configparser
import tkinter.messagebox as messagebox
from tkinter.scrolledtext import ScrolledText

class Setting(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_screen()

    def init_screen(self):
        self.master.title("設定")
        self.pack(fill=tk.BOTH, expand=1)

        button = tk.Button(self, text="戻る", command=self.go_to_home)
        button.grid(row = 15, column = 2, columnspan = 3)

        config_ini = configparser.ConfigParser()
        config_ini.read('config.ini', encoding='utf-8')
        self.var1 = config_ini['DEFAULT']['yamato_kake']
        self.var2 = config_ini['DEFAULT']['yamato_price']
        self.var3 = config_ini['DEFAULT']['yupake_kake']
        self.var4 = config_ini['DEFAULT']['yupake_price']
        self.var5 = config_ini['DEFAULT']['yupack_kake']
        self.var6 = config_ini['DEFAULT']['yupack_price']
        self.var7 = config_ini['DEFAULT']['rakuten_parts']
        self.var8 = config_ini['DEFAULT']['rakuten_evidence']
        self.var9 = config_ini['DEFAULT']['tax']
        self.var10 = config_ini['DEFAULT']['genkaritu']

        self.lbl0 = tkinter.Label(self,text='配送方法の設定')
        self.space_label0 = tk.Label(self, text=" " * 1)


        self.lbl_yama1 = tkinter.Label(self,text='ヤマト',fg="green")
        self.lbl_yama2 = tkinter.Label(self,text='価格×')
        self.txt_yama1 = tkinter.Entry(self,width=20)
        self.lbl_yama3 = tkinter.Label(self,text='+')
        self.txt_yama2 = tkinter.Entry(self,width=20)

        self.lbl_yupake1 = tkinter.Label(self,text='ゆうパケ',fg="red")
        self.lbl_yupake2 = tkinter.Label(self,text='価格×')
        self.txt_yupake1 = tkinter.Entry(self,width=20)
        self.lbl_yupake3 = tkinter.Label(self,text='+')
        self.txt_yupake2 = tkinter.Entry(self,width=20)

        self.lbl_yupack1 = tkinter.Label(self,text='ゆうパック',fg="red")
        self.lbl_yupack2 = tkinter.Label(self,text='価格×')
        self.txt_yupack1 = tkinter.Entry(self,width=20)
        self.lbl_yupack3 = tkinter.Label(self,text='+')
        self.txt_yupack2 = tkinter.Entry(self,width=20)  
        self.space_label1 = tk.Label(self, text=" " * 1)

        self.lbl_tax = tkinter.Label(self,text='消費税')
        self.txt_tax = tkinter.Entry(self,width=20) 

        self.lbl_genka = tkinter.Label(self,text='原価率')
        self.txt_genka = tkinter.Entry(self,width=20)

        self.space_label3 = tk.Label(self, text=" " * 2)
        self.lbld0 = tkinter.Label(self,text='楽天ディレクトリの変更')
        self.space_label2 = tk.Label(self, text=" " * 2)
        self.lbld1 = tkinter.Label(self,text='楽天 商品パーツ')
        self.txtd0 = tkinter.Entry(self,width=20)
        self.lbld2 = tkinter.Label(self,text='楽天 エビデンス')
        self.txtd1 = tkinter.Entry(self,width=20)


        self.lbl0.grid(row = 0, column = 2, columnspan = 3)
        self.space_label0.grid(row = 1, column = 1)

        self.lbl_yama1.grid(row = 3, column = 1)
        self.lbl_yama2.grid(row = 3, column = 2)
        self.txt_yama1.grid(row = 3, column = 3)
        self.txt_yama1.insert(0, self.var1)
        self.lbl_yama3.grid(row = 3, column = 4)
        self.txt_yama2.grid(row = 3, column = 5)
        self.txt_yama2.insert(0, self.var2)

        self.lbl_yupake1.grid(row = 4, column = 1)
        self.lbl_yupake2.grid(row = 4, column = 2)
        self.txt_yupake1.grid(row = 4, column = 3)
        self.txt_yupake1.insert(0, self.var3)
        self.lbl_yupake3.grid(row = 4, column = 4)
        self.txt_yupake2.grid(row = 4, column = 5)
        self.txt_yupake2.insert(0, self.var4)

        self.lbl_yupack1.grid(row = 5, column = 1)
        self.lbl_yupack2.grid(row = 5, column = 2)
        self.txt_yupack1.grid(row = 5, column = 3)
        self.txt_yupack1.insert(0, self.var5)
        self.lbl_yupack3.grid(row = 5, column = 4)
        self.txt_yupack2.grid(row = 5, column = 5)
        self.txt_yupack2.insert(0, self.var6)


        self.space_label1.grid(row = 6, column = 1)


        self.lbl_tax.grid(row = 7, column = 1)
        self.txt_tax.grid(row = 7, column = 2)
        self.txt_tax.insert(0, self.var9)

        self.lbl_genka.grid(row = 8, column = 1)
        self.txt_genka.grid(row = 8, column = 2)
        self.txt_genka.insert(0, self.var10)




        self.space_label3.grid(row = 9, column = 1)
        self.lbld0.grid(row = 10, column = 2, columnspan = 3)
        self.space_label2.grid(row = 11, column = 1)
        self.lbld1.grid(row = 12, column = 1)
        self.txtd0.grid(row = 12, column = 2)
        self.txtd0.insert(0, self.var7)
        self.lbld2.grid(row = 13, column = 1)
        self.txtd1.grid(row = 13, column = 2)
        self.txtd1.insert(0, self.var8)


        button = tk.Button(self, text="保存する", command=self.save_text)
        button.grid(row = 14, column = 2, columnspan = 3)

    def save_text(self):
        #やまとの設定適用
        value0 = self.txt_yama1.get()
        Setting.update_config('config.ini','DEFAULT','yamato_kake', value0)
        value1 = self.txt_yama2.get()
        Setting.update_config('config.ini','DEFAULT','yamato_price', value1)
        
        #ゆうぱけ
        value2 = self.txt_yupake1.get()
        Setting.update_config('config.ini','DEFAULT','yupake_kake', value2)
        value3 = self.txt_yupake2.get()
        Setting.update_config('config.ini','DEFAULT','yupake_price', value3)

        #ゆうパック
        value4 = self.txt_yupack1.get()
        Setting.update_config('config.ini','DEFAULT','yupack_kake', value4)
        value5 = self.txt_yupack2.get()
        Setting.update_config('config.ini','DEFAULT','yupack_price', value5)

        value6 = self.txtd0.get()
        Setting.update_config('config.ini','DEFAULT','rakuten_parts', value6)
        value7 = self.txtd1.get()
        Setting.update_config('config.ini','DEFAULT','rakuten_evidence', value7)

        value8 = self.txt_tax.get()
        Setting.update_config('config.ini','DEFAULT','tax', value8)
        value9 = self.txt_genka.get()
        Setting.update_config('config.ini','DEFAULT','genkaritu', value9)

        messagebox.showinfo("保存", "保存しました")
    
    def update_config(file_path, section, key, value):
        # configparserオブジェクトを作成し、INIファイルを読み込む
        config = configparser.ConfigParser()
        config.read(file_path)

        # 指定されたセクションとキーの値を変更
        config.set(section, key, value)

        # 変更を保存
        with open(file_path, 'w') as config_file:
            config.write(config_file)    
        
        






    def go_to_home(self):
        self.master.switch_frame("home.Home")