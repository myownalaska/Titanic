"""
    Посчитайте среднюю цену за билет и медиану.
    """

import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')
df=pd.Series(data['Fare'])
print(df.describe())
print('median: ',df.median())