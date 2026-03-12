import numpy as np
np.random.seed(42)

#Ex1
arr_sequencia = np.arange(0,10,1)
print(f"Exercicio 1: \n{arr_sequencia}\n")

#Ex2
arr = np.ones((3,3), dtype=bool)
print(f"Exercicio 2: \n{arr}\n")

#Ex3
arr_random = np.random.randint(1,100, size=(5,5))
print(f"Exercicio 3: \n{arr_random}\n")

#Ex4
impares = arr_sequencia[arr_sequencia % 2 != 0]
print(f"Exercicio 4: \n{impares}\n")

#Ex5
arr_sequencia[impares] = -1
print(f"Exercicio 5: \n{arr_sequencia}\n")

#Ex6
print(f"Exercicio 6: \n{arr_random.sum(axis=0)}\n")

#Ex7
print(f"Exercicio 7: \n{arr_random.max(axis=1)}\n")

#Ex8
a = np.array([1, 2, 3, 4, 5])
print(f"Exercicio 8: \n{a + 2}\n")
