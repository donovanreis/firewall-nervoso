import pickle
import numpy as np
from scapy.all import sniff, conf
import pyfiglet

# Configurar scapy para usar L3socket
conf.L3socket

# Carregar o modelo treinado
with open('firewall_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Função para analisar pacotes de rede
def analisar_pacote(pacote):
    if pacote.haslayer("IP"):
        ip_layer = pacote.getlayer("IP")
        source_address = ip_layer.src
        dest_address = ip_layer.dst

        # Extrair características relevantes do pacote
        features = np.array([[ip_layer.version, ip_layer.len, ip_layer.ttl]])  # Exemplo de características
        prediction = model.predict(features)

        if prediction == -1:
            print(f"Tráfego malicioso detectado de {source_address} para {dest_address}")
            bloquear_trafego(source_address)

# Função para bloquear tráfego de IP malicioso
def bloquear_trafego(ip):
    # Adicionar IP à lista negra
    with open('blacklist.txt', 'a') as f:
        f.write(f"{ip}\n")
    print(f"IP {ip} bloqueado!")

if __name__ == "__main__":
    print(pyfiglet.figlet_format("FIREWALL RAT"))
    # Capturar pacotes usando scapy
    sniff(prn=analisar_pacote, store=0)


