import pandas as pd

# Criar dados fictícios
data = {
    'feature1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'feature2': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    'feature3': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

df = pd.DataFrame(data)
df.to_csv('network_traffic_data.csv', index=False)
print("Conjunto de dados fictício criado com sucesso!")
