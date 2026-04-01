import requests
import collections as coll

tema = input('insira o tópico a ser pesquisado no Git: ')
url = "https://api.github.com/search/repositories"
params = {
    'q': tema,
    'per_page': 5
}
try:
    response = requests.get(url, params=params, timeout=10)
    dados = response.json()

    print(f'5 primeiros repositorios sobre {tema}')
    for rep in dados.get('items', []):
        print(f'\n{rep['name']}')
        print(rep['html_url'])
except requests.RequestException as err:
    print("ERRO - ",err)