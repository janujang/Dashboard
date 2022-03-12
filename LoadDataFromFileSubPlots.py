import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import requests 

plt.style.use('seaborn')

x_vals = []
y_vals = []

index = count()


# fig, ax = plt.subplots()

# fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.show()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

def animate(i):
    #for posting temperature to an endpoint
    # r = requests.post('http://myserver.com/api', json={"temp": "28"}) 
    # print(r.status_code)


    #get temperature
    # r = requests.get("http://api.plos.org/search?q=title:DNA")
    # print(r.content['journal'])
    # temp = r.json()

    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['temp_1']
    y2 = data['temp_2']

    ax1.cla()
    ax2.cla()
    ax1.plot(x, y1, label='Temp 1')
    ax2.plot(x, y2, label='Temp 2')
    ax1.set_ylim(bottom=0, top=10)
    ax2.set_ylim(bottom=0, top=10)
    ax1.set_xlim(left=max(0, i-10), right=i+10)
    ax2.set_xlim(left=max(0, i-10), right=i+10)
    # print(i)


    # plt.plot(x, y2, label='Channel 2')

    ax1.legend(loc='upper left')
    # plt.tight_layout()
    



ani = FuncAnimation(plt.gcf(), animate, interval=1000)

ax1.set_title("Temperature Readings")
ax1.set_xlabel("Time (secs)")
ax1.set_xlabel("Temp (C)")
plt.show()
plt.tight_layout()
# fig.show()