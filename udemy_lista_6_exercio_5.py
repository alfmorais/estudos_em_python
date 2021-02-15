soma = 0
qtd = 10
for n in range(1, qtd + 1):
	num = int(input(f'Informe o {n}/{qtd} valor: '))
	soma = soma + num

print(f'A soma é {soma}')
