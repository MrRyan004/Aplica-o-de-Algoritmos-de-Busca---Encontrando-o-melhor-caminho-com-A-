import heapq
import csv

"""
FUNÇÃO: carregar_mapa

Responsável por ler o arquivo CSV e transformar em uma matriz (lista de listas).

Cada linha do CSV vira uma linha da matriz.
Cada valor é convertido para inteiro:
- 0 → caminho livre
- 1 → obstáculo

Essa matriz será usada pelo algoritmo como "mapa do ambiente".
"""
def carregar_mapa():
    mapa = []
    with open("mapa.csv", newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            mapa.append([int(valor) for valor in linha])
    return mapa


"""
FUNÇÃO: heuristica

Calcula a estimativa de distância entre dois pontos.

Aqui usamos a distância de Manhattan:
- Soma das diferenças de linha e coluna
- Não considera diagonal

Isso ajuda o algoritmo a "ter uma noção" de qual caminho parece mais próximo do destino.
"""
def heuristica(ponto_atual, destino):
    return abs(ponto_atual[0] - destino[0]) + abs(ponto_atual[1] - destino[1])


"""
FUNÇÃO: busca_a_estrela

Essa é a implementação do algoritmo A*.

IDEIA GERAL:
O algoritmo não percorre um único caminho até o fim.
Ele mantém várias possibilidades ao mesmo tempo e sempre escolhe a mais promissora.

ESTRUTURAS IMPORTANTES:

- fila_aberta:
  Guarda os pontos que ainda serão explorados.
  É uma fila de prioridade (heap), onde o menor custo sai primeiro.

- custo_g:
  Guarda o custo real já percorrido até cada ponto.

- veio_de:
  Guarda o "caminho percorrido", ou seja, de qual ponto viemos.
  Isso permite reconstruir o caminho no final.

PROCESSO:

1. Começa no ponto inicial
2. Analisa os vizinhos (cima, baixo, esquerda, direita)
3. Calcula o custo de ir até cada vizinho
4. Escolhe sempre o próximo ponto com menor custo total
5. Repete até chegar no destino
"""
def busca_a_estrela(mapa, inicio, destino):
    linhas = len(mapa)
    colunas = len(mapa[0])

    fila_aberta = []
    heapq.heappush(fila_aberta, (0, inicio))

    veio_de = {}
    custo_g = {inicio: 0}

    """
    DIREÇÕES POSSÍVEIS:

    Cada tupla representa um movimento:
    (-1,0) → sobe
    (1,0)  → desce
    (0,-1) → esquerda
    (0,1)  → direita

    Não usamos diagonal neste caso.
    """
    direcoes = [(-1,0), (1,0), (0,-1), (0,1)]

    while fila_aberta:
        _, atual = heapq.heappop(fila_aberta)

        """
        Se chegou no destino:
        Reconstruímos o caminho voltando pelos "pais"
        (usando o dicionário veio_de)
        """
        if atual == destino:
            caminho = []
            while atual in veio_de:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            return caminho[::-1]

        """
        EXPLORAÇÃO DOS VIZINHOS:

        "Vizinho" é qualquer posição adjacente ao ponto atual.
        Ou seja, os pontos que podemos alcançar com um único movimento.

        Exemplo:
        Se estou em (2,2), os vizinhos são:
        (1,2), (3,2), (2,1), (2,3)

        O algoritmo testa cada vizinho para decidir se vale a pena ir até ele.
        """
        for d in direcoes:
            vizinho = (atual[0] + d[0], atual[1] + d[1])

            """
            VERIFICAÇÕES IMPORTANTES:

            1. O vizinho está dentro do mapa?
            2. Não é obstáculo?
            """
            if 0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas:
                if mapa[vizinho[0]][vizinho[1]] == 1:
                    continue

                """
                CÁLCULO DE CUSTO:

                novo_custo = custo até aqui + 1 (cada passo custa 1)

                Isso representa o esforço real para chegar até esse vizinho.
                """
                novo_custo = custo_g[atual] + 1

                """
                ATUALIZAÇÃO DO CAMINHO:

                Só atualizamos se:
                - nunca visitamos esse vizinho
                OU
                - encontramos um caminho melhor até ele
                """
                if vizinho not in custo_g or novo_custo < custo_g[vizinho]:
                    custo_g[vizinho] = novo_custo

                    """
                    PRIORIDADE (ESSÊNCIA DO A*):

                    prioridade = custo real + estimativa até o destino

                    Isso permite ao algoritmo escolher caminhos mais promissores,
                    sem precisar explorar tudo.
                    """
                    prioridade = novo_custo + heuristica(vizinho, destino)

                    heapq.heappush(fila_aberta, (prioridade, vizinho))

                    """
                    REGISTRO DO CAMINHO:

                    Guarda de onde viemos para reconstruir depois.
                    """
                    veio_de[vizinho] = atual

    return None


"""
FUNÇÃO: mostrar_mapa

Responsável por exibir o resultado visualmente.

Símbolos:
S → início
G → destino
* → caminho encontrado
# → obstáculo
. → espaço livre
"""
def mostrar_mapa(mapa, caminho, inicio, destino):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if (i, j) == inicio:
                print("S", end=" ")
            elif (i, j) == destino:
                print("G", end=" ")
            elif caminho and (i, j) in caminho:
                print("*", end=" ")
            elif mapa[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()


"""
EXECUÇÃO DO PROGRAMA:

1. Carrega o mapa do CSV
2. Define início e destino
3. Executa o algoritmo A*
4. Mostra o resultado
"""
mapa = carregar_mapa()

inicio = (0, 0)
destino = (4, 4)

caminho = busca_a_estrela(mapa, inicio, destino)

print("Caminho encontrado:\n")
mostrar_mapa(mapa, caminho, inicio, destino)
