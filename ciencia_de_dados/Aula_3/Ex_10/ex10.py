import pandas as pd

df = pd.read_csv(
    'transacoes_grandes.csv',
    sep=';',
    encoding='utf-8',
    usecols=['produto', 'quantidade', 'preco_unitario'],
    dtype={
        'produto': 'str',
        'quantidade': 'int64',
        'preco_unitario': 'float64'
    },
    chunksize=20
)

print("Exemplo 10:")
for i, chunk in enumerate(df):
    print(f"--- Bloco {i+1} ---")
    print(f"Número de linhas no bloco: {len(chunk)}")
    print(f"3 primeiras linhas:\n{chunk.head(3)}\n")