import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')
print('Коэффициент корреляции Пирсона между возрастом и параметром survived:')
beta2 = data[['Age', 'Survived']]
colleration = beta2.corr(method='pearson')
print(colleration)

print('Коэффициент корреляции Пирсона между полом человека и параметром survived:')
beta2 = data[['Sex', 'Survived']]
colleration = beta2.corr(method='pearson')
print(colleration)

print('Коэффициент корреляции Пирсона между классом, в котором пассажир ехал, и параметром survived:')
beta2 = data[['Pclass', 'Survived']]
colleration = beta2.corr(method='pearson')
print(colleration)
