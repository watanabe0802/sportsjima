import tkinter as tk
import tkinter
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from bs4 import BeautifulSoup
import csv
import pprint

class Screen3(tk.Frame):

    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.master.geometry("1000x1000")
        self.init_screen()
        self.html0 = '''</td></tr>'''
        self.html1 = '''<table width=100% cellpadding=4 cellspacing=1 style="color:#333333; line-height:1.3em; font-size:18px;">'''
        self.html2 = '''<tr><th bgcolor=#FFA07A>ブランド</th><td>'''
        self.html3 = '''<tr><th bgcolor=#FFA07A>対象</th><td>'''
        self.html4 = '''<tr><th bgcolor=#FFA07A>商品名</th><td>'''
        self.html5 = '''<tr><th bgcolor=#FFA07A>サイズ</th><td>'''
        self.html6 = '''<tr><th bgcolor=#FFA07A>カラー</th><td>'''
        self.html7 = '''<tr><th bgcolor=#FFA07A>素材</th><td>'''
        self.html8 = '''<tr><th bgcolor=#FFA07A>特徴</th><td>'''
        self.html9 = '''</table>'''
        self.html10 = '''<br>'''
    def init_screen(self):

        def read_csv_file(file_path):
            data = []
            with open(file_path, newline='',encoding='utf-8') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    data.extend(row)
            return data
        
        makerlist = read_csv_file('maker.csv')
        gender = read_csv_file('gender.csv')




########ウィジェット定義###################################################################################################################333
        self.lbl_goods_information = tkinter.Label(self,text='商品情報')
        self.txt_goods_information = ScrolledText(self, font=("", 10), height=15, width=40)

        self.lbl_goods_information2 = tkinter.Label(self,text='特徴')
        self.txt_goods_information2 = ScrolledText(self, font=("", 10), height=15, width=40)        

        self.lbl_generate_html = tkinter.Label(self,text='生成結果')
        self.txt_generate_html = ScrolledText(self, font=("",10), height=20, width=100)

        self.lbl_goods_title = tkinter.Label(self,text='商品名')
        self.txt_goods_title = tkinter.Entry(self,width=20)

        self.lbl_maker = tkinter.Label(self,text='メーカー')
        self.maker_combobox = ttk.Combobox(self, height=len(makerlist) , values=makerlist , justify="center")
        self.lbl_gender = tkinter.Label(self,text='対象')
        self.gender_combobox = ttk.Combobox(self, height=len(gender) , values=gender , justify="center")



        self.back_button = tk.Button(self, text="戻る", command=self.go_to_home)
        self.generate_button = tk.Button(self, text="生成", command=self.save_text)
#############################################################################################################################################        
        #商品名
        self.lbl_goods_title.grid(row = 0, column = 0 )
        self.txt_goods_title.grid(row = 0, column = 1 )
        #メーカー
        self.lbl_maker.grid(row = 1, column = 0)
        self.maker_combobox.grid(row = 1, column = 1 )
        #対象
        self.lbl_gender.grid(row = 1, column = 2 )
        self.gender_combobox.grid(row = 1, column = 3 )
        #特徴
        self.lbl_goods_information2.grid(row = 2, column = 0 )
        self.txt_goods_information2.grid(row = 2, column = 1 )
        #商品情報
        self.lbl_goods_information.grid(row = 2, column = 2 )
        self.txt_goods_information.grid(row = 2, column = 3 )
        #生成結果
        self.lbl_generate_html.grid(row = 4, column = 0 )
        self.txt_generate_html.grid(row = 4, column = 1 ,columnspan = 3, pady=20 )

        #生成ボタン
        self.generate_button.grid(row = 5, column = 2,sticky=tkinter.NSEW)
        self.back_button.grid(row = 6, column = 2,sticky=tkinter.NSEW)




############################################################################################################################################# 
    def read_text_lines(self,a,):
        text_lines = []

        # ScrolledTextウィジェットからテキストを取得
        text = a.get("1.0", "end-1c")  # 1行目から最終行の1文字前までを取得

        # 改行文字（\n）でテキストを分割し、リストに追加
        text_lines = text.split('\n')

        # リスト内の空の行を削除
        text_lines = [line for line in text_lines if line.strip() != '']

        return text_lines    




    def save_text(self):
        self.txt_generate_html.delete("1.0", tk.END)
        lines = self.read_text_lines(self.txt_goods_information)
        lines2 = self.read_text_lines(self.txt_goods_information2)
        count = 0
        size = []
        color = []
        material = []
        for line in lines:
            if "サイズ：" in line:
                a = lines.index(line)  # "サイズ："の行のインデックスを取得
                size_count = 0  # サイズのカウントを初期化
                a += 1  # 次の行から開始
                while a < len(lines) and ":" not in lines[a]:
                    size.append(lines[a])  # サイズをリストに追加
                    size_count += 1
                    a += 1

            elif "カラー：" in line:
                a = lines.index(line)  # "カラー："の行のインデックスを取得
                color_count = 0  # カラーのカウントを初期化
                a += 1  # 次の行から開始
                while a < len(lines) and ":" not in lines[a]:
                    color.append(lines[a])  # カラーをリストに追加
                    color_count += 1
                    a += 1

            elif "素材：" in line:
                a = lines.index(line)  # "素材："の行のインデックスを取得
                material_count = 0  # 素材のカウントを初期化
                a += 1  # 次の行から開始
                while a < len(lines) and ":" not in lines[a]:
                    material.append(lines[a])  # 素材をリストに追加
                    material_count += 1
                    a += 1        
    



        self.txt_generate_html.insert(tk.END, self.html1+"\n")
        self.txt_generate_html.insert(tk.END, self.html2+self.maker_combobox.get()+self.html0+"\n")
        self.txt_generate_html.insert(tk.END, self.html3+self.gender_combobox.get()+self.html0+"\n")
        self.txt_generate_html.insert(tk.END, self.html4+self.txt_goods_title.get()+self.html0+"\n")
        #サイズ
        self.txt_generate_html.insert(tk.END, self.html5+"\n")
        print(size)
        print(size_count)
        for a1 in range (size_count):
            self.txt_generate_html.insert(tk.END, size[a1]+self.html10+"\n")
            
        self.txt_generate_html.insert(tk.END, self.html0+"\n")
        

        #カラー
        self.txt_generate_html.insert(tk.END, self.html6+"\n")
        for b in range (color_count):
            self.txt_generate_html.insert(tk.END, color[b]+self.html10+"\n")
            
        self.txt_generate_html.insert(tk.END, self.html0+"\n")
        

        #素材
        self.txt_generate_html.insert(tk.END, self.html7+"\n")
        for c in range (material_count):
            self.txt_generate_html.insert(tk.END, material[c]+self.html10+"\n")
            
        self.txt_generate_html.insert(tk.END, self.html0+"\n")
        

        #特徴
        self.txt_generate_html.insert(tk.END, self.html8+"\n")
        for d in lines2:
            self.txt_generate_html.insert(tk.END, d+self.html10+"\n")
            
        self.txt_generate_html.insert(tk.END, self.html0+"\n")
        

        self.txt_generate_html.insert(tk.END, self.html9+"\n")



    def go_to_home(self):
        self.master.switch_frame("home.Home")