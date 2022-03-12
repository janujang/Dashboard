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

def animate(i):
    #for posting temperature to an endpoint
    # r = requests.post('http://myserver.com/api', json={"temp": "28"}) 
    # print(r.status_code)


    #get temperature
    r = requests.get("http://api.plos.org/search?q=title:DNA")
    # print(r.content['journal'])
    temp = r.json()

    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    # y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    # plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    # plt.tight_layout()
    



ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.title("Temperature Readings")
plt.xlabel("Time (secs)")
plt.xlabel("Temp (C)")
plt.tight_layout()
plt.show()