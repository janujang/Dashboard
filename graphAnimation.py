import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import requests
import math

plt.style.use('seaborn')

x_vals = []
y_vals = []

index = count()


# fig, ax = plt.subplots()

def animate(i):
    #for posting temperature to an endpoint
    # r = requests.post('http://myserver.com/api', json={"temp": "28"})
    # print(r.status_code)


    #get temperature
    #r = requests.get("http://api.plos.org/search?q=title:DNA")
    # print(r.content['journal'])
    #temp = r.json()

    data = pd.read_csv('data.csv')

    deviations = []
    avgTemp = []

    x = data.x_value
    t1 = data.temp_1
    t2 = data.temp_2
    t3 = data.temp_3
    t4 = data.temp_4
    t5 = data.temp_5
    fan = data.fan
    compressor = data.compressor

    for i in range(0, len(t1)):
        avg = 0.2*(t1[i] + t2[i] + t3[i] + t4[i] + t5[i])
        avgTemp.append(avg)
        rms = math.sqrt((0.2)*(t1[i]*t1[i] + t2[i]*t2[i] +t3[i]*t3[i] + t4[i]*t4[i] + t5[i]*t5[i])) - avgTemp[i]
        deviations.append(rms)

    plt.cla()

    plt.plot(x, avgTemp, label='Average Temperature')
    plt.plot(x, deviations, label='Temperature Deviation')
    plt.plot(x, fan, label='Fan State (on/off)')
    plt.plot(x, compressor, label='Compressor State (on/off)')

    plt.title("Retrofrigeration Data")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C")
    plt.legend(loc='upper left')

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.title("Temperature Readings")
plt.xlabel("Time (secs)")
plt.xlabel("Temp (C)")
plt.tight_layout()
plt.show()