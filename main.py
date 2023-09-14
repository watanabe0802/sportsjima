import tkinter as tk
from screen1 import Screen1
from screen2 import Screen2
from setting import Setting


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Application")
        self._frame = None
        self.switch_frame("screen1.Screen1")

    def switch_frame(self, frame_name):
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