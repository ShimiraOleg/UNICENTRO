import pandas as pd

df = pd.read_csv(
    'experimento.csv',
    sep=',',
    encoding='utf-8',
    usecols=['amostra', 'ph', 'temperatura', 'concentracao'],
    dtype={
        'amostra': 'str',
        'ph': 'float64',
        'temperatura': 'float64',
        'concentracao': 'float64'
    }
)

print("Exemplo 7:")
print(f"Head:\n{df.head()}\n")
print(f"Tail:\n{df.tail()}\n")
print(f"Describe:\n{df.describe()}\n")