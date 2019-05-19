import pandas
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

random.seed(42)

print("Dices are thrown")
ntries = 25
throws = 10
edata1 = np.array([[int(random.random() * 7) for i in range(throws)] for j in range(ntries)])
data1 = np.array([np.mean(edata1[i][...]) for i in range(len(edata1))])
edata2 = np.array([[np.sin((random.random()*2*np.pi))*3 + 3 for i in range(throws)] for j in range(ntries)])
data2 = np.array([np.mean(edata2[i][...]) for i in range(len(edata2))])
edata3 = np.array([[(6/(1 + np.exp((random.random()*10 - 5)))) for i in range(throws)] for j in range(ntries)])
data3 = np.array([np.mean(edata3[i][...]) for i in range(len(edata3))])

df1 = pandas.DataFrame(data={'experiments': data1})
df2 = pandas.DataFrame(data={'experiments': data2})
df3 = pandas.DataFrame(data={'experiments': data3})
print(stats.kstest(df1, 'norm', (df1.mean(), df1.std())))
print(stats.kstest(df2, 'norm', (df2.mean(), df2.std())))
print(stats.kstest(df3, 'norm', (df3.mean(), df3.std())))

plt.plot(list(range(ntries)), data1, color='red')
plt.plot(list(range(ntries)), data2, color='blue')
plt.plot(list(range(ntries)), data3, color='black')
plt.title('Experimental data')

df1.plot.kde(title='dice')
df2.plot.kde(title='sin')
df3.plot.kde(title='sigmoid')

plt.show()




