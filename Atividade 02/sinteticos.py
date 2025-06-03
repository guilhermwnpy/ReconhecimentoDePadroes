import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numpy import log2

# Comando para limpar o terminal ao executar o código
os.system("cls")

# Localização do arquivo da base de dados
base = "sinteticos1.txt"
arquivo = Path(__file__).parent / "data" / base

# Lendo a base de dados
dados = np.loadtxt(arquivo)

X1 = dados[:, 0]
X2 = dados[:, 1]
rotulos = dados[:, 2]

N = rotulos.size

N0 = np.where(rotulos == 0)[0]
N1 = np.where(rotulos == 1)[0]

P0 = N0.size / N
P1 = N1.size / N

# Impureza máxima ( Todas as probabilidades são iguais )
I = -P0 * log2(P0) - P1 * log2(P1)

# Função de cálculo de entropia de um conjunto de dados
def entropia(padrao:np.ndarray, rotulos:np.ndarray, impureza_inicial):
    """Cálculo da impureza(entropia de shannon) dos padroes"""
    ordenado = np.sort(padrao)
    limiares = (ordenado[1:] + ordenado[:-1]) / 2
    melhor_limiar = 0
    melhor_reducao = 0

    for limiar in limiares:
        # A pergunta é caso o Elemento I do padrão seja menor ou igual ao limiar
        
        # ======================
        # sim
        # ======================

        # A resposta é sim caso a condição "padrao <= limiar" seja verdadeira
        sim = padrao <= limiar #  Um vetor booleano com o mesmo tamanho que o vetor original
        
        # Cria um novo vetor, apenas com os elementos True do vetor booleano "sim"
        Ns0 = rotulos[sim][np.where(rotulos[sim] == 0)].size # Seleciona do novo vetor, apenas os que são iguais a zero 
        Ns1 = rotulos[sim][np.where(rotulos[sim] == 1)].size # Seleciona do novo vetor, apenas os que são iguais a um
        
        # Cálculo da probabilidade de um elemento dentro do subconjunto
        # Ser de determinada classe
        Ps0 = Ns0 / rotulos[sim].size # A probabilidade dada pela quantidade de elementos da classe zero dentro do subconjunto sim
        Ps1 = Ns1 / rotulos[sim].size # A probabilidade dada pela quantidade de elementos da classe um dentro do subconjunto sim

        # Cálculo da impureza da resposta
        # Impureza máxima (1) quando a probabilidade de todas as classes são a mesma
        # Impureza mínima (0) quando todos os elementos são de uma mesma classe
        Is = 0
        if Ps0 > 0:
            Is -= Ps0 * np.log2(Ps0) # Condição caso Probabilidade seja igual a 0
            # log2(0) é indefinido
        if Ps1 > 0:
            Is -= Ps1 * np.log2(Ps1) # Condição caso Probabilidade seja igual a 0
            # log2(0) é indefinido
        

        # ======================
        # não
        # ======================

        # A resposta é não caso a condição "padrao <= limiar" seja falsa
        nao = padrao > limiar #  Um vetor booleano com o mesmo tamanho que o vetor original
        
        # Cria um novo vetor, apenas com os elementos True do vetor booleano "nao"
        Nn0 = rotulos[nao][np.where(rotulos[nao] == 0)].size # Seleciona do novo vetor, apenas os que são iguais a zero 
        Nn1 = rotulos[nao][np.where(rotulos[nao] == 1)].size # Seleciona do novo vetor, apenas os que são iguais a um
        
        # Cálculo da probabilidade de um elemento dentro do subconjunto
        # Ser de determinada classe
        Pn0 = Nn0 / rotulos[nao].size # A probabilidade dada pela quantidade de elementos da classe zero dentro do subconjunto nao
        Pn1 = Nn1 / rotulos[nao].size # A probabilidade dada pela quantidade de elementos da classe um dentro do subconjunto sim

        # Cálculo da impureza da resposta
        # Impureza máxima (1) quando a probabilidade de todas as classes são a mesma
        # Impureza mínima (0) quando todos os elementos são de uma mesma classe
        In = 0
        if Pn0 > 0:
            In -= Pn0 * np.log2(Pn0) # Condição caso Probabilidade seja igual a 0
            # log2(0) é indefinido
        if Pn1 > 0:
            In -= Pn1 * np.log2(Pn1) # Condição caso Probabilidade seja igual a 0
            # log2(0) é indefinido
        
        DI = impureza_inicial - (padrao[sim].size/padrao.size) * Is - (padrao[nao].size/padrao.size) * In

        if DI > melhor_reducao:
            melhor_reducao = DI
            melhor_limiar = limiar
        
    return (melhor_reducao, melhor_limiar)

_, melhorLimiar_X1 = entropia(X1, rotulos, I)
_, melhorLimiar_X2 = entropia(X2, rotulos, I) # Melhor limiar para a Pergunta 1

# Melhor limiar encontrado em X2, sendo melhor limiar -1.55
# A pergunta Q1 será baseado na comparação de X2 com o limiar -1.55

# Pergunta Q1 resposta Sim a X2 <= -1.55
Q1s = X2 <= melhorLimiar_X2
Q1sRotulos = rotulos[Q1s]
Q1s0 = Q1sRotulos == 0  # 3 Elementos da classe 0
Q1s1 = Q1sRotulos == 1  # 250 Elementos da classe 1
# Mais de 98% dos elementos da resposta Sim são da classe 1
# então essa resposta é declarada como uma folha, onde os padrões
# contendo o atributo X2 <= -1.55 são classificados como W1


# Pergunta Q1 resposta Não a X2 <= -1.55
# Ou seja, elementos X2 > -1.55
Q1n = X2 > melhorLimiar_X2
Q1nX1 = X1[Q1n]
Q1nX2 = X2[Q1n]
Q1nRotulos = rotulos[Q1n] # Padrões que tem o atributo X2 > -1.55
Q1n0 = Q1nRotulos == 0  # 497 Elementos da classe 0
Q1n1 = Q1nRotulos == 1  # 250 Elementos da classe 1

# Probabilidade de um padrão ser de determinada classe
P0 = Q1nRotulos[Q1n0].size / Q1nRotulos.size # Probabilidade do padrão ser da classe 0
P1 = Q1nRotulos[Q1n1].size / Q1nRotulos.size # Probabilidade do padrão ser da classe 0

# Impureza do novo conjunto de dados
# Padrões com atributos X2 > -1.55
I1 = -P0 * log2(P0) - P1 * log2(P1)

_, melhorLimiar_Q1X1 = entropia(Q1nX1, Q1nRotulos, I1)
_, melhorLimiar_Q1X2 = entropia(Q1nX2, Q1nRotulos, I1) # Melhor limiar para a pergunta 2

Q2s = Q1nX2 <= melhorLimiar_Q1X2
Q2sRotulos = Q1nRotulos[Q2s]
Q2s0 = Q2sRotulos == 0 # 488 Elementos da classe 0
Q2s1 = Q2sRotulos == 1 # 0 Elementos da classe 1

Q2n = Q1nX2 > melhorLimiar_Q1X2
Q2nRotulos = Q1nRotulos[Q2n]
Q2n0 = Q2nRotulos == 0 # 9 Elementos da classe 0
Q2n1 = Q2nRotulos == 1 # 250 Elementos da classe 1

previsoes = np.zeros(X2.shape)
for i in range(N):
    x = X2[i]
    if x <= melhorLimiar_X2:
        previsoes[i] = 1
    elif x <= melhorLimiar_Q1X2:
        previsoes[i] = 0
    else:
        previsoes[i] = 1

NAcertos = np.sum(previsoes == rotulos)

acuracia = NAcertos / N

# Impressão dos resultados
print(f"Melhor Limiar 1 (X2): {melhorLimiar_X2}")
print(f"Melhor Limiar 2 (X2): {melhorLimiar_Q1X2}")
print(f"Número de acertos: {NAcertos}")
print(f"Acurácia: {acuracia * 100:.2f}%")

fig, ax = plt.subplots()
ax.scatter(X1[rotulos == 0], X2[rotulos == 0], color="blue", label="classe 0", marker="o")
ax.scatter(X1[rotulos == 1], X2[rotulos == 1], color="red", label="classe 1", marker="x")
ax.legend()
plt.show()