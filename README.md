O problema abordado neste trabalho consiste em encontrar o menor caminho entre dois pontos 
em um ambiente bidimensional discreto, representado por uma grade (matriz), que pode conter obstáculos. 
Trata-se de um problema clássico da Inteligência Artificial e da Ciência da Computação, 
com ampla aplicabilidade em jogos digitais, robótica, sistemas de navegação, 
logística e planejamento autônomo de trajetórias. 

Formalmente, o ambiente é modelado como uma matriz de células, onde cada célula pode 
assumir dois valores: 0 (célula livre, transitável) ou 1 (obstáculo, intransitável). 
O agente parte de um ponto de origem, denominado S (Start), e deve alcançar um ponto de destino, 
denominado G (Goal), percorrendo apenas células livres e realizando movimentos em quatro direções possíveis: 
cima, baixo, esquerda e direita — sem movimentos diagonais. 

O objetivo é determinar o caminho com o menor número de passos possível entre os dois pontos, 
evitando os obstáculos. A solução implementada utiliza o algoritmo A* (A-estrela), 
amplamente reconhecido como um dos algoritmos de busca informada mais eficientes para este tipo de problema. 
