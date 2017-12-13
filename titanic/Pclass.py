import pandas as pd


def percentage(perc, whole):
    return (perc * 100) / whole


def get_nubmer_of_pclass(pclass, data=None):
    """
        Какие доли составляли пассажиры первого, второго, третьего класса?
    """
    pclassratio = data.value_counts()

    if pclass == 1:
        return pclassratio[1]
    elif pclass == 2:
        return pclassratio[2]
    else:
        return pclassratio[3]


data = pd.read_csv('train.csv', index_col='PassengerId')
f_int = get_nubmer_of_pclass(1, data['Pclass'])
s_int = get_nubmer_of_pclass(2, data['Pclass'])
t_int = get_nubmer_of_pclass(3, data['Pclass'])

total_int = f_int + s_int + t_int
print(round(percentage(f_int, total_int)), round(percentage(s_int, total_int)), round(percentage(t_int, total_int)))