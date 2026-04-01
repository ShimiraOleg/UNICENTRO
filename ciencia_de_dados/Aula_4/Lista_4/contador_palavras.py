import string
import collections as coll

with open('contar_palavras.txt', 'r', encoding='utf-8') as f:
    texto = f.read().lower()
    for p in string.punctuation:
        texto = texto.replace(p, '')
    palavras = texto.split()
    contador = coll.Counter(palavras)
    print("Top 10 palavras mais comuns no texto: ")
    for palavra, freq in contador.most_common(10):
        print(f"'{palavra}' aparece {freq} vezes")