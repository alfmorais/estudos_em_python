""" Escreva um programa para calcular o valor da série para 5 termos: 

S = 0 + 1/2! + 2/4! + 3/6! + 4/8! + 5/10!

"""
# Programa feito sem o laço for

n2 = 2 * 1
n4 = 4 * 3 * 2 * 1
n6 = 6 * 5 * 4 * 3 * 2 * 1
n8 = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
n10 = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

s = 0 + (1 / n2) + (2 / n4) + (3 / n6) + (4 / n8) + (5 / n10)



# Programa feito com o laço for

lista1 = []
lista2 = []

for n in range(0, 6, 1):
	if n > 0:
		lista1.append(n)

resultado=1

for l in range(0, 11, 2):
	if l > 0:
		resultado *= l
		lista2.append(resultado)
		print(l)

ind0 = lista1[0] / lista2[0]
ind1 = lista1[1] / lista2[1]
ind2 = lista1[2] / lista2[2]
ind3 = lista1[3] / lista2[3]
ind4 = lista1[4] / lista2[4]

s1 = 0 + ind0 + ind1 + ind2 + ind3 + ind4
print(f'Programa sem o laço, resultado = {s}')
print(f'Programa com o laço, resultado = {s1}')
s2 = s - s1
print(f'Prova real, o número {s2}, tem que ser zero!')

