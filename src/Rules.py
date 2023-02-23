import tkinter
from PIL import ImageTk, Image


class Rules:
    def __init__(self, master=None):
        # create window object
        self.window = tkinter.Tk()

        # initialise tkinter window with dimensions
        self.window.geometry("720x600")

        # initialising the grid
        self.window.columnconfigure(0, weight=1, minsize=100)
        self.window.columnconfigure(1, weight=1, minsize=100)
        for i in range(6):
            self.window.rowconfigure(i, weight=1, minsize=100)
            for j in range(2):
                frame = tkinter.Frame(
                    master=self.window,
                    relief=tkinter.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j)  # allows every 'frame' to be attached to the window



