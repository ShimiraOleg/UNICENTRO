frase = "O Rato Roeu a Roupa Do Rei De Roma e o Rei Ficou Com Raiva do Rato"
palavras = frase.lower().split()

contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

itens = list(contagem.items())
for i in range(len(itens)):
    for j in range(i + 1, len(itens)):
        if itens[j][1] > itens[i][1]:
            itens[i], itens[j] = itens[j], itens[i]

print("3 palavras mais frequentes:")
for palavra, qtd in itens[:3]:
    print(f"  '{palavra}': {qtd}x")