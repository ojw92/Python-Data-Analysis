# Finding 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('age.csv', encoding='cp949', index_col=0)
df = df.div(df['총인구수'], axis=0)
del df['총인구수'], df['연령구간인구수']
df = df.fillna(0)    # changes NaN values to 0 in df

name = input('Enter the name of district in Korean (ex. 문래): ')
a = df.index.str.contains(name)
df2 = df[a]

plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')
#plt.title('Towns with Similar Population as ', name)
p = df.loc[np.power(df.sub(df2.iloc[0], axis=1), 2).sum(axis=1).sort_values().index[:5]].T.plot(figsize=(20,10),
                                                            title='Towns with Similar Population as '+ name)
p.set_xlabel('Age')
p.set_ylabel('Population Ratio')
plt.show()

