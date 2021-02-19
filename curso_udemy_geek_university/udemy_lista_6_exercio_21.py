""" Lições Aprendidas:
Função numpy para multiplicação de lista. 

FONTE: https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/

"""

import numpy

n1 = int(input("Digite 1º nº (menor): "))
n2 = int(input("Digite 2º nº (maior): "))

soma = []
mult = []

for s in range(n1, n2 + 1):
	if s % 2 == 0:
		soma.append(s)

for m in range(n1, n2 + 1):
	if m % 2 != 0:
		mult.append(m)

soma2 = sum(soma)
mult2 = numpy.prod(mult)

print(f'\nEsta é a soma dos intervalos do 1º e 2º nº: {soma2}')
print(soma)
print(f'\nEsta é a mult. dos intervalos do 1º e 2º nº: {mult2}')
print(mult)

