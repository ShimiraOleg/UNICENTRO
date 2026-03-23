import pandas as pd

df = pd.read_csv(
    'dados_sensor_gigante.csv',
    sep=',',
    encoding='utf-8',
    usecols=['sensor_id', 'temperatura', 'pressao', 'status'],
    dtype={
        'sensor_id': 'str',
        'temperatura': 'float64',
        'pressao': 'float64',
        'status': 'str'
    },
    na_values=['NA', '-'],
    chunksize=10
)

print("Exemplo 11:")
for i, bloco in enumerate(df):
    media_temp = bloco['temperatura'].mean()
    nulos_temp = bloco['temperatura'].isna().sum()
    
    print(f"Bloco {i+1}:")
    print(f"  > Temperatura Média: {media_temp:.2f}")
    print(f"  > Valores ausentes (temperatura): {nulos_temp}")
    print("-" * 30)