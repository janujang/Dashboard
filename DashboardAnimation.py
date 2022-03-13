from tkinter import *
import os
from tkinter import filedialog
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.pyplot import ticklabel_format
import pandas as pd
import csv
from matplotlib import style
import math

root = Tk()
root.title("Fridge Dashboard")
style.use('seaborn')
# canvas = Canvas(root, height = 700, width = 700, bg="#263D42")
# canvas.pack()
isOn = True

def loadCSV():
    filename = filedialog.askopenfile(initialdir="/", title="Select log (csv)")
    root.update()

    print (filename)

    if filename != None:
        fileData  = pd.read_csv(filename)
        x = fileData['x_value']
        temp1 = fileData['temp_1']
        plt.plot(x, temp1, label="Collected data")
        plt.show()


fig = Figure(figsize=(10,10), dpi=100)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

def animate(i):
    #for posting temperature to an endpoint
    # r = requests.post('http://myserver.com/api', json={"temp": "28"}) 
    # print(r.status_code)

    #get temperature
    # r = requests.get("http://api.plos.org/search?q=title:DNA")
    # print(r.content['journal'])
    # temp = r.json()

    dataCsv = pd.read_csv('data.csv')

    deviations = []
    avgTemp = []
    fanStates = []
    compressorStates = []

    x = dataCsv.x_value
    t1 = dataCsv.temp_1
    t2 = dataCsv.temp_2
    t3 = dataCsv.temp_3
    t4 = dataCsv.temp_4
    t5 = dataCsv.temp_5
    fan = dataCsv.fan
    compressor = dataCsv.compressor

    for i in range(0, len(t1)):
        avg = 0.2*(t1[i] + t2[i] + t3[i] + t4[i] + t5[i])
        avgTemp.append(avg)
        rms = math.sqrt((0.2)*(t1[i]*t1[i] + t2[i]*t2[i] +t3[i]*t3[i] + t4[i]*t4[i] + t5[i]*t5[i])) - avgTemp[i]
        deviations.append(rms)
        fanStates.append(fan[i])
        compressorStates.append(compressor[i])

    ax1.clear()
    ax2.clear()

    ax1.plot(x, avgTemp, label='Average Temperature')
    ax1.plot(x, deviations, label='Temperature Deviation')
    ax2.plot(x, fan, label='Fan State (on/off)')
    ax2.plot(x, compressor, label='Compressor State (on/off)')
    
    # ax1.set_ylim(bottom=0, top=10)
    # ax2.set_ylim(bottom=0, top=1)
    ax1.set_xlim(left=max(0, i-20), right=i)
    ax2.set_xlim(left=max(0, i-20), right=i)
    # ax2.set_xlim(left=max(0, i-10), right=i+10)

    # print(i)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper left')

    # plt.tight_layout()
    ax1.set_title("Temperature Data")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Temp (°C)")

    ax2.set_title("Actuator States")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("On/Off")
    ax2.set_yticks([0,1])

    if (fanStates[-1] == 1):
        fanBtn["text"] = "On"
    else:
        fanBtn["text"] = "Off"

    if (compressorStates[-1] == 1):
        compressorBtn["text"] = "On"
    else:
        compressorBtn["text"] = "Off"

    if (avgTemp[-1] >= 6):
        alertLabel["text"] = "Outside of range"
    else:
        alertLabel["text"] = "Within range"



figureCanvas = FigureCanvasTkAgg(fig, root)
figureCanvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)
# side=BOTTOM, fill=BOTH, expand=TRUE

#toolbar for figure1
toolbar = NavigationToolbar2Tk(figureCanvas, root)
figureCanvas._tkcanvas.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
#anchor=NW


ani = FuncAnimation(fig, animate, interval=1000)

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
alertLabel = Label(text="Good")
alertLabel.pack()

root.mainloop()