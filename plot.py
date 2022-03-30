import csv
import numpy as np
import matplotlib.pyplot as plt

rows = []

with open("final1.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

header = rows[0]
star_data = rows[1:]

mass = []
radius = []
distance=[]
gravity = []
for star in star_data:
    mass = list(star[3]).sort()
    radius = list(star[4]).sort()
    gravity = list(star[5]).sort()
    distance = list(star[2]).sort()

x = np.array(mass)
y = np.array(radius)

plt.plot(x, y)
plt.show()