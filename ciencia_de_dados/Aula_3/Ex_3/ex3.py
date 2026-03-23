import pandas as pd

df = pd.read_csv(
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

print(f"Exemplo 3:\n{df.to_string()}")