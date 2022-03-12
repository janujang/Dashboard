from tkinter import *
import os
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
root = Tk()


def loadCSV():
    filename = filedialog.askopenfile(initialdir="/", title="Select csv")
    print (filename)


def matplotCanvas():
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    a.plot([1,2,3,4,5,6,7,8], [23,22,34,2,1,44,2,23])

    canvas = FigureCanvasTkAgg(f)
    canvas.show()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=TRUE)


matplotCanvas()
canvas = Canvas(root, height=700, width=1000, bg="white")
canvas.pack()

frame = Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
label = Label(root, text="Hello World!")

openFile = Button(root, text="Open log", padx=10, pady=5, command=loadCSV)

openFile.pack()


root.mainloop()