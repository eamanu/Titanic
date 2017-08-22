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

def porcentajeSobreviviente(sobrev, nosobrev):
    total = len(sobrev) + len(nosobrev)
    s = float(len(sobrev))
    ns = float(len(nosobrev))
    s_percent = s/total*100.0
    print('Sobrevivió el %.3f porciento. En el DataFrame hay un total de %i sobrevivientes y un\
total de %i no sobrevivientes' %(s_percent, s, ns))

# Print % sobrevivientes
# porcentajeSobreviviente(sobrev, nosobrev)

sobre_color = 'green'
nosobre_color = 'red'


def drawFirstVis(sobrev, nosobrev, sobre_color, nosobre_color):
    plt.figure()
    # Age study
    sns.distplot(sobrev['Age'].dropna().values, bins=range(0, 100, 1), color=sobre_color, label='Sobrevivio')
    sns.distplot(nosobrev['Age'].dropna().values, bins=range(0, 100, 1), color=nosobre_color,  axlabel='Age', label="No sobrevivio")
    plt.show()
    # Sex study
    plt.figure()
    sns.barplot('Sex', 'Survived', data=train, palette='Reds_d')
    plt.show()
    # Pclass Study
    plt.figure()
    sns.barplot('Pclass', 'Survived', data=train)
    plt.show()
    # SibSp study
    plt.figure()
    sns.barplot('SibSp', 'Survived', data=train)
    plt.show()
    # Parch study
    plt.figure()
    sns.barplot('Parch', 'Survived', data=train)
    plt.show()
    # Embarked Study
    plt.figure()
    sns.barplot('Embarked', 'Survived', data=train)
    plt.show()
    # Fare study
    plt.figure()
    sns.distplot(sobrev['Fare'].dropna().values, bins=range(0, 513, 1), color=sobre_color, label='Sobrevivio')
    sns.distplot(nosobrev['Fare'].dropna().values, bins=range(0, 513, 1), color=nosobre_color, label='No Sobrevivio', axlabel="Fare")
    plt.show()

# drawFirstVis(sobrev, nosobrev, sobre_color, nosobre_color)

# tab = pd.crosstab(train['Parch'], train['Survived'])

print(tab)

