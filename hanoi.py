'''
Crie um algorítmo recursivo para o quebra-cabeça da Torre de Hanoi, com 7 discos.

        0       ||      ||
        1       ||      ||
        2       ||      || 
        3       ||      ||
        4       ||      ||
        5       ||      ||
        6       ||      ||
=================================

Iterações: 
S(1) = 
1 = [6, 5, 4, 3, 2, 1, 0]
2 = []
3 = []   

S(2) = 
1 = [6, 5, 4, 3, 2, 1]
2 = [0]
3 = []

S(3) = 
1 = [6, 5, 4, 3, 2]
2 = [0]
3 = [1]

S(4) = 
1 = [6, 5, 4, 3, 2]
2 = []
3 = [1, 0]

S(5) = 
1 = [6, 5, 4, 3]
2 = [2]
3 = [1, 0]

S(6) = 
1 = [6, 5, 4, 3, 0]
2 = [2]
3 = [1]

S(7) = 
1 = [6, 5, 4, 3, 0]
2 = [2, 1]
3 = []

S(8) = 
1 = [6, 5, 4, 3]
2 = [2, 1, 0]
3 = []

S(9) = 
1 = [6, 5, 4]
2 = [2, 1, 0]
3 = [3]

S(10) = 
1 = [6, 5, 4] 
2 = [2, 1]
3 = [3, 0]
'''

pino_1 = [6, 5, 4, 3, 2, 1, 0, None]
pino_2 = [None]
pino_3 = [None]

# Disco só pode ser colocado em um pino cujo último disco tenha um diâmetro maior do que o dele.
# Mover sempre pra direita
# Não pode mover o mesmo disco duas vezes seguidas



pino_inicial = [6, 5, 4, 3, 2, 1, 0] # Pegar por input do usuário o tamanho do array ou escolher default
pino_2[0] = pino_1.pop() # S(1)
pino_3[0] = pino_1.pop() # S(2)

while pino_3 != pino_inicial:



print(pino_1)
print(pino_2)
print(pino_3)

