import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import os

# Comando para limpar o terminal ao executar o código
os.system("cls")

# Localização do arquivo da base de dados
base = "diabeticos.txt"
arquivo = Path(__file__).parent / "data" / base

# Lendo a base de dados
dados = np.loadtxt(arquivo)

# Separando as duas colunas da base de dados em variáveis próprias, "padroes" e "rotulos"
# Foi realizada uma limpa para valores de glicemia iguais a zero
# a fim de deixar os dados mais precisos e deletar medições não realizadas 
# que estivessem presentes na base de dados
padroes = np.delete(dados[:, 0], np.where(dados[:, 0] == 0))  # Vetor de Glicemia
rotulos = np.delete(dados[:, 1], np.where(dados[:, 0] == 0))  # Vetor de Rótulos (0 = não diabético, 1 = diabético)

# Tamanho total dos vetores
N = padroes.size

# Criação de vetores de índice separando as classes
simDiabeticos = np.where(rotulos == 1)[0]  # Índices onde o padrão é diabético
naoDiabeticos = np.where(rotulos == 0)[0]  # Índices onde o padrão não é diabético

# Tamanho de padrões diabéticos e não diabéticos
Nsim = simDiabeticos.size
Nnao = naoDiabeticos.size

# Cálculos de probabilidades das classes
p0 = Nnao / N   # Probabilidade de um padrão ser não diabético (classe 0)
p1 = Nsim / N   # Probabilidade de um padrão ser diabético (classe 1)

# Cálculo da Impureza do nó (Impureza inicial antes da divisão)
# Baseado na entropia de Shannon
I = -p0 * np.log2(p0) - p1 * np.log2(p1)

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

_, melhorAlpha = entropia(padroes, rotulos, I)

# O melhor limiar ficou definido com "melhorAlpha" (ex: 127.0 de glicose)
# Agora é preciso separar entre menores ou iguais e maiores que esse limiar
# Verificar a presença das classes 0 (não diabético) e 1 (diabético) para cada um dos nós

# Índices dos padrões menores ou iguais ao melhorAlpha (NodeYes)
NodeYes = np.where(padroes <= melhorAlpha)[0]
# Índices dos padrões do NodeYes que são da classe 0
N0Yes = NodeYes[np.where(rotulos[NodeYes] == 0)[0]]
# Índices dos padrões do NodeYes que são da classe 1
N1Yes = NodeYes[np.where(rotulos[NodeYes] == 1)[0]]

# Índices dos padrões maiores que melhorAlpha (NodeNo)
NodeNo = np.where(padroes > melhorAlpha)[0]
# Índices dos padrões do NodeNo que são da classe 0
N0No = NodeNo[np.where(rotulos[NodeNo] == 0)[0]]
# Índices dos padrões do NodeNo que são da classe 1
N1No = NodeNo[np.where(rotulos[NodeNo] == 1)[0]]

# Processo de classificação usando o limiar encontrado
# Se glicemia <= melhorAlpha, classifica como 0 (não diabético)
# Se glicemia > melhorAlpha, classifica como 1 (diabético)
previsoes = np.zeros(rotulos.shape)
for i in range(N):
    x = padroes[i]
    if x <= melhorAlpha:
        previsoes[i] = 0
    else:
        previsoes[i] = 1

# Cálculo do número de acertos
NAcertos = np.sum(previsoes == rotulos)

# Cálculo da acurácia
acuracia = NAcertos / N

# Impressão dos resultados
print(f"Melhor Limiar: {melhorAlpha}")
print(f"Número de acertos: {NAcertos}")
print(f"Acurácia: {acuracia * 100:.2f}%")

fig, ax = plt.subplots()
ax.scatter(padroes[naoDiabeticos], rotulos[naoDiabeticos], color="blue", label="classe 0")
ax.scatter(padroes[simDiabeticos], rotulos[simDiabeticos], color="red", label="classe 1")
ax.legend()
plt.show()