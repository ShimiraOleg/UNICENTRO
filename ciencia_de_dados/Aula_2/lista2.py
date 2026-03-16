import numpy as np
np.random.seed(42)

#Ex1
temps = np.array([22, 24, 21, 23, 25, 20, 22])
print(f"Exercicio 1: Média {temps.mean():.2f}, Dia mais quente {temps.max()}\n")

#Ex2
vendas = np.random.randint(50, 201, size=(3, 4))
print(f"Exercicio 2: {vendas.sum(axis=1)}\n")

#Ex3
scores = np.array([75, 88, 92, 65, 70, 80, 95, 60, 85, 78])
print(f"Exercicio 3: Mínimo {scores.min()}, Máximo {scores.max()}\n")

#Ex4
sensores = np.random.rand(20)
print(f"Exercicio 4: {sensores[sensores > 0.7]}\n")

#Ex5
precos = np.array([120.50, 121.00, 119.80, 122.30, 120.00])
print(f"Exercicio 5: {(np.diff(precos) / precos[:-1]) * 100}\n")

#Ex6
print(f"Exercicio 6: \n{np.eye(4)}")

#Ex7
print(f"Exercicio 7: Zeros \n{np.zeros((3,3))} \nUns \n{np.ones((2,5))}\n")

#Ex8
arr_1d = np.random.rand(25)
print(f"Exercicio 8: \n{arr_1d.reshape(5, 5)}\n")

#Ex9
arr_seq = np.arange(10)
print(f"Exercicio 9: {arr_seq[arr_seq % 2 == 0]}\n")

#Ex10
arr_soma = np.array([1, 2, 3, 4, 5])
print(f"Exercicio 10: {np.cumsum(arr_soma)}\n")

#Ex11
arr_uniq = np.array([1, 2, 2, 3, 4, 4, 4, 5])
print(f"Exercicio 11: {np.unique(arr_uniq)}\n")

#Ex12
print(f"Exercicio 12: {np.linspace(0, 10, 5)}\n")

#Ex13
notas = np.array([80, 90, 70])
pesos = np.array([0.3, 0.5, 0.2])
print(f"Exercicio 13: {np.average(notas, weights=pesos)}\n")

#Ex14
matriz_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Exercicio 14: \n{matriz_2x3.T}\n")

#Ex15
matriz_3x4 = np.random.randint(0, 10, (3, 4))
print(f"Exercicio 15: \n{np.flip(matriz_3x4, axis=0)}\n")

#Ex16
a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
print(f"Exercicio 16: {a == b}\n")

#Ex17
rand_10 = np.random.randint(0, 101, 10)
print(f"Exercicio 17: {rand_10 > 50}\n")

#Ex18
arr_7 = np.array([1, 7, 3, 7, 5, 7])
print(f"Exercicio 18: {np.count_nonzero(arr_7 == 7)}\n")

#Ex19
arr_round = np.array([1.23, 2.78, 3.50, 4.11])
print(f"Exercicio 19: {np.round(arr_round).astype(int)}\n")

#Ex20
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(f"Exercicio 20: \n{np.vstack((v1, v2))}\n")