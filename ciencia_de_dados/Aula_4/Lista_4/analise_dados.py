import csv
import collections as coll

produtos = []
categoria = input('digite uma categoria: ')
with open('dados.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i in reader:
        if i['categoria'].strip().lower() == categoria.lower():
            produtos.append(float(i['preco']))

if not produtos:
    print(f"\nNenhum produto encontrado na categoria '{categoria}'")
else:
    media = sum(produtos) / len(produtos)
    print(f"\nCategoria: {categoria}")
    print(f"Produtos encontrados: {len(produtos)}")
    print(f"Preço médio: R$ {media:.2f}")
    
