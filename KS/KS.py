import pandas
import matplotlib.pyplot as plt
from scipy import stats

survival = []
surm = []
surf = []
money = []
data = pandas.read_csv('train.csv')
for i in range(len(data)):
    if data['Survived'][i] > 0 and data['Age'][i] > 0:
        survival.append(data['Age'][i])

for i in range(len(data)):
    if data['Survived'][i] > 0 and data['Age'][i] > 0 and data['Sex'][i] == 'male':
        surm.append(data['Age'][i])

for i in range(len(data)):
    if data['Survived'][i] > 0 and data['Age'][i] > 0 and data['Sex'][i] == 'female':
        surf.append(data['Age'][i])

for i in range(len(data)):
    if data['Survived'][i] > 0 and data['Fare'][i] > 0:
        money.append(data['Fare'][i])

dfa = pandas.DataFrame(data={'Survived all': survival})
dfm = pandas.DataFrame(data={'Survived men': surm})
dff = pandas.DataFrame(data={'Survived women': surf})
dft = pandas.DataFrame(data={'Ticket price': money})
print(stats.kstest(dfa, 'norm', (dfa.mean(), dfa.std())))
print(stats.kstest(dfm, 'norm', (dfm.mean(), dfm.std())))
print(stats.kstest(dff, 'norm', (dff.mean(), dff.std())))
print(stats.kstest(dft, 'norm', (dft.mean(), dft.std())))

plt.pie([len(surm),len(surf)],labels=['m','f'])
plt.title('Sex of surviviors')

dfa.plot.kde(title='Age of surviviors')
dfm.plot.kde(title='Age of surviviors m')
dff.plot.kde(title='Age of surviviors f')
dft.plot.kde(title='Survived icket prices')

plt.show()




