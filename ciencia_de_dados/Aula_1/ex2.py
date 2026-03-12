items = ["esfera", "quadrado", "triangulo", "retangulo", "ornitorrinco"]
print("Lista Original")
for item in items:
    print(item)
print()
items.append("pentagono")
items.append("hexagono")
items.remove("ornitorrinco")
print("Lista Modificada")
for item in items:
    print(item)