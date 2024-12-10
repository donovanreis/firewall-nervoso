import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

# Carregar conjunto de dados
data = pd.read_csv('network_traffic_data.csv')

# Selecionar características relevantes
features = ['feature1', 'feature2', 'feature3']
X = data[features]

# Treinar o modelo de Floresta de Isolamento
model = IsolationForest(contamination=0.01)
model.fit(X)

# Salvar o modelo treinado
with open('firewall_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modelo treinado e salvo com sucesso!")
