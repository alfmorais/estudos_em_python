num = int(input("Digite um número: "))

div = []
ndv = []

for n in range(1, num + 1):
	if num % n == 0:
		div.append(n)

	else:
		ndv.append(n)

print("\nEsses são os divisores do número " + str(num) + " escolhido.")
print(div)

somadiv = sum(div)

print(f'Essa é a soma dos divisores {somadiv}')
