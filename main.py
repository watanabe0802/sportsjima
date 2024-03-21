import tkinter as tk
from screen1 import Screen1
from screen2 import Screen2
from screen3 import Screen3
from screen4 import Screen4
from setting import Setting
from home import Home



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application")
        self._frame = None
        self.switch_frame("home.Home")

    def switch_frame(self, frame_name):
        if frame_name == "screen1.Screen1" or frame_name =="screen2.Screen2":
            self.geometry("450x400")
        elif frame_name == "screen4.Screen4":
            self.geometry("850x500")
        elif frame_name == "setting.Setting":
            self.geometry("500x400")
        else:
            self.geometry("800x600")

        new_frame = self.create_frame(frame_name)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def create_frame(self, frame_name):
        frame_class = self.get_class(frame_name)
        new_frame = frame_class(self)
        return new_frame

    def get_class(self, class_path):
        module_name, class_name = class_path.rsplit(".", 1)
        module = __import__(module_name, fromlist=[class_name])
        return getattr(module, class_name)

if __name__ == "__main__":
    app = Application()
    app.mainloop()