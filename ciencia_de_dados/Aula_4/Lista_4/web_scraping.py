from bs4 import BeautifulSoup
import requests

try:
    url = input('Insira a url: ')
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2')

    if not titles:
        print('\n Nenhum <h2> encontrado')
    else:
        print("\nTítulos <h2> encontrados:")
        for t in titles:
            print("-", t.get_text(strip=True))
except requests.RequestException as err:
    print("ERRO - ",err)

#site usado de teste: https://www.grimmstories.com/pt/grimm_contos/o_pastorzinho