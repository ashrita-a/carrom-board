import tkinter
from PIL import ImageTk, Image


class NewGame:
    def __init__(self, master=None):
        # create window object
        window = tkinter.Tk()

        # initialise tkinter window with dimensions
        window.geometry("1920x1080")

        # initialising the grid
        window.columnconfigure(0, weight=1, minsize=100)
        window.columnconfigure(1, weight=1, minsize=100)
        for i in range(6):
            window.rowconfigure(i, weight=1, minsize=100)
            for j in range(2):
                frame = tkinter.Frame(
                    master=window,
                    relief=tkinter.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j)  # allows every 'frame' to be attached to the window
                label = tkinter.Label(master=frame, text=f"Row {i}\nColumn {j}")  # displays the row and column of each cell
                label.pack(padx=5, pady=5)  # controls the layout of each frame\

        # creating entry boxes
        ebox_GameName = tkinter.Entry(window,  width=100)
        ebox_GameDate = tkinter.Entry(window,  width=100)

        # positioning entry boxes
        ebox_GameName.grid(row=1, rowspan=2, column=0, columnspan=2, pady=2, sticky="ns")
        ebox_GameDate.grid(row=4, rowspan=2, column=0, columnspan=2, pady=2, sticky="ns")

        # creating labels
        lbl_GameName = tkinter.Label(window, width=100, text="Enter Game's Name")
        lbl_GameDate = tkinter.Label(window, width=100, text="Enter Game's Date")

        # positioning entry boxes
        lbl_GameName.grid(row=0, rowspan=2, column=0, columnspan=2, pady=2, sticky="ns")
        lbl_GameDate.grid(row=3, rowspan=1, column=0, columnspan=2, pady=2, sticky="ns")