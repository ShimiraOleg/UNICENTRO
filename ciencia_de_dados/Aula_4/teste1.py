from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")

##url = ("https://sguweb.unicentro.br/")

html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

important_paragraphs = soup('p', {'class':'important'})
spans_inside_divs = [span
                     for div in soup('div')
                     for span in div('span')]

#print(html)
print(important_paragraphs)
print(spans_inside_divs)