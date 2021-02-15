""" Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais impares """

num = int(input("Digite um número N: "))
lista = []

for n in range(1, num + 1, 2):
	lista.append(n)

print("Esse são os número naturais impares do número digitado!")
print(lista)

