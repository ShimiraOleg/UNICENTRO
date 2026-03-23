import pandas as pd

df = pd.read_csv(
    'sensores.csv',
    sep=',',
    encoding='utf-8',
    usecols=['sensor_id', 'temperatura', 'pressao', 'status'],
    dtype={
        'sensor_id': 'str',
        'temperatura': 'float64',
        'pressao': 'float64',
        'status': 'str'
    },
    na_values=['NA', '-']
)

print(f"Exemplo 6:\n{df.to_string()}\n")