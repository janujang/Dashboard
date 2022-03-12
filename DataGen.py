

import csv
import random
import time

x_value = 0
temp_1 = 1000
temp_2 = 1000
temp_3 = 1000
temp_4 = 1000
temp_5 = 1000
fan = 0
compressor = 0

fieldnames = ["x_value", "temp_1", "temp_2", "temp_3", "temp_4", "temp_5", "fan", "compressor"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "temp_1" : temp_1,
            "temp_2" : temp_2,
            "temp_3" : temp_3,
            "temp_4" : temp_4,
            "temp_5" : temp_5,
            "fan" : fan,
            "compressor" : compressor
        }

        csv_writer.writerow(info)
        print("time:", x_value, "temp_1:", temp_1, "temp_2:", temp_2, "temp_3:", temp_3, "temp_4:", temp_4, "temp_5:", temp_5, "fan:", fan, "compressor:", compressor)

        x_value += 1
        #temperatures likely won't exceed (0, 8) celcius, fan and compressor are either on or off
        temp_1 = random.randint(0, 8)
        temp_2 = random.randint(0, 8)
        temp_3 = random.randint(0, 8)
        temp_4 = random.randint(0, 8)
        temp_5 = random.randint(0, 8)
        fan = random.randint(0, 1)
        compressor = random.randint(0, 1)

    time.sleep(1)