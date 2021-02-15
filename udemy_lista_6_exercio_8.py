qtd = int(input("Digite a quantidade de vezes que você quer repetir: "))
lista = []

for n in range(1, qtd + 1):
	num = int(input(f'Digite um {n}/{qtd}:'))
	lista.append(num)

print(f'Esses são os números escolhidos: {lista} ')
print(f'Esse é o número maior: {max(lista)} ')
print(f'Esse é o número menor: {min(lista)} ')
