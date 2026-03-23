import pandas as pd

df = pd.read_csv(
    'big_data_simulado.csv',
    sep=',',
    encoding='utf-8',
    usecols=['id', 'coluna_a', 'coluna_b', 'coluna_c', 'timestamp'],
    dtype={
        'id': 'int64',
        'coluna_a': 'str',
        'coluna_b': 'float64',
        'coluna_c': 'bool'
    },
    parse_dates=['timestamp']
)

df.info()