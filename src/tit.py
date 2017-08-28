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

# print(tab)
def ClassSexAge():
    # Class 1 Male
    msobreClass1 = train[(train['Survived'] == 1) & (train['Sex'] == 'male')
                         & (train['Pclass'] == 1)]
    mnosobreClass1 = train[(train['Survived'] == 0) & (train['Sex'] == 'male')
                           & (train['Pclass'] == 1)]
    # Class 2 Male
    msobreClass2 = train[(train['Survived'] == 1) & (train['Sex'] == 'male')
                         & (train['Pclass'] == 2)]
    mnosobreClass2 = train[(train['Survived'] == 0) & (train['Sex'] == 'male')
                           & (train['Pclass'] == 2)]
    # Class 3 Male
    msobreClass3 = train[(train['Survived'] == 1) & (train['Sex'] == 'male')
                         & (train['Pclass'] == 3)]
    mnosobreClass3 = train[(train['Survived'] == 0) & (train['Sex'] == 'male')
                           & (train['Pclass'] == 3)]
    
    # Class 1 Female
    fsobreClass1 = train[(train['Survived'] == 1) & (train['Sex'] == 'female')
                         & (train['Pclass'] == 1)]
    fnosobreClass1 = train[(train['Survived'] == 0)
                           & (train['Sex'] == 'female')
                           & (train['Pclass'] == 1)]
    # Class 2 Female
    fsobreClass2 = train[(train['Survived'] == 1) & (train['Sex'] == 'female')
                         & (train['Pclass'] == 2)]
    fnosobreClass2 = train[(train['Survived'] == 0)
                           & (train['Sex'] == 'female')
                           & (train['Pclass'] == 2)]
    # Class 3 Female
    fsobreClass3 = train[(train['Survived'] == 1) & (train['Sex'] == 'female')
                         & (train['Pclass'] == 3)]
    fnosobreClass3 = train[(train['Survived'] == 0)
                           & (train['Sex'] == 'female')
                           & (train['Pclass'] == 3)]
    plt.figure()
    plt.subplot(131)
    sns.distplot(msobreClass1['Age'].dropna().values, bins=range(0, 100, 1),
                 color=sobre_color, label='Sobreviviente Clase 1')
    sns.distplot(mnosobreClass1['Age'].dropna().values, bins=range(0, 100, 1),
                 color=nosobre_color, label='No sobreviviente Clase 1')
    plt.subplot(132)
    sns.distplot(msobreClass2['Age'].dropna().values, bins=range(0, 100, 1),
                 color=sobre_color, label='Sobreviviente Clase 2')
    sns.distplot(mnosobreClass2['Age'].dropna().values, bins=range(0, 100, 1),
                 color=nosobre_color, label='No sobreviviente Clase 2')
    plt.subplot(133)
    sns.distplot(msobreClass3['Age'].dropna().values, bins=range(0, 100, 1),
                 color=sobre_color, label='Sobreviviente Clase 3')
    sns.distplot(mnosobreClass3['Age'].dropna().values, bins=range(0, 100, 1),
                 color=nosobre_color, label='No sobreviviente Clase 3')
    plt.show()
    plt.figure()
    plt.subplot(131)
    sns.distplot(fsobreClass1['Age'].dropna().values, bins=range(0, 100, 1),
                 color=sobre_color, label='Sobreviviente Clase 1')
    sns.distplot(fnosobreClass1['Age'].dropna().values, bins=range(0, 100, 1),
                 color=nosobre_color, label='No sobreviviente Clase 1')
    plt.title("Class 1")
    plt.subplot(132)
    sns.distplot(fsobreClass2['Age'].dropna().values, bins=range(0, 100, 1),
                 color=sobre_color, label='Sobreviviente Clase 2')
    sns.distplot(fnosobreClass2['Age'].dropna().values, bins=range(0, 100, 1),
                 color=nosobre_color, label='No sobreviviente Clase 2')
    plt.title("Class 2")
    plt.subplot(133)
    sns.distplot(fsobreClass3['Age'].dropna().values, bins=range(0, 100, 1),
                 color=sobre_color, label='Sobreviviente Clase 3')
    sns.distplot(fnosobreClass3['Age'].dropna().values, bins=range(0, 100, 1),
                 color=nosobre_color, label='No sobreviviente Clase 3')
    plt.title("Class 3")
    plt.show()


def drawClassAge():
    class1 = train[(train['Pclass'] == 1)]
    class2 = train[(train['Pclass'] == 2)]
    class3 = train[(train['Pclass'] == 3)]
    plt.figure()
    ax = sns.distplot(class1['Age'].dropna().values, bins=range(0, 100, 1),
                      label="Class 1")
    ax.legend(loc="best")
    ax = sns.distplot(class2['Age'].dropna().values, bins=range(0, 100, 1),
                      label='Class 2')
    ax.legend(loc="best")
    ax = sns.distplot(class3['Age'].dropna().values, bins=range(0, 100, 1),
                      label='Class 3', axlabel='Clases')
    ax.legend(loc="best")
    plt.show()


print("Next")
combine = pd.concat([train, test])
train['Embarked'].iloc[61] = "S"
train['Embarked'].iloc[829] = "S"
print("El valor que busco es: ")
print(combine['Fare'][(combine['Pclass'] == 3) &
                      (combine['Sex'] == "male") &
                      (combine['SibSp'] == 0.0) &
                      (combine['Parch'] == 0.0) &
                      (combine['Embarked'] == "S")].dropna().median())
