import pandas as pd
import requests

response = requests.get("https://api.dados.exemplo/usuarios")
if response.status_code == 200:
    dados_usuarios = response.json()
    df_usuarios = pd.DataFrame(dados_usuarios)
    print(df_usuarios)
else:
    print(f"ERRO: {response.status_code}")