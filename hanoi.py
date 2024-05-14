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

n = int(input("Quantos discos você quer? \n>"))

pino_inicial = []

#last_target = -1
pinos = [[], [], []]
#Popula o pino 1
for i in range(n):
	pino_inicial.insert(0, i)

pinos[0] = pino_inicial.copy()

# Disco só pode ser colocado em um pino cujo último disco tenha um diâmetro maior do que o dele.
# Mover sempre pra direita
# Não pode mover o mesmo disco duas vezes seguidas
# Pino que só tem um não pode mover para vazio
#Utilidades
def move_disk(pino_origem, pino_target):
    pino_target.append(pino_origem.pop())


def print_hanoi(count):
    print(count + 1)
    print(pinos[0])
    print(pinos[1])
    print(pinos[2])
    print("\n\n")

#Escolher pino
# def choose_disk():
# 	for i in range(3):
# 		if i != last_target and len(pinos[i]) > 0:
# 			for pino in pinos:
# 				if pino != i:
# 					pinos[i] == [] or pinos[pino][-1] < pinos[i][-1]
# 			return (i, pino)
#recursão
def hanoi(last_target, count):
    #print(len(pinos))
    #print(pinos[0])
    origin = -1
    target = -1
    for i in range(3):
        #print("i: " + str(i))
        if i != last_target and len(pinos[i]) > 0:
            for pino_alvo in range(len(pinos)):
                #print("pino: " + str(pino_alvo))
                if pinos[pino_alvo] != i:
                    if (pinos[pino_alvo] == [] or pinos[pino_alvo][-1] > pinos[i][-1]):
                        origin = i
                        target = pino_alvo
                        #print("ACERTOU:", origin, target)
                        if n % 2.0 == 0 and count == 0:
                            break

    move_disk(pinos[origin], pinos[target])

    if pinos[2] != pino_inicial:
        print_hanoi(count)
        hanoi(target, count + 1)
    else:
        print("MÃE EU TO FAMOSO!\n")
        print_hanoi(count)
	# if p3 != pino_inicial:
	# 	hanoi()
	# else:
	# 	print("Yay")

hanoi(-1, 0)