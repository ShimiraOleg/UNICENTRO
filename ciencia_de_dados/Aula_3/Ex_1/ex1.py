import pandas as pd

df = pd.read_csv(
    'vendas.csv',
    sep=';',
    encoding='utf-8',
    usecols=['produto','quantidade','preco_unitario'],
    dtype={
        'produto':'str',
        'quantidade':'int64',
        'preco_unitario':'float64'
    },
    na_values=['-', 'NA']
)

print(f"Exemplo 1:\n{df.to_string()}")
