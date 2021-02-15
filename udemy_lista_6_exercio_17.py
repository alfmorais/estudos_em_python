"""
Faça um programa que leia um número inteiro positivo N e calcule a soma dos N
primeiros números naturais.

"""

n = int(input("Digite um número: "))
lista = []

for num in range(n+1):
	print(num)
	lista.append(num)

print("Essa é a soma dos 10 primeiros números!")
print(sum(lista[0:11]))
