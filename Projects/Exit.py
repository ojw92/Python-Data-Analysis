# Station with the most exits for each hour


import csv
import matplotlib.pyplot as plt
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24
mx_station = [''] * 24

for row in data:
    row[4:] = map(int, row[4:])
    for j in range(24):
        b = row[2*j+5]
        if b > mx[j]:
            mx[j] = b
            mx_station[j] = row[3]+' ('+str(j+4)+':00)'
print(mx_station, mx)

plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')
plt.bar(range(24), mx, color='b')
plt.xticks(range(24), mx_station, rotation=90)
plt.show()