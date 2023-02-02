import tkinter
from PIL import ImageTk, Image

from Rules import Rules

from NewGame import NewGame


class GameWindow:
    def __init__(self):
        # create window object
        window = tkinter.Tk()

        # initialise tkinter window with dimensions
        window.geometry("1920x1080")

        # initialising the grid
        window.columnconfigure(0, weight=1, minsize=100) # weight=1 for dynamic cells, minsize for minimum size of cell
        window.columnconfigure(1, weight=1, minsize=100) # weight=1 for dynamic cells, minsize for minimum size of cell
        for i in range(6):
            window.rowconfigure(i, weight=1, minsize=100)
            for j in range(2):
                frame = tkinter.Frame(
                    master=window,
                    relief=tkinter.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j)  # allows every 'frame' to be attached to the window

        # creating buttons
        btn_rules = tkinter.Button(window, text="Rules", width=100, command=self.rules) #when clicked, opens Rules
        btn_loadgame = tkinter.Button(window, text="Load Game", width=100)
        btn_newgame = tkinter.Button(window, text="New Game", width=100, command= self.newgame)

        # positioning buttons
        btn_rules.grid(row=2, column=0, pady=2, sticky="ns")
        btn_loadgame.grid(row=3, column=0, pady=2, sticky="ns")
        btn_newgame.grid(row=4, column=0, pady=2, sticky="ns")

        # carrom image
        img_raw = Image.open("/Users/ashri/IdeaProjects/game/src/assets/vector-carrom-board.png")
        img_dims = img_raw.resize((500, 500))  # resize the image
        carrom1_img = ImageTk.PhotoImage(img_dims)
        my_label = tkinter.Label(image=carrom1_img)
        my_label.grid(row=1, column=1, pady=2, rowspan=4, sticky="nsew")

        # creating the title
        lbl_title = tkinter.Label(master=window, text="Play Carrom!", font=("Arial", 50, "bold"))
        # positioning the title
        lbl_title.grid(row=0, column=0, columnspan=2)
        window.mainloop()

    def rules(self):
        Rules()

    def newgame(self):
        NewGame()



        # use rowspan to stretch an object across 2 rows and columnspan for 2 columns
        # label = tkinter.Label(master=frame)  # ,text=f"Row {i}\nColumn {j}")  # displays the row and column of each cell
        # label.pack(padx=5, pady=5)  # controls the layout of each frame\