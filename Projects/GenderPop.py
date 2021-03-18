# Population by Gender


import csv
import math
import matplotlib.pyplot as plt
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
size = []
name = input('Enter desired district name in Korean (ex. 제주특별자치도): ')

for row in data:
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i].replace(',','')))
            f.append(int(row[i+103].replace(',','')))
            size.append(math.sqrt(int(row[i].replace(',',''))+int(row[i+103].replace(',',''))))    # sqrt of sum
        break    # only search for first district match (Jeju Island)

plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.figure(figsize=(10,5), dpi=300)
plt.title(name+' District's Gender Population graph')
plt.scatter(m, f, s=size, c=range(101), alpha=0.7, cmap='jet')
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g')
plt.xlabel('Male Population')
plt.ylabel('Female Population')
plt.show()
# f.close()    # f taken up by f=[]