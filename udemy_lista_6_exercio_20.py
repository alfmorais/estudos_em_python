n = int(input("Digite um número: "))

for n1 in range(n + 1):
	if n1 % 2 == 0:
		print(f'O número digitado {n1} é PAR!')
	elif n1 % 2 != 0:
		print(f'O número digitado {n1} é IMPAR!')

print("")
