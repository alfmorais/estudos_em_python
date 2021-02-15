soma = 0
qtd = 10 #Esse tem como colocar como input

positivo = []
negativo = []

for n in range(1, qtd + 1):
	num = int(input(f'Informe o {n}/{qtd} valor: '))
	soma = soma + num
	media = soma / 10
	if num < 0:
		negativo.append(num)
	if num > 0:
		positivo.append(num)

print(f'\nA média é {media}')
print(len(positivo))
print(len(negativo))

