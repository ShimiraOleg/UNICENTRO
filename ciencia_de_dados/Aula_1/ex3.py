def maior_nota(notas):
    maior = notas[0]
    for nota in notas:
        if nota > maior:
            maior = nota
    return maior

def menor_nota(notas):
    menor = notas[0]
    for nota in notas:
        if nota < menor:
            menor = nota
    return menor

def media(notas):
    media = 0
    for nota in notas:
        media = media + nota
    return media/len(notas)

notas = [0.1, 6.7, 9, 9, 10, 0.5]
print(f"Media: {media(notas)}\nMaior: {maior_nota(notas)}\nMenor: {menor_nota(notas)}")
