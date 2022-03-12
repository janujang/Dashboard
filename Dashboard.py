from tkinter import *
import os
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

root = Tk()
root.title("Fridge Dashboard")

def loadCSV():
    filename = filedialog.askopenfile(initialdir="/", title="Select csv")
    print (filename)


def matplotCanvas():
    figure1 = Figure(figsize=(5,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    ax1.plot([1,2,3,4,5,6,7,8], [23,22,34,2,1,44,2,23])
    ax1.set_title("Average temperature")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Temp (C)")

    figureCanvas = FigureCanvasTkAgg(figure1, root)
    # canvas.show()
    figureCanvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
    # side=BOTTOM, fill=BOTH, expand=TRUE

    figure2 = Figure(figsize=(5,5), dpi=100)
    ax2 = figure2.add_subplot(111)
    ax2.plot([1,2,3,4,5,6,7,8], [23,22,34,2,1,44,2,23])
    ax2.set_title("Temperature Deviation")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Deviation")

    figureCanvas = FigureCanvasTkAgg(figure2, root)
    # canvas.show()
    figureCanvas.get_tk_widget().pack(side=LEFT, fill=BOTH)



matplotCanvas()
# canvas = Canvas(height=700, width=1000, bg="white")
# canvas.pack()

# frame = Frame(root, bg="black")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
label = Label(text="Actions")
label.pack()

openFile = Button(text="Open log", padx=10, pady=5, command=loadCSV)
openFile.pack()



root.mainloop()