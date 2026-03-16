contatos = {
    "Raul":998004367,
    "Jotair":988773434,
    "Josiel Neumann Kuk":90036788
}

nome = input("Insira o nome do contato\n")
for chave, valor in contatos.items():
    if nome == chave:
        print(f"{chave}: {valor}")
else:
    print("Contato não encontrado na lista.")