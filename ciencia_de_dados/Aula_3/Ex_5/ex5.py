import pandas as pd

def parse_valor(s):
    partes = s.split('.')
    if len(partes) == 3:
        return float(partes[0] + partes[1] + '.' + partes[2])
    else:
        return float(s)

df = pd.read_csv(
    'transacoes.csv',
    sep=',',
    encoding='utf-8',
    thousands='.',
    decimal='.',
    usecols=['id_transacao', 'valor', 'moeda'],
    dtype={
        'id_transacao': 'int64',
        'valor': 'str',
        'moeda': 'str'
    }
)

df['valor'] = df['valor'].apply(parse_valor)

print(f"Exemplo 5:\n{df.to_string()}\n{df.dtypes}\n")