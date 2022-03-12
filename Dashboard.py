from tkinter import *
import os
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

root = Tk()
root.title("Fridge Dashboard")
# canvas = Canvas(root, height = 700, width = 700, bg="#263D42")
# canvas.pack()
isOn = False

def loadCSV():
    filename = filedialog.askopenfile(initialdir="/", title="Select csv")
    print (filename)
    isOn = not isOn
    if (isOn):
        fanBtn["text"] = "On"
    else:
        fanBtn["text"] = "Off"


def matplotCanvas():
    figure1 = Figure(figsize=(10,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    ax1.plot([1,2,3,4,5,6,7,8], [23,22,34,2,1,44,2,23])
    ax1.set_title("Average temperature")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Temp (C)")

    figureCanvas1 = FigureCanvasTkAgg(figure1, root)
    # canvas.show()
    figureCanvas1.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)
    # side=BOTTOM, fill=BOTH, expand=TRUE

    #toolbar for figure1
    toolbar = NavigationToolbar2Tk(figureCanvas1, root)
    figureCanvas1._tkcanvas.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    #anchor=NW
    
    figure2 = Figure(figsize=(10,5), dpi=100)
    ax2 = figure2.add_subplot(111)
    ax2.plot([1,2,3,4,5,6,7,8], [23,22,34,2,1,44,2,23])
    ax2.set_title("Temperature Deviation")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Deviation")

    figureCanvas2 = FigureCanvasTkAgg(figure2, root)
    # canvas.show()
    figureCanvas2.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)

    #toolbar for figure2
    toolbar = NavigationToolbar2Tk(figureCanvas2, root)
    figureCanvas2._tkcanvas.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    #add navigation bar for graph



matplotCanvas()
# canvas = Canvas(height=700, width=1000, bg="white")
# canvas.pack()

# frame = Frame(root, bg="grey")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
# logslabel = Label(text="Import logs")
# logslabel.pack()

openFile = Button(text="Open file", padx=10, pady=5, command=loadCSV)
openFile.pack()

fanLabel = Label(text="Fan Status")
fanLabel.pack()
fanBtn = Button(text="On", padx=10, pady=5, bg="green")
fanBtn.pack()

compressorLabel = Label(text="Compressor Status")
compressorLabel.pack()
compressorBtn = Button(text="On", padx=10, pady=5, bg="green")
compressorBtn.pack()


#Alerts


root.mainloop()