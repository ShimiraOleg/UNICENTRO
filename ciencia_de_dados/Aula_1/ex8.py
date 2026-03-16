def estatisticas(*numeros):
    total = 0
    minimo = numeros[0]
    maximo = numeros[0]
    for n in numeros:
        total += n
        if n < minimo:
            minimo = n
        if n > maximo:
            maximo = n
    media = total / len(numeros)
    return {"media": media, "maximo": maximo, "minimo": minimo}

resultado = estatisticas(4, 7, 2, 9, 1, 5)
print(resultado)