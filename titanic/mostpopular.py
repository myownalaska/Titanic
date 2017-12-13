"""
     Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
import pandas as pd

data = pd.read_csv('train.csv', index_col='PassengerId')
# age_bins = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90]
# data["AgeR"] = pd.cut(data["Age"].fillna(-1), bins=age_bins).astype(object)


