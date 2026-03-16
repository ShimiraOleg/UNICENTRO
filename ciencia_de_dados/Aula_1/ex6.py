def distancia_euclidiana(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

ponto1 = (1, 2)
ponto2 = (4, 6)
print(f"Distância: {distancia_euclidiana(ponto1, ponto2)}")