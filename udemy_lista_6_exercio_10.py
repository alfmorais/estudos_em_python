""" Faça um programa que soma os 50 primeiros números pares """
lista = []

for n in range(1, 101):
	if n % 2 == 0:
		lista.append(n)

print(lista)

print("Esta é a somatória dos números pares: usando função 'sum': ")
print(sum(lista))

# A função 'len' tem como objetivo contar a quantidade de caracteres dentro de uma lista
print("Esta é a somatória dos números pares: usando função 'len': ")
print(len(lista))
