import numpy as np
np.random.seed(42)
vendas = np.random.randint(100, 500, size=(1,12))
vendas_semanal = vendas.reshape(3,4)

print(vendas_semanal)
print("Venda Total por Semana:")
print(f"Semana 1: {vendas_semanal[0,:].sum()}")
print(f"Semana 2: {vendas_semanal[1,:].sum()}")
print(f"Semana 3: {vendas_semanal[2,:].sum()}")
print("Média de Vendas para Cada dia da Semana:")
print(f"Dia 1: {vendas_semanal[:,0].mean()}")
print(f"Dia 2: {vendas_semanal[:,1].mean()}")
print(f"Dia 3: {vendas_semanal[:,2].mean()}")
print(f"Dia 4: {vendas_semanal[:,3].mean()}")
print(f"Dias com mais de 400 vendas: {len(vendas_semanal[vendas_semanal > 400])}")

