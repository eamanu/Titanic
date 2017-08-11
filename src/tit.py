import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


train = pd.read_csv('../train.csv')
test = pd.read_csv('../test.csv')

print(train.head(8))
print('Columnas %i, row %i'%(len(train.columns), len(train.index)))
print(train.describe)
print(train.isnull().sum())

sobrev = train[train['Survived'] == 1]
nosobrev = train[train['Survived'] == 0]
s_percent = s/total*100.0

def porcentajeSobreviviente(sobrev, nosobrev):
    total = sobrev + nosobrev
    s = float(len(sobrev))
    ns = float(len(nosobrev))
    print('Sobrevivió el %f porciento. En el DataFrame hay un total de %i sobrevivientes y un\
total de %i no sobrevivientes' %(s_percent, s, ns))

# Print % sobrevivientes
porcentajeSobreviviente(sobrev, nosobrev)

sobre_color = 'green'
nosobre_color = 'red'


plt.figure()
# Age study
sns.distplot(sobrev['Age'].dropna().values, bins=range(0, 100, 1), color=sobre_color, label='Sobrevivio')
sns.distplot(nosobrev['Age'].dropna().values, bins=range(0, 100, 1), color=nosobre_color,  axlabel='Age', label="No sobrevivio")
plt.show()
# Sex study
plt.figure()
sns.barplot('Sex', 'Survived', data=train, palette='Reds_d')
plt.show()


