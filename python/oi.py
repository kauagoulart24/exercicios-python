import numpy as np

# Matriz de consumo (linhas = recursos: Dev, Cloud, Suporte | colunas = produtos: CRM, BI, IoT)
A = np.array([
    [12, 18, 10],
    [4,  7,  6],
    [3,  5,  4]
])

q_atual = np.array([80, 50, 40])      # vetor produção
c = np.array([70, 25, 40])            # custo por hora
margem = np.array([900, 1300, 1100])  # margem por unidade
capacidade = np.array([2000, 700, 500])

consumo = A @ q_atual                 # A · q -> consumo total de cada recurso
custo_total = np.dot(consumo, c)
margem_total = np.dot(q_atual, margem)
viavel = np.all(consumo <= capacidade)

print("Consumo (Dev, Cloud, Suporte):", consumo)
print("Custo total: R$", custo_total)
print("Margem total: R$", margem_total)
print("Viável?", viavel)