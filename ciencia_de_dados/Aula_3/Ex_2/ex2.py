import pandas as pd

df = pd.read_csv(
    'clima.csv',
    sep=',',
    encoding='utf-8',
    decimal='.',
    usecols=['data','temperatura_c','umidade_relativa'],
    parse_dates=['data'],
    index_col=['data'],
    dtype={
        'temperatura_c':'float64',
        'umidade_relativa':'int64'
    }
)
print(f"Exemplo 2:\n{df.to_string()}\n")
df.info()
