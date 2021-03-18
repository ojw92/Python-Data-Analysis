# Total board & exit for all stations for each hour


import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
s_in = [0] * 24    # total boarded for all stations, for each hr
s_out = [0] * 24    # for exited

for row in data:
    row[4:] = map(int, row[4:])
    for i in range(24):
        s_in[i] += row[4 + i*2]    # insert boarding data by hr, summing with previous row's entries
        s_out[i] += row[5 + i*2]

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')
plt.title('Total Entry & Exit in Subway by Hour')
plt.plot(s_in, 'r', label='Entry')    # no need to enter range(24) for x-values ...
plt.plot(s_out, 'g', label='Exit')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.legend()
plt.xticks(range(24), range(4,28))    # ... because this takes care of it
plt.show()
