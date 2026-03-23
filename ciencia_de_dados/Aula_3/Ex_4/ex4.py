import pandas as pd

df = pd.read_csv(
    'estoque.csv',
    sep=';',
    encoding='utf-8',
    decimal=',',
    usecols=['item','valor_unitario','peso_kg'],
    dtype={
        'item':'str',
        'valor_unitario':'float64',
        'peso_kg':'float64'
    },
)

print(f"Exemplo 4:\n{df.to_string()}\n{df.dtypes}\n")
