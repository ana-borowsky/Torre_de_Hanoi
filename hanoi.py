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

last_target = -1
pinos = [[], [], []]
p1 = pinos[0]
p2 = pinos[1]
p3 = pinos[2]

#Popula o pino 1
for i in range(n):
	pino_inicial.append(i)

p1 = pino_inicial.copy()

# Disco só pode ser colocado em um pino cujo último disco tenha um diâmetro maior do que o dele.
# Mover sempre pra direita
# Não pode mover o mesmo disco duas vezes seguidas

#Utilidades
def move_disk(pino_origem, pino_target):
	pino_target.append(pino_origem.pop())

#Escolher pino
# def choose_disk():
# 	for i in range(3):
# 		if i != last_target and len(pinos[i]) > 0:
# 			for pino in pinos:
# 				if pino != i:
# 					pinos[i] == [] or pinos[pino][-1] < pinos[i][-1]
# 			return (i, pino)

#recursão
def hanoi():
	origin = -1
	target = -1
	for i in range(3):
		if i != last_target and len(pinos[i]) > 0:
 			for pino in pinos:
 				if pino != i:
 					if pinos[i] == [] or pinos[pino][-1] < pinos[i][-1]:
                        print(origin, target)
		
	# if p3 != pino_inicial:
	# 	hanoi()
	# else:
	# 	print("Yay")

hanoi()
# print(p1)
# print(p2)
# print(p3)

