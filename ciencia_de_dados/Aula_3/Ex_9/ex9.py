import pandas as pd

df = pd.read_csv(
    'notas.csv',
    sep=',',
    encoding='utf-8',
    usecols=['aluno', 'matematica', 'portugues', 'historia'],
    dtype={
        'aluno': 'str',
        'matematica': 'float64',
        'portugues': 'float64',
        'historia': 'float64'
    }
)

print("Exemplo 9:")
print(df.describe())
print(f"\nMédia por disciplina:\n{df.mean(numeric_only=True)}")