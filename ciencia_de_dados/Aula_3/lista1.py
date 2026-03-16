import pandas as pd

df1 = pd.read_csv(
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
df2 = pd.read_csv(
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
df3 = pd.read_csv(
    'log_sistema.csv',
    sep=',',
    skiprows=2,
    nrows=2,
    engine='python',
    encoding='utf-8',
    usecols=['id_evento','tipo','timestamp','descricao'],
    index_col=['id_evento'],
    parse_dates=['timestamp'],
    dtype={
        'id_evento':'int64',
        'tipo':'str',
        'descricao':'str'
    },
)
df4 = pd.read_csv(
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
print(f"Exemplo 1:\n{df1.head()}\n")
print(f"Exemplo 2:\n{df2.head()}\n{df2.info()}\n")
print(f"Exemplo 3:\n{df3.head()}\n")
print(f"Exemplo 4:\n{df4.head()}\n{df4.dtypes}\n")

