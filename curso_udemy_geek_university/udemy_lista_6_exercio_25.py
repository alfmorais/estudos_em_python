num = int(input("Digite um número: "))
mult3 = []
mult5 = []

for n in range(0, num + 1, 3):
	mult3.append(n)

for n in range(0, num + 1, 5):
	mult5.append(n)

print(f'Esse são multiplos de 3: {mult3}')
print(f'Esse são multiplos de 5: {mult5}')
