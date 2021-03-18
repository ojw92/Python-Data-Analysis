# Station with most entry for each hour (0~23)


import csv
import matplotlib.pyplot as plt
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24    # max station for each of 24 hour
mx_station = [''] * 24

for row in data:
    row[4:] = map(int, row[4:])
    for j in range(24):    # find and record 24 hours from row
        a = row[j*2 + 4]    # index of boarding passengers for each hour is represented by i = 2*j + 4
        if a > mx[j]:
            mx[j] = a
            if j+4 > 24:    # last 3 hrs are 25, 26, 27 hr, so correct them to 1, 2, 3
                j = j - 24
            mx_station[j] = row[3]+' ('+str(j+4)+':00)'    # station & hour
print(mx_station)
print(mx)

plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation=90)    # add label for each x-axis tick and rotate by 90 degrees
plt.show()