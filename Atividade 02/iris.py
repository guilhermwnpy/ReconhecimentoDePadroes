import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numpy import log2

# Comando para limpar o terminal ao executar o código
os.system("cls")

# Localização do arquivo da base de dados
base = "iris.txt"
arquivo = Path(__file__).parent / "data" / base

# Lendo a base de dados
dados = np.loadtxt(arquivo)

padroes = dados[:, 0:4]
rotulos = dados[:, 4]

def impureza(rotulos: np.ndarray):
    I = 0
    for i in np.unique(rotulos):
        P = np.where(rotulos == i)[0].size / rotulos.size
        if P > 0:
            I -= P*log2(P)
    return I

I = impureza(rotulos)

def entropia(padrao:np.ndarray, rotulos:np.ndarray, impureza_inicial):
    """Cálculo da impureza(entropia de shannon) dos padroes"""
    ordenado = np.sort(padrao)
    limiares = (ordenado[1:] + ordenado[:-1]) / 2
    melhor_limiar = 0
    melhor_reducao = 0

    for limiar in limiares:
        sim = padrao <= limiar #  Um vetor booleano com o mesmo tamanho que o vetor original
        Is = impureza(rotulos[sim])

        nao = padrao > limiar #  Um vetor booleano com o mesmo tamanho que o vetor original
        In = impureza(rotulos[nao])

        DI = impureza_inicial - (padrao[sim].size/padrao.size) * Is - (padrao[nao].size/padrao.size) * In

        if DI > melhor_reducao:
            melhor_reducao = DI
            melhor_limiar = limiar
        
    return (melhor_reducao, melhor_limiar)

melhor1DI1, limiar1X1 = entropia(padroes[:, 0], rotulos, I) # 0.5572326878069267
melhor1DI2, limiar1X2 = entropia(padroes[:, 1], rotulos, I) # 0.2679113691892652
melhor1DI3, limiar1X3 = entropia(padroes[:, 2], rotulos, I) # 0.9182958340544894
melhor1DI4, limiar1X4 = entropia(padroes[:, 3], rotulos, I) # 0.9182958340544894

# As reduções de impureza da coluna 3 e 4 são iguais, portanto
# pode ser escolhido qualquer um dos dois para determinar o limiar

Q1s = padroes[:, 3] <= limiar1X4
rotulosQ1s = rotulos[Q1s] 
Q1s0 = rotulosQ1s[rotulosQ1s == 0].size # 50 Elementos da classe 0
Q1s1 = rotulosQ1s[rotulosQ1s == 1].size # 0 Elementos da classe 1
Q1s2 = rotulosQ1s[rotulosQ1s == 2].size # 0 Elementos da classe 2
  

Q1n = padroes[:, 3] > limiar1X4
rotulosQ1n = rotulos[Q1n]
I1 = impureza(rotulosQ1n)

melhor2DI1, limiar2X1 = entropia(padroes[:, 0][Q1n], rotulosQ1n, I1) # 0.16049997364457846
melhor2DI2, limiar2X2 = entropia(padroes[:, 1][Q1n], rotulosQ1n, I1) # 0.05823679945423099
melhor2DI3, limiar2X3 = entropia(padroes[:, 2][Q1n], rotulosQ1n, I1) # 0.6573737500732157
melhor2DI4, limiar2X4 = entropia(padroes[:, 3][Q1n], rotulosQ1n, I1) # 0.6901603707546748

Q2s = padroes[:, 3][Q1n] <= limiar2X4
rotulosQ2s = rotulosQ1n[Q2s] 
Q2s0 = rotulosQ2s[rotulosQ2s == 0].size # 0 Elementos da classe 0
Q2s1 = rotulosQ2s[rotulosQ2s == 1].size # 49 Elementos da classe 1
Q2s2 = rotulosQ2s[rotulosQ2s == 2].size # 5 Elementos da classe 2

Q2n = padroes[:, 3][Q1n] > limiar2X4
rotulosQ2n = rotulosQ1n[Q2n] 
Q2n0 = rotulosQ2n[rotulosQ2n == 0].size # 0 Elementos da classe 0
Q2n1 = rotulosQ2n[rotulosQ2n == 1].size # 1 Elementos da classe 1
Q2n2 = rotulosQ2n[rotulosQ2n == 2].size # 45 Elementos da classe 2

previsoes = np.zeros(padroes[:, 3].shape)
for i in range(padroes[:, 3].size):
    x = padroes[:, 3][i]
    if x <= limiar1X4:
        previsoes[i] = 0
    elif x <= limiar2X4:
        previsoes[i] = 1
    else:
        previsoes[i] = 2
    
NAcertos = np.sum(previsoes == rotulos)

acuracia = NAcertos / padroes[:, 3].size

# Impressão dos resultados
print(f"Melhor Limiar 1 (X4): {limiar1X4}")
print(f"Melhor Limiar 2 (X4): {limiar2X4}")
print(f"Número de acertos: {NAcertos}")
print(f"Acurácia: {acuracia * 100:.2f}%")
