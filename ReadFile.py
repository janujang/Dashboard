import csv

temp1 = []
with open('data.csv', 'r') as file:

    reader = csv.reader(file)
    for row in reader:
        print (row)
        temp1.append(row[1])
print(temp1)