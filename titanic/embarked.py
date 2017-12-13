import pandas as pd

def get_nubmer_of_embarked(embarked, data=None):
    """
        Подсчитайте сколько пассажиров загрузилось на борт в различных портах? 
        Приведите три числа через пробел.
    """
    embarkedratio = data.value_counts()

    if embarked == 'C':
        return embarkedratio['C']
    elif embarked == 'S':
        return embarkedratio['S']
    else:
        return embarkedratio['Q']


data = pd.read_csv('train.csv', index_col='PassengerId')
c_int = get_nubmer_of_embarked('C', data['Embarked'])
q_int = get_nubmer_of_embarked('Q', data['Embarked'])
s_int = get_nubmer_of_embarked('S', data['Embarked'])

print(c_int, q_int, s_int)