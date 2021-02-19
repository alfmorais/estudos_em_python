num = int(input("Digite um número: "))
divisores = []
ndivisores = []

for n in range(1, num + 1):
	if num % n == 0:
		divisores.append(n)

	else:
		ndivisores.append(n)

print("\nEssa é a lista dos divisores: ")
print(divisores)
print("\nEssa é a lista dos não divisores: ")
print(ndivisores)
