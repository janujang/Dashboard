from tkinter import *
import os
from tkinter import filedialog
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import pandas as pd
import csv
from matplotlib import style

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
    # isOn = not isOn
    # if (isOn):
    #     fanBtn["text"] = "On"
    # else:
    #     fanBtn["text"] = "Off"


fig = Figure(figsize=(10,10), dpi=100)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
data, x, temp1, temp2, fan, compressor = [], [], [], [], [], []

def animate(i):
    #for posting temperature to an endpoint
    # r = requests.post('http://myserver.com/api', json={"temp": "28"}) 
    # print(r.status_code)


    #get temperature
    # r = requests.get("http://api.plos.org/search?q=title:DNA")
    # print(r.content['journal'])
    # temp = r.json()

    # use this approach to show information about the statuses and alerts
    with open('data.csv', 'r') as file:
        # [line.strip().split(',')[-1] for line in file.readlines()]
        data = file.readlines()[-1].split(',')
        # print(data)
        # reader = csv.reader(file)
        # # for row in reader:
        # #     print (row)
        # print(reader[-1])

    # use this approach to show graphs
    dataCsv = pd.read_csv('data.csv')
    x = dataCsv['x_value']
    temp1Csv = dataCsv['temp_1']
    temp2Csv = dataCsv['temp_2']
    temp3 = dataCsv['temp_3']
    temp4 = dataCsv['temp_4']
    temp5 = dataCsv['temp_5']
    # fan = dataCsv['fan']
    # compressor = dataCsv['compressor']

    # x.append(data[0])
    temp1.append(data[1])
    temp2.append(data[2])
    # temp3 = data[3]
    # temp4 = data[4]
    # temp5 = data[5]
    fan.append(data[6])
    compressor.append(data[7])

    ax1.clear()
    ax2.clear()
    ax1.plot(x, temp1Csv, label='Temp 1')
    ax2.plot(x, temp2Csv, label='Temp 2')
    ax1.set_ylim(bottom=0, top=10)
    ax2.set_ylim(bottom=0, top=10)
    # ax1.set_xlim(left=max(0, i-10), right=i+10)
    # ax2.set_xlim(left=max(0, i-10), right=i+10)
    # print(i)


    # plt.plot(x, y2, label='Channel 2')

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper left')
    # plt.tight_layout()
    ax1.set_title("Temperature Readings (1)")
    ax1.set_xlabel("Time (secs)")
    ax1.set_ylabel("Temp (C)")

    ax2.set_title("Temperature Readings (2)")
    ax2.set_xlabel("Time (secs)")
    ax2.set_ylabel("Temp (C)")

    if (fan[-1] == '1'):
        fanBtn["text"] = "On"
    else:
        fanBtn["text"] = "Off"

    # print (int(temp1[-1]))
    if (int(temp1[-1]) >= 8):
        alertLabel["text"] = "Warning"
    else:
        alertLabel["text"] = "Good"



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